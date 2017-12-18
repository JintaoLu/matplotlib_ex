#!/usr/bin/env python  
# encoding: utf-8 

""" 
@version: v1.0 
@author: Jinato 
@file: matplotlib_ex11.py 
@time: 2017/12/9 11:31 
"""
import matplotlib.pyplot as plt
import numpy as np

a = np.array([0.31, 0.37, 0.42,
              0.37, 0.42, 0.52,
              0.42, 0.52, 0.65]).reshape(3, 3)

plt.imshow(a, interpolation='nearest', cmap='bone', origin='upper')
plt.colorbar(shrink=.9)

plt.xticks(())
plt.yticks(())
plt.show()