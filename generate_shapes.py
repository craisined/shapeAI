#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  3 19:21:23 2025

@author: quentingeoffroy
"""

import os
import cv2
import numpy as np
import random

IMG_SIZE = 64
NUM_IMAGES = 100  # Number of images per class
OUTPUT_DIR = 'data/train'

# Ensure folders exist
shapes = ['circle', 'square', 'rectangle', 'triangle']
for shape in shapes:
    os.makedirs(os.path.join(OUTPUT_DIR, shape), exist_ok=True)

def draw_circle():
    img = np.ones((IMG_SIZE, IMG_SIZE), dtype=np.uint8) * 255
    center = (random.randint(20, 44), random.randint(20, 44))
    radius = random.randint(10, 20)
    cv2.circle(img, center, radius, (0,), 2)
    return img

def draw_square():
    img = np.ones((IMG_SIZE, IMG_SIZE), dtype=np.uint8) * 255
    start = (random.randint(10, 30), random.randint(10, 30))
    size = random.randint(20, 30)
    cv2.rectangle(img, start, (start[0]+size, start[1]+size), (0,), 2)
    return img

def draw_rectangle():
    img = np.ones((IMG_SIZE, IMG_SIZE), dtype=np.uint8) * 255
    start = (random.randint(5, 25), random.randint(10, 30))
    width = random.randint(25, 35)
    height = random.randint(15, 25)
    cv2.rectangle(img, start, (start[0]+width, start[1]+height), (0,), 2)
    return img

def draw_triangle():
    img = np.ones((IMG_SIZE, IMG_SIZE), dtype=np.uint8) * 255
    pt1 = (random.randint(10, 54), random.randint(10, 30))
    pt2 = (pt1[0] + random.randint(-15, 15), pt1[1] + random.randint(20, 30))
    pt3 = (pt1[0] + random.randint(15, 25), pt1[1] + random.randint(20, 30))
    points = np.array([pt1, pt2, pt3])
    cv2.drawContours(img, [points], 0, (0,), 2)
    return img

draw_functions = {
    'circle': draw_circle,
    'square': draw_square,
    'rectangle': draw_rectangle,
    'triangle': draw_triangle
}

# ----- Generate images -----
for shape in shapes:
    for i in range(NUM_IMAGES):
        img = draw_functions[shape]()
        filename = os.path.join(OUTPUT_DIR, shape, f"{shape}_{i}.png")
        cv2.imwrite(filename, img)

print("Images generated successfully!")
