from scipy.spatial import Delaunay
from matplotlib.colors import ListedColormap
from math import floor, ceil
import numpy as np
import matplotlib.pyplot as plt
from random import random

'''
def GetCrosspoint(tr, y):
    cp = []
    # print(tr)
    for k in range(3):
        pt1, pt2 = tr[k], tr[(k+1) % 3]
        if pt1[1] > pt2[1]:
            pt1, pt2 = pt2, pt1
        if pt1[1] <= y < pt2[1]:
            x = pt1[0] + (y - pt1[1]) / (pt2[1] - pt1[1]) * (pt2[0] - pt1[0])
            cp += [x]
    if len(cp) != 2:
        cp = [0, 0]
    if (cp[0] > cp[1]):
        cp[0], cp[1] = cp[1], cp[0]
    return cp

def ChooseColor(img, tr):
    f = img.convert('L').load()
    inside = [np.sum(tr, axis=0) / 3]
    # print(tr)
    minY = min(pt[1] for pt in tr)
    maxY = max(pt[1] for pt in tr)
    for y in range(minY, maxY):
        x1, x2 = GetCrosspoint(tr, y)
        x1, x2 = floor(x1) + 1, ceil(x2)
        for x in range(x1, x2):
            inside += [(x, y)]
    inside.sort(key = lambda pt: f[pt[0], pt[1]])
    rangeL = floor(0.4 * len(inside))
    rangeR = ceil(0.6 * len(inside))
    R, G, B = 0, 0, 0
    for x, y in inside[rangeL:rangeR]:
        r, g, b = img.getpixel((x, y))
        R, G, B = R + r, G + g, B + b
    R /= (rangeR - rangeL) * 256
    G /= (rangeR - rangeL) * 256
    B /= (rangeR - rangeL) * 256
    return (R, G, B)
'''

def ChooseColor(img, tr):
    f = img.convert('L').load()
    inside = [np.sum(tr, axis=0) / 3]

    pt1, pt2 = tr[1] - tr[0], tr[2] - tr[0]
    area = abs(pt1[0] * pt2[1] - pt1[1] * pt2[0]) / 2
    cnt = int(area * 0.2)
    for run in range(cnt):
        x, y = random(), random()
        if (x + y > 1):
            x, y = 1-x, 1-y
        inside += [tr[0] + pt1*x + pt2*y]
    inside.sort(key=lambda pt: f[pt[0], pt[1]])
    rangeL = floor(0.4 * len(inside))
    rangeR = ceil(0.6 * len(inside))
    R, G, B = 0, 0, 0
    for x, y in inside[rangeL:rangeR]:
        r, g, b = img.getpixel((x, y))
        R, G, B = R + r, G + g, B + b
    R /= (rangeR - rangeL) * 256
    G /= (rangeR - rangeL) * 256
    B /= (rangeR - rangeL) * 256
    return (R, G, B)


import time
def TriAndPaint(img, points, outputIMG):
    print(time.time())
    tri = Delaunay(points)
    print(time.time())
    triList = points[tri.simplices]
    cMap = ListedColormap(
        np.array([ChooseColor(img, tr) for tr in triList]))
    # center = np.sum(points[tri.simplices], axis=1) / 3
    # print(center)
    # cMap = ListedColormap(
    #     np.array([img.getpixel((x, y)) for x, y in center]) / 256)
    color = np.array(range(len(triList)))
    print(time.time())
    # print(color)

    width, height = img.size
    plt.figure(figsize=(width, height), dpi=1)
    plt.tripcolor(points[:, 0], points[:, 1],
                  tri.simplices.copy(), facecolors=color, cmap=cMap)
    # plt.tick_params(labelbottom='off', labelleft='off',
    #                 left='off', right='off', bottom='off', top='off')
    # plt.tight_layout(pad=0)
    plt.axis('off')
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.xlim(0, width)
    plt.ylim(0, height)
    plt.gca().invert_yaxis()
    plt.savefig(outputIMG)
    plt.show()

