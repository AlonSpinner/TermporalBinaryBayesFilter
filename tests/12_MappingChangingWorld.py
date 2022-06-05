import numpy as np
import matplotlib.pyplot as plt
from TBBF.probalistic_models import sampleMeasurement, updateCellDynamicWorld
from TBBF.random_models import gaussian1D as g1d
from TBBF.plotting import plotter

np.random.seed(2)

schedule = [g1d(3,0.5),
            g1d(8,2),
            g1d(1e10,1), #build far far in the future
            g1d(12,2),
            g1d(1e10,5),
            g1d(1e10,1), #build far far in the future
            g1d(12,3)]
history = np.array([g.sample() for g in schedule]) #when things were built
# history[4] = 1.0 #error in schedule

get_world = lambda t: np.array([int(t > h) for h in history])
get_schedule = lambda t: np.array([g.cdf(t) for g in schedule])
bool2str = lambda c: "⬛" if c else "⬜"

t0 = 4
actions = [-1,-1,0,+1,+1,0,+1,+1,0,0,0,0,-1,-1,-1,-1,1]
L = len(actions) #number of actions
tf = t0 + L
n = len(schedule) #number of cells
pltr = plotter(t0 = t0, tf = tf, n  = n)


estMap = np.copy(get_schedule(t0))
x = 2 #robot location

pltr.update(t0, estMap = estMap, world = get_world(t0), robot = x, schedule = get_schedule(t0))
pltr.show()
t = t0
with plt.ion():
    for a in actions:
        t += 1

        #move robot
        x += a

        #sample measurement
        z = sampleMeasurement(bool2str(get_world(t)[x]))
        meas = np.random.rand(n)

        #update estMap
        for c in range(n):
            if t == 16 and c == 4:
                test = 0
            estMap[c] = updateCellDynamicWorld(z, schedule[c], t, estMap[c], gama = float(c == x))

        #plot
        pltr.update(t, z = z, estMap = estMap, world = get_world(t), robot = x, schedule = get_schedule(t))
        pltr.show()
        plt.pause(0.5)

plt.show()