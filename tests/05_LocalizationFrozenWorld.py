import numpy as np
import matplotlib.pyplot as plt
from TBBF.probalistic_models import sampleMeasurement, forwardSensorScheduleModel, motionModel
from TBBF.random_models import gaussian1D as g1d
from TBBF.plotting import plotter

np.random.seed(4) #seed 4 and seed 2 are interesting

schedule = [g1d(3,0.5),
            g1d(4,1),
            g1d(1e10,1), #build far far in the future
            g1d(5,0.5),
            g1d(2,1),
            g1d(1e10,1), #build far far in the future
            g1d(7,0.2)]
history = np.array([g.sample() for g in schedule]) #when things were built

get_world = lambda t: np.array([int(t > h) for h in history])
get_schedule = lambda t: np.array([g.cdf(t) for g in schedule])
bool2str = lambda c: "⬛" if c else "⬜"

t0 = 4
frozenWorld = get_world(t0)
frozenSchedule = get_schedule(t0)
moves = [-1,-1,+1,+1,+1,+1,+1,+1,-1,-1]
actions = [0] * len(moves)*2
actions[::2] = moves
L = len(actions) #number of actions
tf = t0 + L
n = len(schedule) #number of cells
pltr = plotter(t0 = t0, tf = tf, n  = n)


estRobot = np.ones(n)/n
x = 2 #robot location

pltr.update(t0, estRobot = estRobot, world = frozenWorld, robot = x, schedule = frozenSchedule)
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

        #update estRobot
        estRobotNew = np.zeros(n)
        for ci in range(n):
                pm = 0
                for cj in range(n):
                    pm += motionModel(cj,ci,a) * estRobot[cj]
                estRobotNew[ci] = forwardSensorScheduleModel(z,schedule[ci],t0) * pm
        estRobot = estRobotNew/sum(estRobotNew)

        #plot
        pltr.update(t, z = z, estRobot = estRobot, world = frozenWorld, robot = x, schedule = frozenSchedule)
        pltr.show()
        plt.pause(0.5)

plt.show()