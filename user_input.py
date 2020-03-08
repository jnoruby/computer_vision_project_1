#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


# Given numeric input that is not odd integer, round to next odd integer > 1
def next_odd_integer(n):
    if isinstance(n, float):
        n = int(n)
    if n % 2 == 0:
        n += 1
    if n == 1:
        n += 2
    return n

# Get box filter size, either from user or default with bad user input
def get_box_filter_size():
    try:
        box_filter_size = float(input("Set size of box filter (default: 3): "))
        box_filter_size = next_odd_integer(box_filter_size)
    except ValueError:
        box_filter_size = 3
    return int(box_filter_size)

# Get Gaussian sigma from user
def get_gaussian_sigma():
    try:
        gaussian_sigma = float(input("Set size of Gaussian sigma (default: 3): "))
    except ValueError:
        gaussian_sigma = 3
    return int(gaussian_sigma)

# Get a list of three floats between 0 and 1 from user, for noise sigma
def get_sigmas():
    sigmas = []
    for i in range(0, 3):
        print(i)
        input_str = input("Enter floating point value " + str(i + 1) + " (0 < f < 1:)")
        if len(input_str) == 0:
            sigmas.append((i + 1) / 10)
        else:
            sigmas.append(float(input("Enter floating point value " +
                          str(i + 1) + " (0 < f < 1): ")))
    return sigmas

# Return list of 3 empty image files from user-defined sigmas, with file suffix
def generate_image_fds(fd, sigmas, suffix_string):
    fds = []
    for sigma in sigmas:
        sigma_string = "0." + str(int(sigma * 10))
        output_file = fd.replace(".png", sigma_string + suffix_string)
        fds.append(output_file)
    return fds

# Report image min, max values to user
def print_min_max_values(im_str, im):
    print(im_str + ".min() = " + str(im.min()))
    print(im_str + ".max() = " + str(im.max()))
