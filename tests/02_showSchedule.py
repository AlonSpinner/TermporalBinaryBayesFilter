import numpy as np
from TBBF.gaussians import gaussian1D as g1d
import matplotlib.pyplot as plt

schedule = [g1d(3,0.5),
            g1d(4,1),
            g1d(5,0.5),
            g1d(6,1),
            g1d(7,0.2)]
world = [g.sample() for g in schedule]



dt = 0.1
t = np.array(np.arange(0,10,dt))

cdf = []
pdf = []
for g in schedule:
    cdf.append(g.cdf(t))
    pdf.append(g.pdf(t))

# dydt = np.gradient(y)/dt

fig, axes = plt.subplots(2,1)

for c,p in zip(cdf,pdf):
    axes[0].plot(t,c)
    axes[1].plot(t,p)

axes[0].set_title('y(t)')
axes[1].set_title('dydt(t)')    
plt.show()



