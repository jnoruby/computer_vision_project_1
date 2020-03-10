#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2 as cv
from skimage import color
import image_denoising as denoise

# Import key image for template matching assignment
im = color.rgb2gray(cv.imread("multiplekeys.png"))
# Threshold with a low value so that keys become black
thresh = 0.9
max_value = 1.0
th, threshold_im_1 = cv.threshold(im, thresh, max_value, cv.THRESH_BINARY_INV)
# Create 0 - 255 image so it's viewable as png to test threshold
output_im = denoise.scale_image(threshold_im_1, 0, 255)
cv.imwrite("multiplekeys_threshold.png", output_im)
print(output_im)
