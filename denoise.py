#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os                           # Just for cmd line interface
import cv2 as cv
import image_denoising as denoise
import user_input as ui

borderType = cv.BORDER_CONSTANT

# Get user-defined file handle; report back
fd = input("Enter path to image file (default: lena.png): ") or "lena.png"
print("Image file set to " + os.getcwd() + "/" + fd)

# Get user-defined list of three Gaussian noise levels; report back
sigmas = ui.get_sigmas()

# Get user-defined box filter size, round to nearest odd integer; report back
box_filter_size = ui.get_box_filter_size()
print("Box filter size set to " + str(box_filter_size))
gaussian_sigma = ui.get_gaussian_sigma()
print("Gaussian distance set to " + str(gaussian_sigma))
pad = denoise.calculate_pad(box_filter_size)
print("Padding set to " + str(pad))

# Create grayscale copy of user-defined file using skimage.color.rgb2gray
im = denoise.make_grayscale(fd)
# Intialize box filter at user-defined size
g = denoise.create_box_filter(box_filter_size)
print("Box filter: ")
print(g)
# Initialize gaussian filter at user-defined size
g2 = denoise.create_gaussian_filter(box_filter_size)
print("Gaussian filter: ")
print(g2)

# Create image files for image noising from user-defined sigmas
noised = ui.generate_image_fds(fd, sigmas, ".png")
padded = ui.generate_image_fds(fd, sigmas, "padded.png")
box_filtered = ui.generate_image_fds(fd, sigmas, "box_filtered.png")
gaussian_filtered = ui.generate_image_fds(fd, sigmas, "gaussian_filtered.png")

# Iterate through zipped list of sigmas, to generate noised and padded images
for sigma, fd_noised, fd_padded, fd_boxed, fd_gauss in zip(sigmas, 
                                                           noised, 
                                                           padded,
                                                           box_filtered,
                                                           gaussian_filtered):
    """
    # Add Gaussian noise with mean 0 and std dev sigma
    im_noise = denoise.add_gaussian_noise(im, sigma)
    # Scale image values to range [0, 255]
    im_noise = denoise.scale_image(im_noise, 0, 255) 
    # Pad noised images
    im_padded = cv.copyMakeBorder(im_noise, pad, pad, pad, pad, borderType) 
    # Output noisy images to files
    cv.imwrite(fd_noised, im_noise) 
    # Output padded images to files
    cv.imwrite(fd_padded, im_padded)
    # Create a copy of original image
    im_box_filtered = im_padded.copy()
    # Apply box filter 
    im_box_filtered = denoise.apply_box_filter(im_padded, pad, g)
    # Output box filtered images to files 
    cv.imwrite(fd_boxed, im_box_filtered)
    """

    # Add Gaussian noise with mean 0 and std dev sigma
    im_noise = denoise.add_gaussian_noise(im, sigma)
    # Scale image values to range [0, 255] for output
    im_noise_out = denoise.scale_image(im_noise, 0, 255)  
    # Output noisy images to files
    cv.imwrite(fd_noised, im_noise_out) 
    # Pad noised images
    im_padded = cv.copyMakeBorder(im_noise, pad, pad, pad, pad, borderType)
    # Scale image values to range [0, 255] for output
    im_padded_out = denoise.scale_image(im_padded, 0, 255) 
    # Output padded images to files
    cv.imwrite(fd_padded, im_padded_out)
    # Create a copy of original image
    im_box_filtered = im_padded.copy()
    # Apply box filter 
    im_box_filtered = denoise.apply_box_filter(im_padded, pad, g)
    # Scale image values to range [0, 255] for output
    im_box_filtered_out = denoise.scale_image(im_box_filtered, 0, 255) 
    # Output box filtered images to files 
    cv.imwrite(fd_boxed, im_box_filtered_out)
    # Apply Gaussian filter 
    im_gaussian_filtered = denoise.apply_gaussian_filter(im_padded, pad, g)
    # Scale image values to range [0, 255] for output
    im_gaussian_filtered_out = denoise.scale_image(im_gaussian_filtered, 0, 255) 
    # Output box filtered images to files 
    cv.imwrite(fd_gauss, im_gaussian_filtered_out)
    
    # Report image min, max values to user
    ui.print_min_max_values("im", im)
    ui.print_min_max_values("im_noise", im_noise)
    ui.print_min_max_values("im_padded", im_padded)
    ui.print_min_max_values("im_box_filtered", im_box_filtered)
