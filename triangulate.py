from scipy.spatial import Delaunay
from matplotlib.colors import ListedColormap
import numpy as np
import matplotlib.pyplot as plt


def TriAndPaint(img, points, outputIMG):
    tri = Delaunay(points)
    center = np.sum(points[tri.simplices], axis=1) / 3
    # print(center)
    cMap = ListedColormap(
        np.array([img.getpixel((x, y)) for x, y in center]) / 256)
    color = np.array(range(len(center)))
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
