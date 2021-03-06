import numpy as np
import matplotlib.pyplot as plt
from TBBF.random_models import gaussian1D as g1d, dead1D
from TBBF.plotting import plotter

schedule = [g1d(3,0.5),
            g1d(4,1),
            dead1D(), #build far far in the future
            g1d(5,0.5),
            g1d(6,1),
            dead1D(), #build far far in the future
            g1d(7,0.2)]
history = np.array([g.sample() for g in schedule]) #when things were built

get_world = lambda t: np.array([int(t > h) for h in history])

get_schedule = lambda t: np.array([g.cdf(t) for g in schedule])

n = len(schedule) #number of cells
L = 7 #number of actions
t0 = 4
tf = t0 + L
pltr = plotter(t0 = t0, tf = tf, n  = n)


actions = [1,1,0,-1,-1,0,-1]
measurements = ["⬛","⬜","⬛","⬜","⬜","⬛","⬜"]
x = 2

pltr.update(t0, world = get_world(t0), robot = x, schedule = get_schedule(t0))
pltr.show()
t = t0
for a,z in zip(actions,measurements):
    t += 1

    x += a
    
    pltr.update(t, z,  world = get_world(t), robot = x, schedule = get_schedule(t))
    pltr.show()
    plt.pause(0.5)

plt.show()
