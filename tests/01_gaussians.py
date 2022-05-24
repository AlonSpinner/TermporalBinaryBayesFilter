import numpy as np
import matplotlib.pyplot as plt

from TBBF.gaussians import gaussian1D

g = gaussian1D(3,1)

dt = 0.5
t = np.array(np.arange(0,10,dt))
dydt = g.pdf(t)
y = g.cdf(t)

fig, axes = plt.subplots(1,2)
axes[0].plot(t,y)
axes[0].set_title('y(t)')
axes[1].plot(t,dydt)
axes[1].set_title('dydt(t)')
plt.show()



