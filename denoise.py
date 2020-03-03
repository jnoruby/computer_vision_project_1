#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2 as cv
import image_denoising as denoise

# Load image files 
lena = cv.imread('lena.png')
cameraman = cv.imread('cameraman.png')
multiplekeys = cv.imread('multiplekeys.png')

# Show original images
# cv.imshow('original Lena',lena)
# cv.imshow('original cameraman', cameraman)
# cv.imshow('original multiple keys', multiplekeys)
# cv.waitKey(0)

# Intialize zeroed out box filter of user-defined size
box_filter_size = int(input("Set size of box filter: "))
g = denoise.create_box_filter(box_filter_size)
print(g)

# Destroy all OpenCV windows
# cv.destroyAllWindows()

