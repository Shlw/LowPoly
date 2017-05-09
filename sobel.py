#-*-coding:utf-8-*-
import Image
import sys
import pprint

inputPNG = sys.argv[1]
outputPNG = sys.argv[2]

im = Image.open(inputPNG)
im = im.convert('L')
pic = im.load()
width = im.size[0]
height = im.size[1]

Gx = [[0]*height for x in xrange(width)]
Gy = [[0]*height for x in xrange(width)]
G  = [[0]*height for x in xrange(width)]

K = 65 #灰度阈值
for x in xrange(1, width-1):
	for y in xrange(1, height-1):
		Gx[x][y] = pic[x+1, y-1] + 2*pic[x+1, y] + pic[x+1, y+1] - \
				   (pic[x-1, y-1] + 2*pic[x-1, y] + pic[x-1, y+1])
		Gy[x][y] = pic[x-1, y-1] + 2*pic[x, y-1] + pic[x+1, y-1] - \
				   (pic[x-1, y+1] + 2*pic[x, y+1] + pic[x+1, y+1])
		G[x][y] = abs(Gx[x][y]) + abs(Gy[x][y])

'''
file = open("L.txt", "w")
for x in xrange(width):
	for y in xrange(height):
		print >> file, G[x][y],
	print >> file, ''
file.close()
'''

newIm = Image.new("L", (width, height))
for x in xrange(width):
	for y in xrange(width):
		if (G[x][y] > K):
			newIm.load()[x, y] = 255
newIm.show()