#!/usr/bin/env python  
# encoding: utf-8 

""" 
@version: v1.0 
@author: Jinato 
@file: matplotlib_ex12.py 
@time: 2017/12/9 11:38 
"""
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)

Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
ax.contour(X, Y, Z, zdir='x', offset=-4, cmap='rainbow')
plt.show()