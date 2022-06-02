import numpy as np
import matplotlib.pyplot as plt
from enum import IntEnum

fc = lambda v,c: np.stack((np.expand_dims(v, axis = 0),)*3,axis=-1) * c
f = lambda v: np.stack((np.expand_dims(v, axis = 0))*3,axis=-1)

def show_gtScheduleMeasurement(actual : np.ndarray, robot : float, schedule : np.ndarray, measurement : str ,time : float):
    ashow = f(actual,np.array([1,0,0]))
    sshow = f(schedule,np.array([0.7,0.5,0]))
    rshow = np.array([robot,0])
    im = np.concatenate((ashow,sshow),axis = 0)
    if measurement == "⬛":
        z = "occ"
    else:
        z = "free"
    plt.imshow(im)
    plt.scatter(rshow[0],rshow[1], s = 50 ,color = 'g') #actual location of robot
    plt.title(f"t = {time}      z = {z}")


class axE(IntEnum):
    Meas= 0
    EstMap = 1
    EstRobot = 2
    World = 3
    Schedule = 4

class plotter:

    def __init__(self, t0 = 0, tf : int =10, n : int = 5) -> None:
        fig, axes = plt.subplots(1,5, sharey = False, sharex = True ,squeeze = False,)
        for row in axes:
            for ax in row:
                ax.set_xticks([])
                ax.set_yticks([])
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                ax.spines['bottom'].set_visible(False)
                ax.spines['left'].set_visible(False)

        axes[0,axE.Meas].set_title('Measurement')
        axes[0,axE.EstMap].set_title('Est. Map')
        axes[0,axE.EstRobot].set_title('Est. Robot')
        axes[0,axE.World].set_title('World')
        axes[0,axE.Schedule].set_title('Schedule')

        L = tf - t0 + 1
        ticks = list(range(0,2*L,2))
        labels = [f"t = {l+t0}      " for l in range(L)]
        axes[0,axE.Meas].set_yticks(ticks,labels)

        self.axes = axes
        self.fig = fig
        self.n = n
        self.t = t0

        #data
        self.meas = np.ones((L*2, n))
        self.estMap = np.ones((L*2, n))
        self.estRobot = np.ones((L*2, n))
        self.world = np.ones((L*2, n))
        self.schedule = np.ones((L*2, n))
        self.robot = -np.ones(L) #-1 where location is not decided

    def update(self, t : int ,z : str = None, 
                    estMap : np.ndarray = None, estRobot : np.ndarray = None, 
                    world : np.ndarray = None, robot : np.ndarray = None, 
                    schedule : np.ndarray = None):
        
        self.t = t
        
        if z:
            self.meas[t,self.n//2] = 1.0
        else:
            self.meas[t,self.n//2] = 0.5
        if estMap:
            self.estMap[t,:] = estMap
        if estRobot:
            self.estRobot[t,:] = estRobot
        if world:
            self.world[t,:] = world
        if schedule:
            self.schedule[t,:] = schedule
        if robot:
            self.robot[t] = robot
    
    def show(self):
        self.axes[0,axE.Meas].imshow(self.meas, cmap ="gray", vmin = 0, vmax = 1)
        self.axes[0,axE.EstMap].imshow(self.estMap, cmap ="gray", vmin = 0, vmax = 1)
        self.axes[0,axE.EstRobot].imshow(self.estRobot, cmap ="gray", vmin = 0, vmax = 1)
        self.axes[0,axE.World].imshow(self.world, cmap ="gray", vmin = 0, vmax = 1)
        self.axes[0,axE.Schedule].imshow(self.schedule, cmap ="gray", vmin = 0, vmax = 1)

        if self.robot[self.t] > 0:
            self.axes[0,axE.World].scatter(self.robot[self.t],self.t * 2, s = 50 ,color = 'r') #actual location of robot

if __name__ == "__main__":
    p = plotter()
    p.show()
    plt.show()

