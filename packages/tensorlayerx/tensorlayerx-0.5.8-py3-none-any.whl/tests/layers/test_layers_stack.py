#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorlayerx as tlx
from tensorlayerx.nn import Input, Linear, Stack, UnStack
import tensorlayerx
from tests.utils import CustomTestCase


class Layer_Stack_Test(CustomTestCase):

    @classmethod
    def setUpClass(cls):
        print("-" * 20, "Layer_Stack_Test", "-" * 20)
        cls.batch_size = 4
        cls.inputs_shape = [cls.batch_size, 10]

        cls.ni = Input(cls.inputs_shape, name='input_layer')

        class model(tensorlayerx.nn.Module):

            def __init__(self):
                super(model, self).__init__()
                self.a = Linear(out_features=5)
                self.b = Linear(out_features=5)
                self.stack = Stack(axis=1)

            def forward(self, inputs):
                output1 = self.a(inputs)
                output2 = self.b(inputs)
                output = self.stack([output1, output2])
                return output

        a = Linear(out_features=5)(cls.ni)
        b = Linear(out_features=5)(cls.ni)
        cls.layer1 = Stack(axis=1)
        cls.n1 = cls.layer1([a, b])

        net = model()
        net.set_train()
        cls.inputs = Input(cls.inputs_shape)
        cls.n2 = net(cls.inputs)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_layer_n1(self):
        self.assertEqual(self.n1.shape, (4, 2, 5))

    def test_layer_n2(self):
        self.assertEqual(self.n2.shape, (4, 2, 5))


class Layer_UnStack_Test(CustomTestCase):

    @classmethod
    def setUpClass(cls):
        print("-" * 20, "Layer_UnStack_Test", "-" * 20)
        cls.batch_size = 4
        cls.inputs_shape = [cls.batch_size, 10]

        cls.ni = Input(cls.inputs_shape, name='input_layer')
        a = Linear(out_features=5)(cls.ni)
        cls.layer1 = UnStack(axis=1)
        cls.n1 = cls.layer1(a)

        class model(tensorlayerx.nn.Module):

            def __init__(self):
                super(model, self).__init__()
                self.a = Linear(out_features=5)
                self.unstack = UnStack(axis=1)

            def forward(self, inputs):
                output1 = self.a(inputs)
                output = self.unstack(output1)
                return output

        cls.inputs = Input(cls.inputs_shape)
        net = model()
        net.set_train()
        cls.n2 = net(cls.inputs)

        print(cls.layer1)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_layer_n1(self):
        self.assertEqual(len(self.n1), 5)
        self.assertEqual(self.n1[0].shape, (self.batch_size, ))

    def test_layer_n2(self):
        self.assertEqual(len(self.n2), 5)
        self.assertEqual(self.n1[0].shape, (self.batch_size, ))


if __name__ == '__main__':

    tlx.logging.set_verbosity(tlx.logging.DEBUG)

    unittest.main()
