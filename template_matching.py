#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np
from skimage import color
import image_denoising as denoise


# Used for lab report
from skimage.feature import match_template
from skimage import data


# Import key image for template matching assignment
im = color.rgb2gray(cv.imread("multiplekeys.png"))

# Threshold with a low value so that keys become black
thresh = 0.9
max_value = 1.0
th, binary_image = cv.threshold(im, thresh, max_value, cv.THRESH_BINARY_INV)

# Create 0 - 255 image so it's viewable as png to test threshold
output_im = denoise.scale_image(binary_image, 0, 255)
cv.imwrite("multiplekeys_threshold.png", output_im)
print(output_im)

# Import manually cropped template image and convert to range [-1.0, 1.0]
template_im = cv.imread("keytemplate.png")
template_im = (template_im / 255.0 - 0.5) * 2 

# Implement cross-correlation = Sum x,y of Image1(x,y) * Image2(x,y)
# This is my own attempt to implement, parallel to how median filtering works.
# As of near the due time, it was still running (hopefully correctly)
# at a very slow speed to to really bad asympotic complexity
# So for the lab report I used builtin functions.


# Pad binary image to allow template image to pass at its edge
top = bottom = edge_y = template_im.shape[0]
left = right = edge_x = template_im.shape[1]
padded_binary_im = cv.copyMakeBorder(binary_image, top, bottom, left, right, cv.BORDER_CONSTANT)
# Test pad with an imwrite call
cv.imwrite("padded_binary_keys.png", padded_binary_im * 255)
# Define correlation image
correlation_im = [[0] * padded_binary_im.shape[0] for i in range(padded_binary_im.shape[1])]

# Pass template image over binary image as a sliding window, similar to median filter function
for x in range(edge_x, padded_binary_im.shape[0] - edge_x - 1):
    for y in range(edge_y, padded_binary_im.shape[1] - edge_y - 1):
        pixel_total = 0
        for k in range(0, template_im.shape[0]):
            for j in range(0, template_im.shape[1]):
                pixel_total += template_im[k][j] * padded_binary_im[x][y]
                print(str(x) + " " + str(y) + " " + str(k) + " " + str(j))
        correlation_im[x][y] = pixel_total
correlation_im - denoise.scale_image(binary_image, 0, 255)
cv.imwrite("correlation_image_keys.png", correlation_im * 255)

# Builtin function version for lab report
correlation_im_builtin = match_template(padded_binary_im, template_im)
print(correlation_im_builtin)
