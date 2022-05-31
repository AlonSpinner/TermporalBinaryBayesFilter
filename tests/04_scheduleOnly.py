import numpy as np
import matplotlib.pyplot as plt
from TBBF.gaussians import gaussian1D as g1d
from TBBF.plotting import show_gtScheduleMeasurement
n = 5

np.random.seed(1)

schedule = [g1d(3,0.5),
            g1d(4,1),
            g1d(5,0.5),
            g1d(6,1),
            g1d(7,0.2)]
actual = np.array([g.sample() for g in schedule])

t = 4.0

dt = 0.1

actions = [1,1,0,-1,-1,0,-1]
x = 2

for a in actions:
    #move robot
    #sample schedule
    x += a
    s = np.array([g.cdf(t) for g in schedule])
    building = np.array([int(t > ac) for ac in actual])
    show_gtScheduleMeasurement(building,x,s,"⬛",t)
    plt.pause(1)
    t += 1

