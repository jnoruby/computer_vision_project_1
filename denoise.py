#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2 as cv
from skimage import color
from skimage import io
import image_denoising as denoise

# Box filter test

# Load user-defined image file and convert to grayscale
fd = input("Please enter path to image file: ")
im = color.rgb2gray(cv.imread(fd))
# Show original image
cv.imshow(fd, im)
cv.waitKey(0)

# Add Gaussian noise with mean 0 and standard deviations to images
sigmas = [0.1, 0.4, 0.7]
for sigma in sigmas:
    im_noise = im + (sigma * np.random.randn(*im.shape))
    # Show noisy images
    cv.imshow("sigma=" + str(sigma) + " " + fd, im_noise)
    cv.waitKey(0)

# Intialize box filter of user-defined size
box_filter_size = int(input("Set size of box filter: "))
g = denoise.create_box_filter(box_filter_size)
print(g)

# Destroy all OpenCV windows
cv.destroyAllWindows()

