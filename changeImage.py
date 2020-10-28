#!/usr/bin/env python3

import os, sys
from PIL import Image

home_dir = os.path.expanduser("~")
img_dir = r"{0}/supplier-data/images/".format(home_dir)
output_dir = r"{0}/supplier-data/images".format(home_dir)
size = (600,400)

# Create Directory if doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process all files in img_dir
for f in os.listdir(img_dir):
    if not f.startswith(".") and "." in f:
        filename = None
        if ".tiff" in f:
            filename = f.replace(".tiff",".jpeg")
        
        if filename:
            outfile = os.path.join(output_dir, filename)

        try:
            img = Image.open(os.path.join(img_dir,f))
            img = img.resize(size)
            img.convert('RGB').save(outfile, "JPEG")
        except OSError:
            print("unable to convert file", f)