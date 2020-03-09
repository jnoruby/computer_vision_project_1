#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2 as cv
import image_denoising as denoise
import user_input as ui

borderType = cv.BORDER_CONSTANT

# Get user-defined file handle; report back
fd = ui.get_image_path()
# Get user-defined list of three Gaussian noise levels; report back
sigmas = ui.get_sigmas()
# Get user-defined box filter size, round to nearest odd integer; report back
box_filter_size = ui.get_box_filter_size()
# Get user-defined Gaussian sigma; report back
gaussian_sigma = ui.get_gaussian_sigma()
# Set pad from box filter; report back
pad_box = denoise.calculate_pad(box_filter_size)
# Create grayscale copy of user-defined file using skimage.color.rgb2gray
im = denoise.make_grayscale(fd)
# Intialize box filter at user-defined size
g = denoise.create_box_filter(box_filter_size)
# Initialize gaussian filter at user-defined size
g2, n = denoise.create_gaussian_filter(gaussian_sigma)
# Set pad from Gaussian filter; report back
pad_gauss = denoise.calculate_pad(n)
# Get user-defined median filter size
median_filter_size = ui.get_median_filter_size()


# Create image files for image noising from user-defined sigmas
noised = ui.generate_image_fds(fd, sigmas, ".png")
padded = ui.generate_image_fds(fd, sigmas, "padded.png")
box_filtered = ui.generate_image_fds(fd, sigmas, "box_filtered.png")
gaussian_filtered = ui.generate_image_fds(fd, sigmas, "gaussian_filtered.png")
median_filtered = ui.generate_image_fds(fd, sigmas, "median_filtered.png")

# Iterate through zipped list of sigmas, to generate noised and padded images
for sigma, fd_noised, fd_padded, fd_boxed, fd_gauss, fd_median in zip(sigmas, 
                                                                      noised, 
                                                                      padded,
                                                                      box_filtered,
                                                                      gaussian_filtered,
                                                                      median_filtered):

    # Add Gaussian noise with mean 0 and std dev sigma
    im_noise = denoise.add_gaussian_noise(im, sigma)
    # Scale image values to range [0, 255] for output
    im_noise_out = denoise.scale_image(im_noise, 0, 255)  
    # Output noisy images to files
    cv.imwrite(fd_noised, im_noise_out) 
    # Pad noised images for box filter
    im_padded = cv.copyMakeBorder(im_noise, pad_box, pad_box, pad_box,
                                  pad_box, borderType)
    # Scale image values to range [0, 255] for output
    im_padded_out = denoise.scale_image(im_padded, 0, 255) 
    # Output padded images to files
    cv.imwrite(fd_padded, im_padded_out)
    # Create a copy of original image
    im_box_filtered = im_padded.copy()
    # Apply box filter 
    im_box_filtered = denoise.apply_filter(im_padded, pad_box, g)
    # Scale image values to range [0, 255] for output
    im_box_filtered_out = denoise.scale_image(im_box_filtered, 0, 255) 
    # Output box filtered images to files 
    cv.imwrite(fd_boxed, im_box_filtered_out)
    
    # Pad noised images for Gaussian filter
    im_padded = cv.copyMakeBorder(im_noise, pad_gauss, pad_gauss, pad_gauss,
                                  pad_gauss, borderType)
    # Apply Gaussian filter 
    im_gaussian_filtered = denoise.apply_filter(im_padded, pad_gauss, g2)
    # Scale image values to range [0, 255] for output
    im_gaussian_filtered_out = denoise.scale_image(im_gaussian_filtered, 0, 255) 
    # Output box filtered images to files 
    cv.imwrite(fd_gauss, im_gaussian_filtered_out)

    # Apply median filter
    im_median_filtered = denoise.median_filtering(im_padded, median_filter_size)
    im_median_filtered = np.array(im_median_filtered)
    im_median_filtered = denoise.scale_image(im_median_filtered, 0, 255)
    cv.imwrite(fd_median, im_median_filtered)
    
    # Report image min, max values to user
    ui.print_min_max_values("im", im)
    ui.print_min_max_values("im_noise", im_noise)
    ui.print_min_max_values("im_padded", im_padded)
    ui.print_min_max_values("im_box_filtered", im_box_filtered)

# Test convolution
f = [[-2, -1, 0],[-1, 1, 1],[0, 1, 2]]
convolved_image = denoise.convolution2D(f, im)
convolved_image = np.array(convolved_image)
convolved_image = denoise.scale_image(convolved_image, 0, 255)
cv.imwrite("convolved_lena.png", convolved_image)
#median_filtered_image = denoise.median_filtering(im, 10)
#median_filtered_image = np.array(median_filtered_image)
#median_filtered_image = denoise.scale_image(median_filtered_image, 0, 255)
#cv.imwrite("median_filtered_lena.png", median_filtered_image)
