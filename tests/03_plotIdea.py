import numpy as np
import matplotlib.pyplot as plt
from TBBF.plotting import plotter

np.random.seed(2)
n = 7
tf = 10
t0 = 4

pltr = plotter(t0 = t0, tf = tf, n  = n)

L = tf - t0 + 1
for l in range(L):
    t = t0 + l
    meas = np.random.rand(n)
    estMap = np.random.rand(n)
    estRobot = np.random.rand(n)
    world = np.random.rand(n)
    schedule = np.random.rand(n)
    robot = np.random.randint(0,n-1)
    z = "⬛" if np.random.rand() > 0.5 else "⬜"
    pltr.update(t, z, estMap, estRobot, world, robot, schedule)
    print(t)
    pltr.show()
    plt.pause(0.5)
plt.show()
