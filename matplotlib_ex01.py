#!/usr/bin/env python  
# encoding: utf-8 

""" 
@version: v1.0 
@author: Jinato 
@file: matplotlib_ex01.py 
@time: 2017/12/8 20:38 
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
# y = 2 * x + 1
y = x ** 2
plt.plot(x, y)
plt.show()