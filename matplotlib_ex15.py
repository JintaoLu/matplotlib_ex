#!/usr/bin/env python  
# encoding: utf-8 

""" 
@version: v1.0 
@author: Jinato 
@file: matplotlib_ex15.py 
@time: 2017/12/9 12:23 
"""
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

fig = plt.figure()
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 2, 4, 2, 5, 8, 6]

left, bottom, width, height = .1, .1, .8, .8
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(x, y, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

left, bottom, width, height = .2, .6, .25, .25
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(y, x, 'b')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title inside 1')


plt.axes([.6, .2, .25, .25])
plt.plot(x, y, 'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('title')

plt.show()