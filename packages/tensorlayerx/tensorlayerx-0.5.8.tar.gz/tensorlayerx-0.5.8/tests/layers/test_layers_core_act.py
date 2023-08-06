#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorlayerx
import tensorlayerx as tlx

from tests.utils import CustomTestCase


class Layer_Convolution_2D_Test(CustomTestCase):

    @classmethod
    def setUpClass(self):
        self.batch_size = 5
        self.inputs_shape = [self.batch_size, 400, 400, 3]
        self.input_layer = tlx.nn.Input(self.inputs_shape, name='input_layer')

        self.conv2dlayer1 = tlx.nn.Conv2d(
            out_channels=32, in_channels=3, act=tlx.ReLU, kernel_size=(5, 5), stride=(2, 2), padding='SAME',
            b_init=tensorlayerx.nn.initializers.constant(value=0.0), name='conv2dlayer'
        )
        self.n1 = self.conv2dlayer1(self.input_layer)

        self.conv2dlayer2 = tlx.nn.Conv2d(
            out_channels=32, in_channels=32, kernel_size=(3, 3), stride=(2, 2), act="relu", name='conv2d'
        )
        self.n2 = self.conv2dlayer2(self.n1)

        self.conv2dlayer3 = tlx.nn.Conv2d(
            out_channels=32, in_channels=32, kernel_size=(3, 3), stride=(2, 2), act="leaky_relu", b_init=None
        )
        self.n3 = self.conv2dlayer3(self.n2)

        self.conv2dlayer4 = tlx.nn.Conv2d(
            out_channels=32, in_channels=32, kernel_size=(3, 3), stride=(2, 2), act="lrelu", b_init=None
        )
        self.n4 = self.conv2dlayer4(self.n3)

        self.conv2dlayer5 = tlx.nn.Conv2d(
            out_channels=32, in_channels=32, kernel_size=(3, 3), stride=(2, 2), act="sigmoid"
        )
        self.n5 = self.conv2dlayer5(self.n4)

        self.conv2dlayer6 = tlx.nn.Conv2d(
            out_channels=32, in_channels=32, kernel_size=(3, 3), stride=(2, 2), act="tanh"
        )
        self.n6 = self.conv2dlayer6(self.n5)

        self.conv2dlayer7 = tlx.nn.Conv2d(
            out_channels=32, kernel_size=(3, 3), stride=(2, 2), act="leaky_relu0.22", in_channels=32
        )
        self.n7 = self.conv2dlayer7(self.n6)

        self.conv2dlayer8 = tlx.nn.Conv2d(
            out_channels=32, kernel_size=(3, 3), stride=(2, 2), act="lrelu0.22", in_channels=32
        )
        self.n8 = self.conv2dlayer8(self.n7)

        self.conv2dlayer9 = tlx.nn.Conv2d(
            out_channels=32, kernel_size=(3, 3), stride=(2, 2), act="softplus", in_channels=32
        )
        self.n9 = self.conv2dlayer9(self.n8)

        self.conv2dlayer10 = tlx.nn.Conv2d(
            out_channels=32, kernel_size=(3, 3), stride=(2, 2), act="relu6", in_channels=32
        )
        self.n10 = self.conv2dlayer10(self.n9)

    @classmethod
    def tearDownClass(self):
        pass

    def test_relu(self):
        self.assertEqual(tlx.get_tensor_shape(self.n1), [5, 200, 200, 32])

    def test_relu_str(self):
        self.assertEqual(tlx.get_tensor_shape(self.n2), [5, 100, 100, 32])

    def test_leaky_relu_str(self):
        self.assertEqual(tlx.get_tensor_shape(self.n3), [5, 50, 50, 32])

    def test_lrelu_str(self):
        self.assertEqual(tlx.get_tensor_shape(self.n4), [5, 25, 25, 32])

    def test_sigmoid_str(self):
        self.assertEqual(tlx.get_tensor_shape(self.n5), [5, 13, 13, 32])

    def test_tanh_str(self):
        self.assertEqual(tlx.get_tensor_shape(self.n6), [5, 7, 7, 32])

    def test_leaky_relu_float_str(self):
        self.assertEqual(tlx.get_tensor_shape(self.n7), [5, 4, 4, 32])

    def test_lrelu_float_str(self):
        self.assertEqual(tlx.get_tensor_shape(self.n8), [5, 2, 2, 32])

    def test_softplus_str(self):
        self.assertEqual(tlx.get_tensor_shape(self.n9), [5, 1, 1, 32])

    def test_relu6_str(self):
        self.assertEqual(tlx.get_tensor_shape(self.n10), [5, 1, 1, 32])


if __name__ == '__main__':

    tlx.logging.set_verbosity(tlx.logging.DEBUG)

    unittest.main()
