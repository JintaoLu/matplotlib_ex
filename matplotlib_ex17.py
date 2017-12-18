#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: Jinato
@file: matplotlib_ex17.py
@time: 2017/12/9 12:48
"""
import matplotlib.pyplot as plt
import  numpy as np
from matplotlib import animation

fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

def animat(i):
    line.set_ydata(np.sin(x+i/10))
    return line,

def init():
    line.set_ydata(np.sin(x))
    return line,

ani = animation.FuncAnimation(fig=fig, func=animat, frames=200,
                              init_func=init, interval=20, blit=True)

# # First set up the figure, the axis, and the plot element we want to animate
# fig = plt.figure()
# ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
# line, = ax.plot([], [], lw=2)
#
#
# # initialization function: plot the background of each frame
# def init():
#     line.set_data([], [])
#     return line,
#
#
# # animation function.  This is called sequentially
# # note: i is framenumber
# def animate(i):
#     x = np.linspace(0, 2, 1000)
#     y = np.sin(2 * np.pi * (x - 0.01 * i))
#     line.set_data(x, y)
#     return line,
#
#
# # call the animator.  blit=True means only re-draw the parts that have changed.
# anim = animation.FuncAnimation(fig, animate, init_func=init,
#                                frames=200, interval=20, blit=True)

plt.show()
