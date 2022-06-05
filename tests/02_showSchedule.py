import numpy as np
from TBBF.random_models import gaussian1D as g1d
import matplotlib.pyplot as plt

np.random.seed(1)

schedule = [g1d(3,0.5),
            g1d(4,1),
            g1d(5,0.5),
            g1d(6,1),
            g1d(7,0.2)]
world = np.array([g.sample() for g in schedule])

dt = 0.1
t = np.array(np.arange(0,10,dt))

cdf = []
pdf = []
for g in schedule:
    cdf.append(g.cdf(t))
    pdf.append(g.pdf(t))

fig, axes = plt.subplots(2,1)

for c,p in zip(cdf,pdf):
    axes[0].plot(t,c)
    axes[1].plot(t,p)
for w in world:
    axes[1].scatter(w,0.5)
axes[0].set_title('cdf')
axes[1].set_title('pdf')  
plt.show()



