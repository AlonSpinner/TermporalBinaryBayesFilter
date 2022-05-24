import numpy as np
from TBBF.gaussians import gaussian1D as g1d

schedule = [g1d([3,1]),
            g1d([4,1]),
            g1d([5,1]),
            g1d([6,1]),
            g1d([7,1])]
world = [g.sample() for g in schedule]



dt = 0.5
t = np.array(np.arange(0,10,dt))

y = []
for i in range(len(schedule)):
    y.append()
y = logisticCurve(t,5,3)
dydt = np.gradient(y)/dt

fig, axes = plt.subplots(1,2)
axes[0].plot(t,y)
axes[0].set_title('y(t)')
axes[1].plot(t,dydt)
axes[1].set_title('dydt(t)')
plt.show()



