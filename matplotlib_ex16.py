#!/usr/bin/env python  
# encoding: utf-8 

""" 
@version: v1.0 
@author: Jinato 
@file: matplotlib_ex16.py 
@time: 2017/12/9 12:44 
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 19, 0.1)
y1 = .05 * x ** 2
y2 = -1 * y1

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(x, y1, 'r')
ax2.plot(x, y2, 'g--')

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1 data', color='r')
ax2.set_ylabel('Y2 data', color='g')




plt.show()