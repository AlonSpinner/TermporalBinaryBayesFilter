import numpy as np
import matplotlib.pyplot as plt
from TBBF.plotting import plotter


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

# f = lambda v,c: np.stack((np.expand_dims(v, axis = 0),)*3,axis=-1) * c
# n = 5

# x = np.random.rand(n) #robot hypothesied location
# b = np.random.rand(n) #belief of occpuancy from algorithm
# a = np.random.rand(n) #actual state of building
# r = np.array([4,2.2]) #actual location of robot
# m = np.array([4,1.8]) #measurement
# s = np.random.rand(n) #schedule of occpuancy
# t = 5 #time

# xshow = f(x,np.array([0,1,0]))
# bshow = f(b,np.array([0,0,1]))
# sshow = f(s,np.array([0.7,0.5,0]))
# ashow = f(a,np.array([1,0,0]))
# im = np.concatenate((xshow,bshow,ashow,sshow),axis = 0)
# plt.imshow(im)
# plt.scatter(r[0],r[1], s = 50 ,color = 'g') #actual location of robot
# plt.scatter(m[0],m[1], s = 50 ,color = 'w', marker = 's') #actual location of robot
# plt.title(f"t = {t}")
# plt.show()

