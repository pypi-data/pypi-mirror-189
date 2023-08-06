#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorlayerx
import tensorlayerx as tlx
import numpy as np
from tests.utils import CustomTestCase


class Image_Test(CustomTestCase):

    @classmethod
    def setUpClass(self):
        self.input_shape = [100, 100, 3]
        self.input_layer = np.random.randint(0, 255, size = self.input_shape, dtype=np.uint8)

        self.centralcrop_1 = tensorlayerx.vision.transforms.transforms.CentralCrop(central_fraction=0.5)(self.input_layer)
        self.centralcrop_2 = tensorlayerx.vision.transforms.transforms.CentralCrop(size=50)(self.input_layer)

        self.adjustbrightness = tensorlayerx.vision.transforms.transforms.AdjustBrightness(brightness_factor=0.5)(self.input_layer)
        self.adjustconstrast = tensorlayerx.vision.transforms.transforms.AdjustContrast(contrast_factor=0.5)(self.input_layer)
        self.adjusthue = tensorlayerx.vision.transforms.transforms.AdjustHue(hue_factor=0.5)(self.input_layer)
        self.adjustsaturation = tensorlayerx.vision.transforms.transforms.AdjustSaturation(saturation_factor=0.5)(self.input_layer)

        self.crop = tensorlayerx.vision.transforms.transforms.Crop(top=10, left=10, height=80, width=80)(self.input_layer)

        self.fliphorizontal = tensorlayerx.vision.transforms.transforms.FlipHorizontal()(self.input_layer)
        self.flipvertical = tensorlayerx.vision.transforms.transforms.FlipVertical()(self.input_layer)

        self.rgbtogray = tensorlayerx.vision.transforms.transforms.RgbToGray()(self.input_layer)

        self.padtoboundingbox = tensorlayerx.vision.transforms.transforms.PadToBoundingbox(
            top=10, left=10, height=150, width=150, padding_value=0
        )(self.input_layer)

        self.pad_1 = tensorlayerx.vision.transforms.transforms.Pad(padding=10, padding_value=0, mode='constant')(self.input_layer)
        self.pad_2 = tensorlayerx.vision.transforms.transforms.Pad(padding=(10, 10), mode='reflect')(self.input_layer)
        self.pad_3 = tensorlayerx.vision.transforms.transforms.Pad(padding=(10, 20, 30, 40), mode='symmetric')(self.input_layer)

        self.normalize = tensorlayerx.vision.transforms.transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))(self.input_layer)
        self.standardize = tensorlayerx.vision.transforms.transforms.StandardizePerImage()(self.input_layer)

        self.randombrightness = tensorlayerx.vision.transforms.transforms.RandomBrightness(brightness_factor=(0.5, 2))(self.input_layer)
        self.randomcontrast = tensorlayerx.vision.transforms.transforms.RandomContrast(contrast_factor=(0.5, 2))(self.input_layer)
        self.randomhue = tensorlayerx.vision.transforms.transforms.RandomHue(hue_factor=(-0.5, 0.5))(self.input_layer)
        self.randomsaturation = tensorlayerx.vision.transforms.transforms.RandomSaturation(saturation_factor=(0.5, 2))(self.input_layer)

        self.randomcrop_1 = tensorlayerx.vision.transforms.transforms.RandomCrop(
            size=50, padding=10, pad_if_needed=False, fill=0, padding_mode='constant'
        )(self.input_layer)

        self.resize_1 = tensorlayerx.vision.transforms.transforms.Resize(size=46, interpolation='bilinear')(self.input_layer)

        self.rgbtohsv = tensorlayerx.vision.transforms.transforms.RgbToHsv()(self.input_layer)
        self.hsvtorgb = tensorlayerx.vision.transforms.transforms.HsvToRgb()(self.rgbtohsv)
        self.transpose = tensorlayerx.vision.transforms.transforms.Transpose(order=(2, 0, 1))(self.input_layer)
        self.randomrotation = tensorlayerx.vision.transforms.transforms.RandomRotation(
            degrees=30, interpolation='bilinear', expand=False, center=None, fill=0
        )(self.input_layer)
        self.randomshift_1 = tensorlayerx.vision.transforms.transforms.RandomShift(shift=(0.2, 0.2), interpolation='bilinear',
                                                                                   fill=0)(self.input_layer)

        self.randomshear = tensorlayerx.vision.transforms.transforms.RandomShear(shear=30, interpolation='bilinear',
                                                                                 fill=0)(self.input_layer)

        self.randomzoom_1 = tensorlayerx.vision.transforms.transforms.RandomZoom(zoom=(0.2, 0.5), interpolation='bilinear',
                                                                                 fill=0)(self.input_layer)

        self.randomflipvertical = tensorlayerx.vision.transforms.transforms.RandomFlipVertical()(self.input_layer)
        self.randomfliphorizontal = tensorlayerx.vision.transforms.transforms.RandomFlipHorizontal()(self.input_layer)
        self.hwc2chw = tensorlayerx.vision.transforms.transforms.HWC2CHW()(self.input_layer)
        self.chw2hwc = tensorlayerx.vision.transforms.transforms.CHW2HWC()(self.hwc2chw)
        self.randomresizedcrop = tensorlayerx.vision.transforms.transforms.RandomResizedCrop(
            size=(80, 80), scale=(0.08, 1.0), ratio=(3. / 4., 4. / 3.), interpolation='bilinear'
        )(self.input_layer)

        self.randomaffine = tensorlayerx.vision.transforms.transforms.RandomAffine(
            degrees=30, shift=(0.2, 0.2), zoom=(0.2, 0.5), shear=30, interpolation='bilinear', fill=0
        )(self.input_layer)

        self.colorjitter = tensorlayerx.vision.transforms.transforms.ColorJitter(
            brightness=(1, 5), contrast=(1, 5), saturation=(1, 5), hue=(-0.2, 0.2)
        )(self.input_layer)

    @classmethod
    def tearDownClass(self):
        pass

    def test_centralcrop_1(self):

        self.assertEqual(self.centralcrop_1.shape, (50, 50, 3))

    def test_centralcrop_2(self):

        self.assertEqual(self.centralcrop_2.shape, (50, 50, 3))

    def test_hsvtorgb(self):

        self.assertEqual(self.hsvtorgb.shape, (100, 100, 3))

    def test_adjustbrightness(self):

        self.assertEqual(self.adjustbrightness.shape, (100, 100, 3))

    def test_adjustconstrast(self):

        self.assertEqual(self.adjustconstrast.shape, (100, 100, 3))

    def test_adjusthue(self):

        self.assertEqual(self.adjusthue.shape, (100, 100, 3))

    def test_adjustsaturation(self):

        self.assertEqual(self.adjustsaturation.shape, (100, 100, 3))

    def test_crop(self):

        self.assertEqual(self.crop.shape, (80, 80, 3))

    def test_fliphorizontal(self):

        self.assertEqual(self.fliphorizontal.shape, (100, 100, 3))

    def test_flipvertical(self):

        self.assertEqual(self.flipvertical.shape, (100, 100, 3))

    def test_rgbtogray(self):

        self.assertEqual(self.rgbtogray.shape, (100, 100, 1))

    def test_padtoboundingbox(self):

        self.assertEqual(self.padtoboundingbox.shape, (150, 150, 3))

    def test_pad_1(self):

        self.assertEqual(self.pad_1.shape, (120, 120, 3))

    def test_pad_2(self):

        self.assertEqual(self.pad_2.shape, (120, 120, 3))

    def test_pad_3(self):

        self.assertEqual(self.pad_3.shape, (160, 140, 3))

    def test_normalize(self):

        self.assertEqual(self.normalize.shape, (100, 100, 3))

    def test_standardize(self):

        self.assertEqual(self.standardize.shape, (100, 100, 3))

    def test_randomcontrast(self):

        self.assertEqual(self.randomcontrast.shape, (100, 100, 3))

    def test_randomhue(self):

        self.assertEqual(self.randomhue.shape, (100, 100, 3))

    def test_randomsaturation(self):

        self.assertEqual(self.randomsaturation.shape, (100, 100, 3))

    def test_randomcrop_1(self):

        self.assertEqual(self.randomcrop_1.shape, (50, 50, 3))

    def test_resize_1(self):

        self.assertEqual(self.resize_1.shape, (46, 46, 3))

    def test_rgbtohsv(self):

        self.assertEqual(self.rgbtohsv.shape, (100, 100, 3))

    def test_transpose(self):

        self.assertEqual(self.transpose.shape, (3, 100, 100))

    def test_randomrotation(self):

        self.assertEqual(self.randomrotation.shape, (100, 100, 3))

    def test_randomshift_1(self):

        self.assertEqual(self.randomshift_1.shape, (100, 100, 3))

    def test_randoshear(self):

        self.assertEqual(self.randomshear.shape, (100, 100, 3))

    def test_randomzoom_1(self):

        self.assertEqual(self.randomzoom_1.shape, (100, 100, 3))

    def test_randomflipvertical(self):

        self.assertEqual(self.randomflipvertical.shape, (100, 100, 3))

    def test_randomfliphorizontal(self):

        self.assertEqual(self.randomfliphorizontal.shape, (100, 100, 3))

    def test_hwc2chw(self):

        self.assertEqual(self.hwc2chw.shape, (3, 100, 100))

    def test_chw2hwc(self):

        self.assertEqual(self.chw2hwc.shape, (100, 100, 3))

    def test_randomaffine(self):

        self.assertEqual(self.randomaffine.shape, (100, 100, 3))

    def test_colorjitter(self):

        self.assertEqual(self.colorjitter.shape, (100, 100, 3))


if __name__ == '__main__':

    tlx.logging.set_verbosity(tlx.logging.DEBUG)

    unittest.main()
