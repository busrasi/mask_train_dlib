#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import glob

import dlib

images = []
bounding_boxes = []
i = 1
options = dlib.simple_object_detector_training_options()

options.add_left_right_image_flips = False
options.C = 4
options.num_threads = 4
options.be_verbose = True


dlib.train_simple_object_detector("/Users/busrasirin/Desktop/my_train_mask/train/xmls/last_imglab.xml", "/Users/busrasirin/Desktop/my_train_mask/train/mask_detect_v2.svm", options)




