#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorlayerx
import tensorlayerx as tlx

from tests.utils import CustomTestCase


class Activation_Layer_Test(CustomTestCase):

    @classmethod
    def setUpClass(self):
        self.inputs = tlx.layers.Input([10, 5])

    @classmethod
    def tearDownClass(self):
        pass

    def test_prelu_1(self):
        prelulayer = tlx.layers.PRelu()

        class prelu_model(tensorlayerx.nn.Module):

            def __init__(self):
                super(prelu_model, self).__init__()
                self.prelu = prelulayer

            def forward(self, inputs):
                return self.prelu(inputs)

        net = prelu_model()

        self.assertTrue(tlx.get_tensor_shape(net(self.inputs)), [10, 5])

    def test_prelu_2(self):
        prelulayer = tensorlayerx.layers.PRelu(num_parameters=5)
        prelu = prelulayer(self.inputs)

        self.assertTrue(tlx.get_tensor_shape(prelu), [10, 5])

    def test_prelu6_1(self):
        prelu6layer = tensorlayerx.layers.PRelu6(in_channels=5)
        prelu6 = prelu6layer(self.inputs)

        self.assertTrue(tlx.get_tensor_shape(prelu6), [10, 5])

    def test_prelu6_2(self):
        prelu6layer = tensorlayerx.layers.PRelu6(channel_shared=True)

        class prelu6_model(tensorlayerx.nn.Module):

            def __init__(self):
                super(prelu6_model, self).__init__()
                self.prelu = prelu6layer

            def forward(self, inputs):
                return self.prelu(inputs)

        net = prelu6_model()

        self.assertTrue(tlx.get_tensor_shape(net(self.inputs)), [10, 5])

    def test_ptrelu6_1(self):
        ptrelu6layer = tensorlayerx.layers.PTRelu6(channel_shared=True)
        ptrelu6 = ptrelu6layer(self.inputs)

        self.assertTrue(tlx.get_tensor_shape(ptrelu6), [10, 5])

    def test_ptrelu6_2(self):
        ptrelu6layer = tensorlayerx.layers.PTRelu6(in_channels=5)

        class ptrelu6_model(tensorlayerx.nn.Module):

            def __init__(self):
                super(ptrelu6_model, self).__init__()
                self.prelu = ptrelu6layer

            def forward(self, inputs):
                return self.prelu(inputs)

        net = ptrelu6_model()

        self.assertTrue(tlx.get_tensor_shape(net(self.inputs)), [10, 5])

    def test_lrelu(self):
        lrelulayer = tensorlayerx.layers.LeakyReLU(negative_slope=0.5)
        lrelu = lrelulayer(self.inputs)

        self.assertTrue(tlx.get_tensor_shape(lrelu), [5, 10])

    def test_lrelu6(self):
        lrelu6layer = tensorlayerx.layers.LeakyReLU6(alpha=0.5)
        lrelu6 = lrelu6layer(self.inputs)

        self.assertTrue(tlx.get_tensor_shape(lrelu6), [5, 10])

    def test_ltrelu6(self):
        ltrelu6layer = tensorlayerx.layers.LeakyTwiceRelu6()
        ltrelu6 = ltrelu6layer(self.inputs)

        self.assertTrue(tlx.get_tensor_shape(ltrelu6), [5, 10])

    def test_swish(self):
        swishlayer = tensorlayerx.layers.Swish()
        swish = swishlayer(self.inputs)

        self.assertTrue(tlx.get_tensor_shape(swish), [5, 10])

    def test_hardtanh(self):
        hardtanhlayer = tensorlayerx.layers.HardTanh()
        hardtanh = hardtanhlayer(self.inputs)

        self.assertTrue(tlx.get_tensor_shape(hardtanh), [5, 10])

    def test_mish(self):
        mishlayer = tensorlayerx.layers.Mish()
        mish = mishlayer(self.inputs)

        self.assertTrue(tlx.get_tensor_shape(mish), [5, 10])


if __name__ == '__main__':

    unittest.main()
