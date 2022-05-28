#!/usr/bin/env python3
import requests

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
source_path = "supplier-data/images"

for file in os.listdir(source_path):
    if not file.endswith(".DS_Store"):
        with open(file, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
