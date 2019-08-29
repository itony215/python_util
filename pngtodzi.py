#!/usr/bin/env python
# -*- coding: utf-8 -*-

import deepzoom
import os,glob

dicom_png_path = '../raw_images'

for dirPath, dirNames, fileNames in os.walk(dicom_png_path):
    print("dirPath: {}".format(dirPath))
    print("dirNames: {}".format(dirNames))
    print("fileNames: {}".format(fileNames))

    for f in fileNames:
        if f.endswith('.png'):
            print "filePath = ", os.path.join(dirPath, f)
            print "fileName = ", f

            SOURCE = os.path.relpath(os.path.join(dirPath, f), './')

            creator = deepzoom.ImageCreator(tile_size=256, tile_overlap=2, tile_format="png",
                                image_quality=1, resize_filter="bicubic")

            name, ext = os.path.splitext(f)

            creator.create(SOURCE, "{}.dzi".format(name))

