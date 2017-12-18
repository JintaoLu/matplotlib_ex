#!/usr/bin/env python  
# encoding: utf-8 

""" 
@version: v1.0 
@author: Jinato 
@file: matplotlib_ex10.py 
@time: 2017/12/9 11:21 
"""
import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

X, Y = np.meshgrid(x,y)

plt.contour(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)

C = plt.contour(X, Y, f(X, Y), 8, colors='black', lw=.5)
plt.clabel(C, inline=True, fontsize=10)
plt.xticks(())
plt.yticks(())

plt.show()