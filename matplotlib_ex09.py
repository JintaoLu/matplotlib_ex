#!/usr/bin/env python  
# encoding: utf-8 

""" 
@version: v1.0 
@author: Jinato 
@file: matplotlib_ex09.py 
@time: 2017/12/9 11:14 
"""
import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(.5, 1., n)
Y2 = (1 - X / float(n)) * np.random.uniform(.5, 1., n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y1, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X, Y1):
    plt.text(x + .4, y + .05, '%.2f' % y, ha='center', va='bottom')
for x, y in zip(X, Y2):
    plt.text(x + .4, -y - .05, '-%.2f' % y, ha='center', va='top')
plt.show()