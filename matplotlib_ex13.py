#!/usr/bin/env python  
# encoding: utf-8 

""" 
@version: v1.0 
@author: Jinato 
@file: matplotlib_ex13.py 
@time: 2017/12/9 11:47 
"""
import matplotlib.pyplot as plt

plt.figure()

plt.subplot(2, 2, 1)
plt.plot([0, 1], [0, 1])
plt.subplot(2, 2, 2)
plt.plot([0, 1], [0, 2])
plt.subplot(2, 2, 3)
plt.plot([0, 1], [0, 3])
plt.subplot(2, 2, 4)
plt.plot([0, 1], [0, 4])

plt.figure()

plt.subplot(2, 1, 1)
plt.plot([0, 1], [0, 1])
plt.subplot(2, 3, 4)
plt.plot([0, 1], [0, 2])
plt.subplot(2, 3, 5)
plt.plot([0, 1], [0, 3])
plt.subplot(2, 3, 6)
plt.plot([0, 1], [0, 4])

plt.show()