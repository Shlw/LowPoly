import sys
from sobel import SelectVertices
from triangulate import TriAndPaint
from PIL import Image
import numpy as np

inputIMG = sys.argv[1]
outputIMG = sys.argv[2]
img = Image.open(inputIMG)
if len(sys.argv) == 4:
    num = int (sys.argv[3])
else:
    num = 2000
points = np.array(SelectVertices(img, num))
TriAndPaint(img, points, outputIMG)
