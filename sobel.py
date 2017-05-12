#-*-coding:utf-8-*-
from PIL import Image
import sys

def SobelEdgeDetection(im):
	im = im.convert('L')
	f = im.load()
	width = im.size[0]
	height = im.size[1]

	Gx = [[0]*height for x in range(width)]
	Gy = [[0]*height for x in range(width)]
	G  = [[0]*height for x in range(width)]

	K = 75 # 灰度阈值
	pt = [] # 边界点
	for x in range(1, width-1):
		for y in range(1, height-1):
			Gx[x][y] = f[x+1, y-1] + 2*f[x+1, y] + f[x+1, y+1] - \
					   (f[x-1, y-1] + 2*f[x-1, y] + f[x-1, y+1])
			Gy[x][y] = f[x-1, y-1] + 2*f[x, y-1] + f[x+1, y-1] - \
					   (f[x-1, y+1] + 2*f[x, y+1] + f[x+1, y+1])
			G[x][y] = abs(Gx[x][y]) + abs(Gy[x][y])
			if G[x][y] > K:
				pt += [(x, y)]
	return pt

if __name__ == '__main__':
	inputPNG = sys.argv[1]
	im = Image.open(inputPNG)

	newIm = Image.new("L", im.size)
	for (x, y) in SobelEdgeDetection(im):
		newIm.load()[x, y] = 255
	newIm.show()