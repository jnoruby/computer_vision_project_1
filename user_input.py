#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os                   # getcwd()
import math

def get_image_path():
    """
    Gets user-defined string argument (allegedly file path); reports to console

    :returns: used-defined string
    """
    fd = input("Enter image file path (default: lena.png): ") or "lena.png"
    print("Image file path set to " + os.getcwd() + "/" + fd)
    return fd

def get_sigmas():
    """
    Gets a list of three floats between 0 and 1 from user; reports to console
    
    :returns: list of three Gaussian noise sigmas
    """
    sigmas = []
    for i in range(0, 3):
        input_str = input("Enter floating point value " + str(i + 1)
                          + " (0 < f < 1:)")
        if len(input_str) == 0:
            sigma = (i + 1) / 10
        else:
            sigma = float(input("Enter floating point value " +
                          str(i + 1) + " (0 < f < 1): "))
        print("adding sigma = " + str(sigma))
        sigmas.append(sigma)
    return sigmas

def get_box_filter_size():
    """
    Gets box filter size from user input (or default); reports to console

    :returns: int
    """
    try:
        box_filter_size = float(input("Set size of box filter (default: 3): "))
        box_filter_size = next_odd_integer(box_filter_size)
    except ValueError:
        box_filter_size = 3
    print("Box filter size set to " + str(box_filter_size))
    return int(box_filter_size)

def get_gaussian_sigma():
    """
    Gets Gaussian sigma from user input (or default); reports to console

    :returns: int
    """
    try:
        gaussian_sig = float(input("Set size of Gaussian sigma (default: 3): "))
    except ValueError:
        gaussian_sig = 3
    print("Gaussian sigma set to " + str(gaussian_sig))
    return int(gaussian_sig)

def get_median_filter_size():
    try:
        median_filter_size = int(input("Set size of median filter: "))
    except:
        median_filter_size = 3
    print("Median filter size set to " + str(median_filter_size))
    return median_filter_size

# Given numeric input that is not odd integer, round to next odd integer > 1
def next_odd_integer(n):
    if isinstance(n, float):
        n = int(n)
    if n % 2 == 0:
        n += 1
    if n == 1:
        n += 2
    return n

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
