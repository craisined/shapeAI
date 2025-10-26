import os
import cv2
import numpy as np
import random

IMG_SIZE = 64
NUM_IMAGES = 250  # Number of images per class
OUTPUT_DIR = 'data'

# Ensure folders exist
shapes = ['circle', 'square', 'rectangle', 'triangle']
for shape in shapes:
    os.makedirs(os.path.join(OUTPUT_DIR, shape), exist_ok=True)

def draw_circle():
    img = np.ones((IMG_SIZE, IMG_SIZE), dtype=np.uint8) * 255
    center = (random.randint(8, 56), random.randint(8, 56))
    radius = random.randint(4, min(60 - max(center), min(center)))
    cv2.circle(img, center, radius, (0,), 2)
    return img

def draw_square():
    img = np.ones((IMG_SIZE, IMG_SIZE), dtype=np.uint8) * 255
    start = (random.randint(4, 56), random.randint(4, 56))
    size = random.randint(4, 60 - max(start))
    cv2.rectangle(img, start, (start[0]+size + random.randint(0, 3), start[1]+size + random.randint(0, 3)), (0,), 2)
    return img

def draw_rectangle():
    img = np.ones((IMG_SIZE, IMG_SIZE), dtype=np.uint8) * 255
    vertical = random.randint(0, 1)
    long, short = (random.randint(4, 28), random.randint(33, 56))
    if vertical:
        start = (random.randint(4, 60 - short), random.randint(4, 60 - long))
        width, height = short, long
    else:
        start = (random.randint(4, 60 - long), random.randint(4, 60 - short))
        width, height = long, short
    cv2.rectangle(img, start, (start[0]+width, start[1]+height), (0,), 2)
    return img

def draw_triangle():
    img = np.ones((IMG_SIZE, IMG_SIZE), dtype=np.uint8) * 255
    pt1 = (random.randint(4, 60), random.randint(4, 60))
    pt2 = (random.randint(4, 60), random.randint(4, 60))
    pt3 = (random.randint(4, 60), random.randint(4, 60))
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