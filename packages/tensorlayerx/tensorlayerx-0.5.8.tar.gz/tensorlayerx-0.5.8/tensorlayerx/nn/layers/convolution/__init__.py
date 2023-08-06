#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
TensorLayer provides rich layer implementations trailed for
various benchmarks and domain-specific problems. In addition, we also
support transparent access to native TensorFlow parameters.
For example, we provide not only layers for local response normalization, but also
layers that allow user to apply ``tf.ops.lrn`` on ``network.outputs``.
More functions can be found in `TensorFlow API <https://www.tensorflow.org/versions/master/api_docs/index.html>`__.
"""

from .binary_conv import *
from .deformable_conv import *
from .depthwise_conv import *
from .dorefa_conv import *
# from .expert_conv import *
# from .expert_deconv import *
from .group_conv import *
from .quan_conv import *
from .quan_conv_bn import *
from .separable_conv import *
from .simplified_conv import *
# from .simplified_deconv import *
from .super_resolution import *
from .ternary_conv import *
from .mask_conv import *

__all__ = [

    # simplified conv
    'Conv1d',
    'Conv2d',
    'Conv3d',

    # simplified deconv
    'ConvTranspose1d',
    'ConvTranspose2d',
    'ConvTranspose3d',

    # binary
    'BinaryConv2d',

    # deformable
    'DeformableConv2d',

    # depthwise
    'DepthwiseConv2d',

    # dorefa
    'DorefaConv2d',

    # group
    'GroupConv2d',

    # separable
    'SeparableConv1d',
    'SeparableConv2d',

    # subpixel
    'SubpixelConv1d',
    'SubpixelConv2d',

    # ternary
    'TernaryConv2d',

    #quan_conv
    'QuanConv2d',
    'QuanConv2dWithBN',

    # masked conv
    'MaskedConv3d'
]
