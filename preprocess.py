#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  3 19:16:52 2025

@author: quentingeoffroy
"""
from PIL import Image, ImageOps
import numpy as np

def preprocess_image(image_path):
    # Load image in grayscale
    image = Image.open(image_path).convert('L')

    # Invert colors: white background becomes black, drawing becomes white
    image = ImageOps.invert(image)

    # Resize to 64x64
    image = image.resize((64, 64))

    # Convert to numpy array
    img_array = np.array(image)

    # Normalize to 0-1
    img_array = img_array / 255.0

    # Add batch and channel dimensions for CNN input
    img_array = img_array.reshape(1, 64, 64, 1)

    return img_array

if __name__ == "__main__":
    processed = preprocess_image("data/drawing.png")
    print("Preprocessed image shape:", processed.shape)


