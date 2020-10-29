#!/usr/bin/env python3
import requests
import os

home_dir = os.path.expanduser("~")
img_dir = r"{0}/supplier-data/images".format(home_dir)
url = "http://localhost/upload/"

for image in os.listdir(img_dir):
    if image.endswith(".jpeg"):
        image_path = os.path.join(img_dir,image)
        with open(image_path, 'rb') as img_opened:
            r = requests.post(url, files={'file':img_opened})
            print(r.status_code, r.text)