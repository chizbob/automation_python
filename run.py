#! /usr/bin/env python3

import os
import requests

source_path = "supplier-data/descriptions"
image_path = "images"
fruit = {}

for file in os.listdir(source_path):
    with open(os.path.join(source_path, file)) as f:
        desc = f.read().splitlines() #list
        for i in range(0, len(desc)):
            fruit["name"] = desc[0]
            fruit["weight"] = int(desc[1].split(" ")[0])
            fruit["description"] = desc[2]
            fruit["image_name"] = os.path.join(source_path, image_path, file.split(".")[0] + ".jpg")

    res = requests.post("http://127.0.0.1:80/fruits/", json=fruit)
