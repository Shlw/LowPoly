import sys
from sobel import SelectVertices
from triangulate import TriAndPaint
from PIL import Image
import numpy as np

inputIMG = sys.argv[1]
outputIMG = sys.argv[2]
img = Image.open(inputIMG)
points = np.array(SelectVertices(img, 2000))
TriAndPaint(img, points, outputIMG)
