import numpy as np
import matplotlib.pyplot as plt
from TBBF.gaussians import gaussian1D as g1d
from TBBF.models import updateMapping, sampleMeasurement, logodds2p, p2logodds
from TBBF.plotting import show_gtScheduleMeasurement
n = 5

np.random.seed(2)

schedule = [g1d(3,0.5),
            g1d(4,1),
            g1d(50,1), #build far far in the future
            g1d(5,0.5),
            g1d(6,1),
            g1d(50,1), #build far far in the future
            g1d(7,0.2)]
history = np.array([g.sample() for g in schedule])


t = 7.0
dt = 1.0
building = ["⬛" if int(t > h) else "⬜" for h in history]
actions = [1,1,0,-1,-1,0,-1]
logodds_estimation = p2logodds(np.array([g.cdf(t) for g in schedule]))
print(logodds_estimation)
x = 2

for a in actions:
    x += a
    
    z = sampleMeasurement(x,building)

    #update mapping
    for i in range(len(logodds_estimation)):
        if x == i:
            logodds_estimation[i] += updateMapping(z, schedule, i, t)
        else:
            logodds_estimation[i] += updateMapping('', schedule, i, t)

    print(logodds_estimation[6])
    #update building state
    building = ["⬛" if int(t > h) else "⬜" for h in history]
    showbuilding = np.array([b == "⬛" for b in building])
    
    #plot
    # s = np.array([g.cdf(t) for g in schedule])
    
    plt.cla()
    show_gtScheduleMeasurement(showbuilding,x,logodds2p(logodds_estimation),z,t)
    plt.pause(1)
    # t += dt

plt.show()
