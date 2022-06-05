import matplotlib.pyplot as plt
from TBBF.random_models import gaussian1D, gaussian1DT, uniform1D

g = gaussian1D(3,1)
fig, axes = g.plot()
x = g.sample(1000)
axes[1].hist(x, bins = 30, density = True)
fig.suptitle('gaussian1d', fontsize=16)
plt.show()

g = gaussian1DT(5,3,0,10)
fig, axes = g.plot()
x = g.sample(1000)
axes[1].hist(x, bins = 30, density = True)
fig.suptitle('gaussian1DT', fontsize=16)
plt.show()

g = uniform1D(1,3)
fig, axes = g.plot()
x = g.sample(1000)
axes[1].hist(x, bins = 30, density = True)
fig.suptitle('uniform', fontsize=16)
plt.show()

