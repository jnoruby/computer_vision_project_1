#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import numpy as np
import cv2 as cv
import image_denoising as denoise

# Load image files and organise in list
lena = cv.imread('lena.png')
cameraman = cv.imread('cameraman.png')
multiplekeys = cv.imread('multiplekeys.png')
images = [('lena.png', lena),
          ('cameraman.png', cameraman),
          ('multiplekeys.png', multiplekeys)]

# Show original images
for image in images:
    cv.imshow(image[0], image[1])
cv.waitKey(0)

# Add Gaussian noise with mean 0 and standard deviation 0.1 to images


# Intialize zeroed out box filter of user-defined size
box_filter_size = int(input("Set size of box filter: "))
g = denoise.create_box_filter(box_filter_size)
print(g)

# Destroy all OpenCV windows
# cv.destroyAllWindows()

