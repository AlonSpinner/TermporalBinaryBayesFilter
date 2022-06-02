import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
# f = lambda v,c: np.stack((np.expand_dims(v, axis = 0),)*3,axis=-1) * c
f = lambda v: np.stack((np.expand_dims(v, axis = 0),)*3,axis=-1)

n = 5
schedule = np.random.rand(5)
world = np.random.rand(5)
estimationMap = np.random.rand(5)
estimationRobot = np.random.rand(5)
z = "⬜"
r = [3,0]

fig, axes = plt.subplots(1,5, sharey = False, sharex = True ,squeeze = False,)
for row in axes:
    for ax in row:
        ax.set_xticks([])
        ax.set_yticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

axes[0,0].set_title('Measurement')
axes[0,1].set_title('EstimationMap')
axes[0,2].set_title('EstimationRobot')
axes[0,3].set_title('World')
axes[0,4].set_title('Schedule')

# axes[0,0].set_ylabel('5', rotation=0,labelpad = 30)
axes[0,0].set_yticks(ticks = [0], labels = [' t = 5    '])

meas = np.array([1 if z == "⬜" else 0])
axes[0,0].imshow(f(meas))
axes[0,1].imshow(f(estimationMap))
axes[0,2].imshow(f(estimationRobot))
axes[0,3].imshow(f(world))
axes[0,3].scatter(r[0],r[1], s = 50 ,color = 'r') #actual location of robot
axes[0,4].imshow(f(schedule))
plt.show()