#!/usr/bin/env python3

from PIL import Image
import os

# 1. Make a directory to store updated image

source_path = "supplier-data/images"
size = (600,400)

for file in os.listdir(source_path):
    if file.endswith(".tiff"):
        Image.open(os.path.join(source_path, file)).resize(size).convert('RGB').save(os.path.join(source_path, file.split(".")[0]) + ".jpeg", "JPEG")
