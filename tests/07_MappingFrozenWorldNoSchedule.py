import numpy as np
import matplotlib.pyplot as plt
from TBBF.models import sampleMeasurement, updateCell
from TBBF.gaussians import gaussian1D as g1d
from TBBF.plotting import plotter

np.random.seed(2)

schedule = [g1d(4,1e10)] * 7
history = np.array([[ 5.83242153e-01],
                    [ 2.87466346e+00],
                    [ 1.00000000e+10],
                    [ 5.82013540e+00],
                    [-6.96717793e+00],
                    [ 1.00000000e+10],
                    [ 7.10057628e+00]])

get_world = lambda t: np.array([int(t > h) for h in history])
get_schedule = lambda t: np.array([g.cdf(t) for g in schedule])
bool2str = lambda c: "⬛" if c else "⬜"

t0 = 4
frozenWorld = get_world(t0)
frozenSchedule = get_schedule(t0)
actions = [-1,-1,0,+1,+1,0,+1,+1,+1,+1,-1,-1]
L = len(actions) #number of actions
tf = t0 + L
n = len(schedule) #number of cells
pltr = plotter(t0 = t0, tf = tf, n  = n)


estMap = np.copy(frozenSchedule)
x = 2 #robot location

pltr.update(t0, estMap = estMap, world = frozenWorld, robot = x, schedule = frozenSchedule)
pltr.show()
t = t0
with plt.ion():
    for a in actions:
        t += 1

        #move robot
        x += a

        #sample measurement
        z = sampleMeasurement(bool2str(frozenWorld[x]))
        meas = np.random.rand(n)

        #update estMap
        estMap[x] = updateCell(z, schedule[x], t0, estMap[x])

        #plot
        pltr.update(t, z = z, estMap = estMap, world = frozenWorld, robot = x, schedule = frozenSchedule)
        pltr.show()
        plt.pause(0.5)

plt.show()