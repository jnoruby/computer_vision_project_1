#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import cv2 as cv
import numpy as np
from skimage import color

# Read an image to file and return grayscale array of file
def make_grayscale(fd):
    im = color.rgb2gray(cv.imread(fd))
    return im

# Define padding necessary for a box filter of a given size
def calculate_pad(box_filter_size):
    return int((box_filter_size - 1) / 2)

# Scale image intensity values to the range min, max
def scale_image(im, range_min, range_max):
    return (im - im.min()) * ((range_max - range_min) / (im.max() - im.min())) + range_min

# Add Gaussian noise with mean 0 and std dev sigma
def add_gaussian_noise(im, sigma):
    im_noise = im + (sigma * np.random.randn(*im.shape))
    return im_noise

# Create a box filter of size n
def create_box_filter(n):
    # Enforce odd dimensions on filter, given even input by user
    if n % 2 == 0:
        n += 1
    # Create box filter g of size (n * n)
    g = np.full((n, n), 1 / (n * n), dtype=float)
    return g

# Apply box filter to an image, return box filtered image
def apply_box_filter(im, pad, g):
    im_height = im.shape[0]
    im_width = im.shape[1]
    im_box_filtered = im.copy()
    for y in np.arange(pad, im_height - pad):
        for x in np.arange(pad, im_width - pad):
            sliding_window = im[y - pad: y + pad + 1, x - pad:x + pad + 1]
            filtered_pixel = (sliding_window * g).sum()
            im_box_filtered[y,x] = filtered_pixel
    return im_box_filtered

def create_gaussian_filter(sigma):
    # The size (n * n) of our filter
    n = 2 * math.floor(3 * sigma) + 1
    # Create Gaussian filter g of size n * n
    g = np.full((n, n), 1 / (n * n), dtype=float)
    return g

def apply_gaussian_filter(im, pad, g):
    im_height = im.shape[0]
    im_width = im.shape[1]
    im_box_filtered = im.copy()
    for y in np.arange(pad, im_height - pad):
        for x in np.arange(pad, im_width - pad):
            sliding_window = im[y - pad: y + pad + 1, x - pad:x + pad + 1]
            filtered_pixel = (sliding_window * g).sum()
            im_box_filtered[y,x] = filtered_pixel
    return im_box_filtered

"""
def convolution2D(f, I):
    # Handle boundary of I, e.g. pad I according to size of f 

    # Computer im_conv = (f * I)
    return im_conv

def median_filtering(I, n):
    # Handle boundary of I, e.g. pad I according to size n
    # Denoise image with an (n * n) median filter 
""    return denoised_im 
"""


