#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import cv2 as cv
import numpy as np
from skimage import color

def create_box_filter(n):
    """ 
    Creates a box filter of size n; reports to console

    :param n: int
    :returns: np.ndarray m * m, where m is next odd integer >= int(n)
    """
    # Enforce odd dimensions on filter, given even input by user
    n = enforce_odd_integer(n)
    # Create box filter g of size (n * n)
    g = np.full((n, n), 1 / (n * n), dtype=float)
    print("Box filter: " + str(g))
    return g

def create_gaussian_filter(sigma):
    """
    Creates a Gaussian filter with user-set sigma; reports to console
    
    :param sigma: int
    :returns: tuple(np.ndarray, int)
    """
    # The size (n * n) of our filter
    n = 2 * math.floor(3 * sigma) + 1
    # Create Gaussian filter g of size n * n
    sum = 0
    g = [[0] * n for i in range(n)]
    for x in range(0, n):
        for y in range(0, n):
            r = math.sqrt(x * x + y * y)
            g[x][y] = math.exp(-(r * r) / sigma) / math.pi * sigma
            sum = sum + g[x][y] 
    print("Gaussian filter: " + str(g))
    print("n = " + str(n))
    return g, n

# a lot like my apply_filter function, but with no builtin functions`
def convolution2D(f, I):
    # Handle boundary of I, e.g. pad I according to size of f 
    pad = calculate_pad(len(f))
    # Compute im_conv = (f * I)
    im_conv = [[0] * len(I[0]) for i in range(len(I))]
    for y in range(pad, len(I) - pad):
        for x in range(pad, len(I[0]) - pad):
            total = 0
            for k in range(0, len(f)):
                for j in range(0, len(f[0])):
                    if x - j < 0:
                        x_out = x + k
                    else:
                        x_out = x - k
                    if y - j < 0:
                        y_out = y + j
                    else:
                        y_out = y - j
                    total = total + f[j][k] * I[y_out][x_out]
            im_conv[y][x] = total
    return im_conv


def median_filtering(I, n):
    # Handle boundary of I, e.g. pad I according to size n
    n = enforce_odd_integer(n)
    pad = calculate_pad(n)
    # Denoise image with an (n * n) median filter
    denoised_im = [[0] * I.shape[0] for i in range(I.shape[1])]
    sliding_window = [0] * n * n
    print(sliding_window)
    edge = math.floor(n / 2)
    for x in range(pad, I.shape[0] - pad - 1):
        for y in range(pad, I.shape[1] - pad - 1):
            total = 0
            for k in range(0, n):
                for j in range(0, n):
                    sliding_window[total] = I[x + k - edge][y + j - edge]
                    total = total + 1
            sliding_window.sort()
            denoised_im[x][y] = sliding_window[n * n // 2]
    return denoised_im 

def enforce_odd_integer(n):
    if n % 2 == 0:
        n = n + 1
    return n

# Scale image intensity values to the range min, max
def scale_image(im, range_min, range_max):
    return (im - im.min()) * ((range_max - range_min) / (im.max() - im.min()) 
            + range_min)

# Add Gaussian noise with mean 0 and std dev sigma
def add_gaussian_noise(im, sigma):
    im_noise = im + (sigma * np.random.randn(*im.shape))
    return im_noise

def apply_filter(im, pad, g):
    """ Returns a numpy array defining an image, filtered either with a box
        filter or a Gaussian filter

    :param im: numpy.ndarray grayscale input image
    :param pad: int padding for applying the filter, either box or Gaussian
    :param g: numpy.ndarray a box filter or a Gaussian filter
    """
    im_height, im_width = im.shape
    im_filtered = im.copy()
    for y in np.arange(pad, im_height - pad):
        for x in np.arange(pad, im_width - pad):
            sliding_window = im[y - pad: y + pad + 1, x - pad:x + pad + 1]
            filtered_pixel = (sliding_window * g).sum()
            im_filtered[y,x] = filtered_pixel
    return im_filtered 

def calculate_pad(box_filter_size):
    """
    Defines padding necessary for a box filter of a given size

    :param box_filter_size: int
    :returns: int
    """
    pad = int((box_filter_size - 1) / 2)
    print("Padding set to " + str(pad))
    return pad

def make_grayscale(fd):
    """
    Reads an image to file and returns grayscale array of file 

    :param fd: string
    :returns: np.ndarray
    """
    im = color.rgb2gray(cv.imread(fd))
    return im

