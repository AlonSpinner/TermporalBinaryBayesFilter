import numpy as np
import matplotlib.pyplot as plt

def logisticCurve(t, gama, sigma):
    y = 1/(1 + np.exp(-sigma*(t-gama)))
    return y

dt = 0.5
t = np.array(np.arange(0,10,dt))
y = logisticCurve(t,5,3)
dydt = np.gradient(y)/dt

fig, axes = plt.subplots(1,2)
axes[0].plot(t,y)
axes[0].set_title('y(t)')
axes[1].plot(t,dydt)
axes[1].set_title('dydt(t)')
plt.show()



