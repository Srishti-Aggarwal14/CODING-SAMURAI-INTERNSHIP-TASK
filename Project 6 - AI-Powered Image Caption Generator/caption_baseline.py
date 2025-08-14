#!/usr/bin/env python3
from PIL import Image
import numpy as np
img = Image.open("data/sample.jpg").convert('L')
arr = np.array(img)/255.0
print("Mean brightness",arr.mean())
