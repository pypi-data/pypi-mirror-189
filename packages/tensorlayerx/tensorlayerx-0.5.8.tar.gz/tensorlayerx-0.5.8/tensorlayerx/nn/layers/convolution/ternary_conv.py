#! /usr/bin/python
# -*- coding: utf-8 -*-

import tensorlayerx as tlx
from tensorlayerx import logging
from tensorlayerx.nn.core import Module

__all__ = ['TernaryConv2d']


class TernaryConv2d(Module):
    """
    The :class:`TernaryConv2d` class is a 2D ternary CNN layer, which weights are either -1 or 1 or 0 while inference.

    Note that, the bias vector would not be tenarized.

    Parameters
    ----------
    out_channels : int
        The number of filters.
    kernel_size : tuple or int
        The filter size (height, width).
    stride : tuple or int
        The sliding window stride of corresponding input dimensions.
        It must be in the same order as the ``shape`` parameter.
    act : activation function
        The activation function of this layer.
    padding : str
        The padding algorithm type: "SAME" or "VALID".
    use_gemm : boolean
        If True, use gemm instead of ``tf.matmul`` for inference.
        TODO: support gemm
    data_format : str
        "channels_last" (NHWC, default) or "channels_first" (NCHW).
    dilation_rate : tuple or int
        Specifying the dilation rate to use for dilated convolution.
    W_init : initializer or str
        The initializer for the the weight matrix.
    b_init : initializer or None or str
        The initializer for the the bias vector. If None, skip biases.
    in_channels : int
        The number of in channels.
    name : None or str
        A unique layer name.

    Examples
    ---------
    With TensorLayer

    >>> net = tlx.nn.Input([8, 12, 12, 32], name='input')
    >>> ternaryconv2d = tlx.nn.TernaryConv2d(
    ...     out_channels=64, kernel_size=(5, 5), stride=(1, 1), act=tlx.ReLU, padding='SAME', name='ternaryconv2d'
    ... )(net)
    >>> print(ternaryconv2d)
    >>> output shape : (8, 12, 12, 64)

    """

    def __init__(
        self,
        out_channels=32,
        kernel_size=(3, 3),
        stride=(1, 1),
        act=None,
        padding='SAME',
        use_gemm=False,
        data_format="channels_last",
        dilation=(1, 1),
        W_init='truncated_normal',
        b_init='constant',
        in_channels=None,
        name=None  # 'ternary_cnn2d',
    ):
        super().__init__(name, act=act)
        self.out_channels = out_channels
        self.kernel_size = self.check_param(kernel_size)
        self.stride = self._strides = self.check_param(stride)
        self.padding = padding
        self.use_gemm = use_gemm
        self.data_format = data_format
        self.dilation_rate = self._dilation_rate = self.check_param(dilation)
        self.W_init = self.str_to_init(W_init)
        self.b_init = self.str_to_init(b_init)
        self.in_channels = in_channels

        if self.in_channels:
            self.build(None)
            self._built = True

        logging.info(
            "TernaryConv2d %s: out_channels: %d kernel_size: %s stride: %s pad: %s act: %s" % (
                self.name, out_channels, str(kernel_size), str(stride), padding,
                self.act.__class__.__name__ if self.act is not None else 'No Activation'
            )
        )

        if use_gemm:
            raise Exception("TODO. The current version use tf.matmul for inferencing.")

        if len(self.stride) != 2:
            raise ValueError("len(stride) should be 2.")

    def __repr__(self):
        actstr = self.act.__name__ if self.act is not None else 'No Activation'
        s = (
            '{classname}(in_channels={in_channels}, out_channels={out_channels}, kernel_size={kernel_size}'
            ', stride={stride}, padding={padding}'
        )
        if self.dilation_rate != (1, ) * len(self.dilation_rate):
            s += ', dilation={dilation_rate}'
        if self.b_init is None:
            s += ', bias=False'
        s += (', ' + actstr)
        if self.name is not None:
            s += ', name=\'{name}\''
        s += ')'
        return s.format(classname=self.__class__.__name__, **self.__dict__)

    def build(self, inputs_shape):
        if self.data_format == 'channels_last':
            self.data_format = 'NHWC'
            if self.in_channels is None:
                self.in_channels = inputs_shape[-1]
            self._strides = [1, self._strides[0], self._strides[1], 1]
            self._dilation_rate = [1, self._dilation_rate[0], self._dilation_rate[1], 1]
        elif self.data_format == 'channels_first':
            self.data_format = 'NCHW'
            if self.in_channels is None:
                self.in_channels = inputs_shape[1]
            self._strides = [1, 1, self._strides[0], self._strides[1]]
            self._dilation_rate = [1, 1, self._dilation_rate[0], self._dilation_rate[1]]
        else:
            raise Exception("data_format should be either channels_last or channels_first")

        self.filter_shape = (self.kernel_size[0], self.kernel_size[1], self.in_channels, self.out_channels)

        self.filters = self._get_weights("filters", shape=self.filter_shape, init=self.W_init)
        if self.b_init:
            self.biases = self._get_weights("biases", shape=(self.out_channels, ), init=self.b_init)
            self.bias_add = tlx.ops.BiasAdd(data_format=self.data_format)

        self.ternary_conv = tlx.ops.TernaryConv(
            weights=self.filters, strides=self._strides, padding=self.padding, data_format=self.data_format,
            dilations=self._dilation_rate
        )

    def forward(self, inputs):
        if self._forward_state == False:
            if self._built == False:
                self.build(tlx.get_tensor_shape(inputs))
                self._built = True
            self._forward_state = True

        outputs = self.ternary_conv(inputs)

        if self.b_init:
            outputs = self.bias_add(outputs, self.biases)
        if self.act:
            outputs = self.act(outputs)

        if not self._nodes_fixed and self._build_graph:
            self._add_node(inputs, outputs)
            self._nodes_fixed = True
        return outputs
