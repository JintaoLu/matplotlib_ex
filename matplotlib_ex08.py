#!/usr/bin/env python  
# encoding: utf-8 

""" 
@version: v1.0 
@author: Jinato 
@file: matplotlib_ex08.py 
@time: 2017/12/9 10:58 
"""
import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)

plt.scatter(X, Y, s=75, c=T, alpha=.5)

plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)

plt.xticks(())
plt.yticks(())
plt.show()