#!/usr/bin/env python
import os

for size in ['s','m','l','x']:
    os.system(f'wget https://github.com/ultralytics/yolov5/releases/download/v5.0/yolov5{size}.pt')
