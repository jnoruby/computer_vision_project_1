#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from skimage import color
import image_denoising as denoise
import cv2 as cv

im = color.rgb2gray(cv.imread("cameraman.png"))
derivative_filter = [[-1, 0, 1],[-1, 0, 1],[-1,0,1]]
derivative_im = denoise.convolution2D(derivative_filter, im)
derivative_im = np.array(derivative_im)
derivative_im = denoise.scale_image(derivative_im, 0, 255)
cv.imwrite("derivative_cameraman.png", derivative_im)
