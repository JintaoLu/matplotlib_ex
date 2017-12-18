#!/usr/bin/env python  
# encoding: utf-8 

""" 
@version: v1.0 
@author: Jinato 
@file: matplotlib_ex03.py 
@time: 2017/12/8 20:50 
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure(num=3, figsize=(8, 5))
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1., linestyle='--')
plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('x label')
plt.ylabel('y label')

new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)

plt.yticks([-2, -1.5, -1, 1.7, 2],
           ['$really\ bad$','$bad\ \\alpha$', '$normal$', '$good$', '$really\ good$'])
plt.xticks(new_ticks)
plt.show()