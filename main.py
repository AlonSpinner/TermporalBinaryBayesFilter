from .GridFastSlam import GridFastSlam
import numpy as np

schedule = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])
world = np.array([1,2,3,4,5])
grid = GridFastSlam(5,schedule)

t = 3
x_gt = 2
actions = np.array([1,1,0,-1,-1,-1])
measurements = np.array(["⬜","⬜","⬜","⬜","⬜","⬛"])

for i in range(actions):
    #move robot
    x_gt += actions[i]
    
    #update estimator
    grid.moveParticles(actions[i])
    grid.reWeight(measurements[i])
    grid.updateMaps(measurements[i],t)
    #<resample>

    t +=1
