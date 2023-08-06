#! /usr/bin/python
# -*- coding: utf-8 -*-

import tensorlayerx as tlx
from tensorlayerx import logging
from tensorlayerx.nn.core import Module

__all__ = [
    'UpSampling2d',
    'DownSampling2d',
]


class UpSampling2d(Module):
    """The :class:`UpSampling2d` class is a up-sampling 2D layer.

    See `tf.image.resize_images <https://www.tensorflow.org/api_docs/python/tf/image/resize_images>`__.

    Parameters
    ----------
    scale : int or tuple of int
        (scale_height, scale_width) scale factor. scale_height = new_height/height, scale_width = new_width/width.
    method : str
        The resize method selected through the given string. Default 'bilinear'.
            - 'bilinear', Bilinear interpolation.
            - 'nearest', Nearest neighbor interpolation.
            - 'bicubic', Bicubic interpolation.
            - 'area', Area interpolation.
    antialias : boolean
        Whether to use an anti-aliasing filter when downsampling an image.
    data_format : str
        channels_last 'channel_last' (default) or channels_first.
    name : None or str
        A unique layer name.

    Examples
    ---------
    With TensorLayer

    >>> ni = tlx.nn.Input([10, 50, 50, 32], name='input')
    >>> ni = tlx.nn.UpSampling2d(scale=(2, 2))(ni)
    >>> output shape : [10, 100, 100, 32]

    """

    def __init__(self, scale, method='bilinear', antialias=False, data_format='channels_last', name=None, ksize=None):
        super(UpSampling2d, self).__init__(name)
        self.method = method
        self.antialias = antialias
        self.data_format = data_format
        self.ksize = ksize

        logging.info(
            "UpSampling2d %s: scale: %s method: %s antialias: %s" % (self.name, scale, self.method, self.antialias)
        )

        if isinstance(scale, (list, tuple)) and len(scale) != 2:
            raise ValueError("out_size must be int or tuple/list of length 2")

        self.scale = (scale, scale) if isinstance(scale, int) else scale
        self.build(None)
        self._built = True

    def __repr__(self):
        s = '{classname}(scale={scale}, method={method}'
        if self.name is not None:
            s += ', name=\'{name}\''
        s += ')'
        return s.format(classname=self.__class__.__name__, scale=self.scale, method=self.method, name=self.name)

    def build(self, inputs_shape):
        self.resize = tlx.ops.Resize(
            scale=self.scale, method=self.method, antialias=self.antialias, data_format=self.data_format
        )

    def forward(self, inputs):
        """

        Parameters
        ------------
        inputs : :class:`Tensor`
            Inputs tensors with 4-D Tensor of the shape (batch, height, width, channels)
        """
        outputs = self.resize(inputs)

        if not self._nodes_fixed and self._build_graph:
            self._add_node(inputs, outputs)
            self._nodes_fixed = True
        return outputs


class DownSampling2d(Module):
    """The :class:`DownSampling2d` class is down-sampling 2D layer.

    See `tf.image.resize_images <https://www.tensorflow.org/versions/master/api_docs/python/image/resizing#resize_images>`__.

    Parameters
    ----------
    scale : int or tuple of int
        (new_height, new_width) scale factor.scale_height = new_height/height, scale_width = new_width/width.
    method : str
        The resize method selected through the given string. Default 'bilinear'.
            - 'bilinear', Bilinear interpolation.
            - 'nearest', Nearest neighbor interpolation.
            - 'bicubic', Bicubic interpolation.
            - 'area', Area interpolation.
    antialias : boolean
        Whether to use an anti-aliasing filter when downsampling an image.
    data_format : str
        channels_last 'channel_last' (default) or channels_first.
    name : None or str
        A unique layer name.

    Examples
    ---------
    With TensorLayer

    >>> ni = tlx.nn.Input([10, 50, 50, 32], name='input')
    >>> ni = tlx.nn.DownSampling2d(scale=(2, 2))(ni)
    >>> output shape : [10, 25, 25, 32]

    """

    def __init__(self, scale, method='bilinear', antialias=False, data_format='channels_last', name=None, ksize=None):
        super(DownSampling2d, self).__init__(name)
        self.method = method
        self.antialias = antialias
        self.data_format = data_format
        self.ksize = ksize
        logging.info(
            "DownSampling2d %s: scale: %s method: %s antialias: %s" % (self.name, scale, self.method, self.antialias)
        )

        if isinstance(scale, (list, tuple)) and len(scale) != 2:
            raise ValueError("scale must be int or tuple/list of length 2")

        self.scale = (scale, scale) if isinstance(scale, int) else scale

        self.build(None)
        self._built = True

    def __repr__(self):
        s = '{classname}(scale={scale}, method={method}'
        if self.name is not None:
            s += ', name=\'{name}\''
        s += ')'
        return s.format(classname=self.__class__.__name__, scale=self.scale, method=self.method, name=self.name)

    def build(self, inputs_shape):
        scale = [1.0 / self.scale[0], 1.0 / self.scale[1]]
        self.resize = tlx.ops.Resize(
            scale=scale, method=self.method, antialias=self.antialias, data_format=self.data_format
        )

    def forward(self, inputs):
        """

        Parameters
        ------------
        inputs : :class:`Tensor`
            Inputs tensors with 4-D Tensor of the shape (batch, height, width, channels)
        """

        outputs = self.resize(inputs)

        if not self._nodes_fixed and self._build_graph:
            self._add_node(inputs, outputs)
            self._nodes_fixed = True
        return outputs
