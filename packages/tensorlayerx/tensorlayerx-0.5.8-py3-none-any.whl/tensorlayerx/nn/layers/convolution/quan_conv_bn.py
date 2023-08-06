#! /usr/bin/python
# -*- coding: utf-8 -*-

import tensorlayerx as tlx
from tensorlayerx import logging
from tensorlayerx.nn.core import Module
from tensorlayerx.backend import BACKEND

__all__ = ['QuanConv2dWithBN']


class QuanConv2dWithBN(Module):
    """The :class:`QuanConv2dWithBN` class is a quantized convolutional layer with BN, which weights are 'bitW' bits and the output of the previous layer
    are 'bitA' bits while inferencing.

    Note that, the bias vector would keep the same.

    Parameters
    ----------
    out_channels : int
        The number of filters.
    kernel_size : tuple or int
        The filter size (height, width).
    stride : tuple or int
        The sliding window stride of corresponding input dimensions.
        It must be in the same order as the ``shape`` parameter.
    padding : str
        The padding algorithm type: "SAME" or "VALID".
    act : activation function
        The activation function of this layer.
    decay : float
        A decay factor for `ExponentialMovingAverage`.
        Suggest to use a large value for large dataset.
    epsilon : float
        Eplison.
    is_train : boolean
        Is being used for training or inference.
    beta_init : initializer or None or str
        The initializer for initializing beta, if None, skip beta.
        Usually you should not skip beta unless you know what happened.
    gamma_init : initializer or None or str
        The initializer for initializing gamma, if None, skip gamma.
    bitW : int
        The bits of this layer's parameter
    bitA : int
        The bits of the output of previous layer
    use_gemm : boolean
        If True, use gemm instead of ``tf.matmul`` for inferencing. (TODO).
    W_init : initializer or str
        The initializer for the the weight matrix.
    W_init_args : dictionary
        The arguments for the weight matrix initializer.
    data_format : str
        "NHWC" or "NCHW", default is "NHWC".
    dilation : tuple or int
        Specifying the dilation rate to use for dilated convolution.
    in_channels : int
        The number of in channels.
    name : str
        A unique layer name.

    Examples
    ---------
    >>> import tensorlayerx as tlx
    >>> net = tlx.nn.Input([50, 256, 256, 3])
    >>> layer = tlx.nn.QuanConv2dWithBN(out_channels=64, kernel_size=(5,5),stride=(1,1),padding='SAME',name='qcnnbn1')
    >>> print(layer)
    >>> net = tlx.nn.QuanConv2dWithBN(out_channels=64, kernel_size=(5,5),stride=(1,1),padding='SAME',name='qcnnbn1')(net)
    >>> print(net)
    """

    def __init__(
        self,
        out_channels=32,
        kernel_size=(3, 3),
        stride=(1, 1),
        padding='SAME',
        act=None,
        decay=0.9,
        epsilon=1e-5,
        is_train=False,
        gamma_init='truncated_normal',
        beta_init='truncated_normal',
        bitW=8,
        bitA=8,
        use_gemm=False,
        W_init='truncated_normal',
        W_init_args=None,
        data_format="channels_last",
        dilation=(1, 1),
        in_channels=None,
        name='quan_cnn2d_bn',
    ):
        super(QuanConv2dWithBN, self).__init__(act=act, name=name)
        self.out_channels = out_channels
        self.kernel_size = self.check_param(kernel_size)
        self.stride = self.check_param(stride)
        self.padding = padding
        self.decay = decay
        self.epsilon = epsilon
        self.is_train = is_train
        self.gamma_init = self.str_to_init(gamma_init)
        self.beta_init = self.str_to_init(beta_init)
        self.bitW = bitW
        self.bitA = bitA
        self.use_gemm = use_gemm
        self.W_init = self.str_to_init(W_init)
        self.W_init_args = W_init_args
        self.data_format = data_format
        self.dilation = self.check_param(dilation)
        self.in_channels = in_channels
        logging.info(
            "QuanConv2dWithBN %s: out_channels: %d kernel_size: %s stride: %s pad: %s act: %s " % (
                self.name, out_channels, kernel_size, str(stride), padding,
                self.act.__class__.__name__ if self.act is not None else 'No Activation'
            )
        )

        if BACKEND == 'mindspore':
            raise NotImplementedError("MindSpore backend does not implement this method")

        if self.in_channels:
            self.build(None)
            self._built = True

        if use_gemm:
            raise Exception("TODO. The current version use tf.matmul for inferencing.")

        if len(stride) != 2:
            raise ValueError("len(stride) should be 2.")

    def __repr__(self):
        actstr = self.act.__class__.__name__ if self.act is not None else 'No Activation'
        s = (
            '{classname}(in_channels={in_channels}, out_channels={out_channels}, kernel_size={kernel_size}'
            ', stride={stride}, padding={padding}' + actstr
        )
        if self.dilation != (1, ) * len(self.dilation):
            s += ', dilation={dilation}'
        if self.name is not None:
            s += ', name=\'{name}\''
        s += ')'
        return s.format(classname=self.__class__.__name__, **self.__dict__)

    def build(self, inputs_shape):
        if self.data_format == 'channels_last':
            self.data_format = 'NHWC'
            if self.in_channels is None:
                self.in_channels = inputs_shape[-1]
            self._strides = [1, self.stride[0], self.stride[1], 1]
            self._dilation_rate = [1, self.dilation[0], self.dilation[1], 1]
        elif self.data_format == 'channels_first':
            self.data_format = 'NCHW'
            if self.in_channels is None:
                self.in_channels = inputs_shape[1]
            self._strides = [1, 1, self.stride[0], self.stride[1]]
            self._dilation_rate = [1, 1, self.dilation[0], self.dilation[1]]
        else:
            raise Exception("data_format should be either channels_last or channels_first")

        self.filter_shape = (self.kernel_size[0], self.kernel_size[1], self.in_channels, self.out_channels)
        self.filters = self._get_weights("filters", shape=self.filter_shape, init=self.W_init)

        para_bn_shape = (self.out_channels, )
        if self.gamma_init:
            self.scale_para = self._get_weights(
                "scale_para", shape=para_bn_shape, init=self.gamma_init, trainable=self.is_train
            )
        else:
            self.scale_para = None

        if self.beta_init:
            self.offset_para = self._get_weights(
                "offset_para", shape=para_bn_shape, init=self.beta_init, trainable=self.is_train
            )
        else:
            self.offset_para = None

        self.moving_mean = self._get_weights(
            "moving_mean", shape=para_bn_shape, init=tlx.nn.initializers.constant(1.0), trainable=False
        )
        self.moving_variance = self._get_weights(
            "moving_variance", shape=para_bn_shape, init=tlx.nn.initializers.constant(1.0), trainable=False
        )

        self.quan_conv_bn = tlx.ops.QuanConvBn(
            weights=self.filters, scale_para=self.scale_para, offset_para=self.offset_para, moving_mean=self.moving_mean,
            moving_variance=self.moving_variance, strides=self._strides, padding=self.padding,
            data_format=self.data_format, dilations=self._dilation_rate, bitW=self.bitW, bitA=self.bitA,
            decay=self.decay, epsilon=self.epsilon, is_train=self.is_train
        )

    def forward(self, inputs):
        if self._forward_state == False:
            if self._built == False:
                self.build(tlx.get_tensor_shape(inputs))
                self._built = True
            self._forward_state = True

        conv_fold = self.quan_conv_bn(inputs)

        if self.act:
            conv_fold = self.act(conv_fold)

        if not self._nodes_fixed and self._build_graph:
            self._add_node(inputs, conv_fold)
            self._nodes_fixed = True
        return conv_fold
