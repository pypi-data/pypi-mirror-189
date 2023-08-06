#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("/home/wurundi/workspace/tensorlayer2")

import os
import unittest

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorlayerx as tlx
from tensorlayerx.nn import Input
import tensorlayerx
from tests.utils import CustomTestCase


class Layer_Pooling_Test(CustomTestCase):

    @classmethod
    def setUpClass(cls):

        ## 1D ========================================================================

        ## 2D ========================================================================

        x_2_input_shape = [None, 100, 100, 3]
        nin_2 = Input(x_2_input_shape)


        n6 = tlx.nn.Conv2d(out_channels=32, kernel_size=(3, 3), stride=(2, 2), name='test_conv2d')(nin_2)

        n7 = tlx.nn.UpSampling2d(scale=(2, 2), name='test_UpSampling2d_1')(n6)

        n8 = tlx.nn.UpSampling2d(scale=3, name='test_UpSampling2d_2')(n6)

        n9 = tlx.nn.DownSampling2d(scale=(2, 2), name='test_DownSampling2d_1')(n6)

        n10 = tlx.nn.DownSampling2d(scale=5, name='test_DownSampling2d_2')(n6)

        cls.n6_shape = n6.get_shape().as_list()
        cls.n7_shape = n7.get_shape().as_list()
        cls.n8_shape = n8.get_shape().as_list()
        cls.n9_shape = n9.get_shape().as_list()
        cls.n10_shape = n10.get_shape().as_list()

    @classmethod
    def tearDownClass(cls):
        pass
        # tf.reset_default_graph()

    def test_UpSampling2d(self):
        self.assertEqual(self.n7_shape[1:3], [100, 100])
        self.assertEqual(self.n8_shape[1:3], [150, 150])

        try:
            layer = tlx.nn.UpSampling2d(scale=(2, 2, 2))
        except Exception as e:
            print(e)

    def test_DownSampling2d(self):
        self.assertEqual(self.n9_shape[1:3], [25, 25])
        self.assertEqual(self.n10_shape[1:3], [10, 10])

        try:
            layer = tlx.nn.DownSampling2d(scale=(2, 2, 2))
        except Exception as e:
            print(e)


if __name__ == '__main__':

    tlx.logging.set_verbosity(tlx.logging.DEBUG)

    unittest.main()
