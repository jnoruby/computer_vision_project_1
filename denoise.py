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
cv.imshow('original Lena',lena)
cv.imshow('original cameraman', cameraman)
cv.imshow('original multiple keys', multiplekeys)
cv.waitKey(0)

# Destroy all OpenCV windows
cv.destroyAllWindows()

