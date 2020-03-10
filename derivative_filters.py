#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from skimage import color
import image_denoising as denoise
import cv2 as cv

# Make and apply derivative filter
im = color.rgb2gray(cv.imread("cameraman.png"))
derivative_filter = [[-1, 0, 1],[-1, 0, 1],[-1,0,1]]
derivative_im = denoise.convolution2D(derivative_filter, im)
derivative_im = np.array(derivative_im)
derivative_im = denoise.scale_image(derivative_im, 0, 255)
cv.imwrite("derivative_cameraman.png", derivative_im)

# Create binary edge images with various thresholds
median_thresh = (derivative_im.min() + derivative_im.max()) / 2
max_value = 255
min_value = 0
threshold_im_1 = derivative_im.copy()

th, threshold_im_1 = cv.threshold(derivative_im, median_thresh, max_value, cv.THRESH_BINARY)
cv.imwrite("threshold_binary_cameraman_1.png", threshold_im_1)

three_quarters_thresh = (median_thresh + derivative_im.max()) / 2
threshold_im_2 = derivative_im.copy()

th, threshold_im_2 = cv.threshold(derivative_im, three_quarters_thresh, max_value, cv.THRESH_BINARY)
cv.imwrite("threshold_binary_cameraman_2.png", threshold_im_2)

one_quarter_thresh = (median_thresh + derivative_im.min()) / 2
threshold_im_3 = derivative_im.copy()

th, threshold_im_3 = cv.threshold(derivative_im, one_quarter_thresh, max_value, cv.THRESH_BINARY)
cv.imwrite("threshold_binary_cameraman_3.png", threshold_im_3)
