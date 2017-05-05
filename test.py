import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

h = 300
w = 1000
npts = 500
pts = np.zeros((npts,2))
pts[:,0] = np.random.randint(0,w,npts)
pts[:,1] = np.random.randint(0,h,npts)
tri = Delaunay(pts)
plt.xlim(0, w)
plt.ylim(0, h)
centers = np.sum(pts[tri.simplices], axis=1, dtype='int')/3.0
colors = np.array([ (x-w/2.)**2 + (y-h/2.)**2 for x,y in centers])
plt.tripcolor(pts[:,0], pts[:,1], tri.simplices.copy(), facecolors=colors, edgecolors='k')
plt.gca().set_aspect('equal')
plt.show()
