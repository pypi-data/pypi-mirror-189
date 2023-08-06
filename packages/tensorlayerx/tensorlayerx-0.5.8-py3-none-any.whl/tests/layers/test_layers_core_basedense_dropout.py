#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorlayerx
import tensorlayerx as tlx

from tests.utils import CustomTestCase


class Layer_Core_Test(CustomTestCase):

    @classmethod
    def setUpClass(self):

        self.batch_size = 8

        self.inputs_shape = [self.batch_size, 784]
        self.input = tlx.nn.Input(self.inputs_shape)
        self.dense1 = tlx.nn.Linear(out_features=800, act=tlx.ReLU, in_features=784, name='test_dense')
        self.n1 = self.dense1(self.input)

        self.dropout1 = tlx.nn.Dropout(p=0.2)
        self.n2 = self.dropout1(self.n1)

        self.dense2 = tlx.nn.Linear(out_features=10, act='relu', b_init=None, in_features=800)
        self.n3 = self.dense2(self.n2)

        self.dense3 = tlx.nn.Linear(out_features=10, act='relu', b_init=None, in_features=10)
        self.n4 = self.dense3(self.n3)

        self.concat = tlx.nn.Concat(concat_dim=-1)([self.n2, self.n3])

        class get_model(tensorlayerx.nn.Module):

            def __init__(self):
                super(get_model, self).__init__()
                self.layer1 = tlx.nn.Linear(out_features=800, act=tlx.ReLU, in_features=784, name='test_dense')
                self.dp = tlx.nn.Dropout(p=0.2)
                self.layer2 = tlx.nn.Linear(out_features=10, act='relu', b_init=None, in_features=800)
                self.layer3 = tlx.nn.Linear(out_features=10, act='relu', b_init=None, in_features=10)

            def forward(self, inputs):
                z = self.layer1(inputs)
                z = self.dp(z)
                z = self.layer2(z)
                z = self.layer3(z)
                return z

        self.net = get_model()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_dense(self):
        self.assertEqual(tlx.get_tensor_shape(self.n1), [self.batch_size, 800])

    def test_dense_nonbias(self):
        self.assertEqual(len(self.dense2.all_weights), 1)

    def test_dropout(self):
        self.assertEqual(len(self.dropout1.all_weights), 0)

    def test_model(self):
        self.assertEqual(len(self.net.all_weights), 4)


if __name__ == '__main__':

    unittest.main()
