#!/usr/bin/env python
# -*- coding: utf-8 -*-

def create_box_filter(n):
    # Create box filter g of size (n * n)
    return g

def create_gaussian_filter(sigma):
    # The size (n * n) of our filter
    n = 2 * math.floor(3 * sigma) + 1
    # Create Gaussian filter g of size n * n
    return g

def convolution2D(f, I):
    # Handle boundary of I, e.g. pad I according to size of f 

    # Computer im_conv = (f * I)
    return im_conv

def median_filtering(I, n):
    # Handle boundary of I, e.g. pad I according to size n
    # Denoise image with an (n * n) median filter 
    return denoised_im
