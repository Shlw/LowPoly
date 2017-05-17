#-*-coding:utf-8-*-
from PIL import Image
import sys
import random


def SobelEdgeDetection(im):
    im = im.convert('L')
    f = im.load()
    width, height = im.size

    Gx = [[0] * height for x in range(width)]
    Gy = [[0] * height for x in range(width)]
    G = [[0] * height for x in range(width)]

    K = 75  # gray scale threshold
    pt = []  # edge points
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            Gx[x][y] = f[x + 1, y - 1] + 2 * f[x + 1, y] + f[x + 1, y + 1] - \
                (f[x - 1, y - 1] + 2 * f[x - 1, y] + f[x - 1, y + 1])
            Gy[x][y] = f[x - 1, y - 1] + 2 * f[x, y - 1] + f[x + 1, y - 1] - \
                (f[x - 1, y + 1] + 2 * f[x, y + 1] + f[x + 1, y + 1])
            G[x][y] = abs(Gx[x][y]) + abs(Gy[x][y])
            if G[x][y] > K:
                pt += [(x, y)]
    return pt


def SelectVertices(im, cnt):
    pt, ver = SobelEdgeDetection(im), []
    width, height = im.size
    ver += [(0, 0)]
    ver += [(width, 0)]
    ver += [(0, height)]
    ver += [(width, height)]
    ratio = 0.7
    P1 = (cnt * ratio) / len(pt)
    P2 = (cnt * (1 - ratio)) / (width * height)
    for (x, y) in pt:
        if random.random() <= P1:
            ver += [(x, y)]
    for x in range(width):
        for y in range(height):
            if random.random() <= P2:
                ver += [(x, y)]
    return ver


if __name__ == '__main__':
    inputPNG = sys.argv[1]
    im = Image.open(inputPNG)

    newIm = Image.new("L", im.size)
    for (x, y) in SelectVertices(im, 2000):
        newIm.load()[x, y] = 255
    newIm.show()
