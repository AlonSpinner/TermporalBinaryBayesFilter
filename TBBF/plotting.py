import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb, rgb_to_hsv, rgb_to_hsv
from enum import IntEnum

def colorise(gray, hue):
    #to help pick hue
    #https://subscription.packtpub.com/book/data/9781789537147/1/ch01lvl1sec09/object-detection-using-color-in-hsv
    rgb = np.stack((gray,gray,gray),axis = 2)
    hsv = rgb_to_hsv(rgb)
    hsv[:,:,0] = hue
    hsv[:,:,1] = 1 - hsv[:,:,2]
    hsv[:,:,2] = 1
    return hsv_to_rgb(hsv)

class axE(IntEnum):
    Meas= 0
    EstMap = 1
    EstRobot = 2
    World = 3
    Schedule = 4

class plotter:

    def __init__(self, t0 = 0, tf : int =10, n : int = 5) -> None:
        fig, axes = plt.subplots(1,5, sharey = False, sharex = False ,squeeze = False,)
        for row in axes:
            for ax in row:
                ax.set_xticks([])
                ax.set_yticks([])
                ax.spines['top'].set_visible(False)
                # ax.spines['right'].set_visible(False)
                ax.spines['bottom'].set_visible(False)
                # ax.spines['left'].set_visible(False)

        axes[0,axE.Meas].set_title('Measurement')
        axes[0,axE.EstMap].set_title('Est. Map')
        axes[0,axE.EstRobot].set_title('Est. Robot')
        axes[0,axE.World].set_title('World')
        axes[0,axE.Schedule].set_title('Schedule')

        L = tf - t0 + 1
        ticks = list(range(0,2*L,2))
        labels = [f"t = {l+t0}      " for l in range(L)]
        axes[0,axE.Meas].set_yticks(ticks,labels)

        self.axes : list[list[plt.Axes]]= axes
        self.fig : plt.Figure = fig
        self.n : int = n
        self.t0 : int = t0
        self.dt : int = 0
        self.row : int = 0

        #data: -1 == not measured
        self.meas = -np.ones((L*2, n)) 
        self.estMap = -np.ones((L*2, n))
        self.estRobot = -np.ones((L*2, n))
        self.world = -np.ones((L*2, n))
        self.schedule = -np.ones((L*2, n))
        self.robot = -np.ones(L) #-1 where location should not be drawn

    def update(self, t : int ,z : str = None, 
                    estMap : np.ndarray = None, estRobot : np.ndarray = None, 
                    world : np.ndarray = None, robot : np.ndarray = None, 
                    schedule : np.ndarray = None) -> None:
        
        dt = t -self.t0
        row = (dt)*2

        #store for show
        self.dt = dt 
        self.row = row 
        
        if z is not None:
            if z == "⬛":
                self.meas[row,self.n//2] = 1 #occupied
            else: # z == "⬜"
                self.meas[row,self.n//2] = 0 #free
        if estMap is not None:
            self.estMap[row,:] = estMap #black is high probability ~ 0 in image
        if estRobot is not None:
            self.estRobot[row,:] = estRobot
        if world is not None:
            self.world[row,:] =  world
        if schedule is not None:
            self.schedule[row,:] = schedule
        if robot is not None:
            self.robot[dt] = robot
    
    def show(self) -> None:
        self.axes[0,axE.EstMap].imshow(1 - np.maximum(self.estMap,0), cmap ="gray", vmin = 0, vmax = 1)
        self.axes[0,axE.EstRobot].imshow(colorise(1 - np.maximum(self.estRobot,0), hue = 1.0))
        self.axes[0,axE.World].imshow(1 - np.maximum(self.world,0), cmap ="gray", vmin = 0, vmax = 1)
        self.axes[0,axE.Schedule].imshow(1 - np.maximum(self.schedule,0), cmap ="gray", vmin = 0, vmax = 1)

        if self.robot[self.dt] != -1:
            self.axes[0,axE.World].scatter(self.robot[self.dt],self.row, s = 10 ,color = 'r') #actual location of robot

        if self.meas[self.row,self.n//2] == 0:
            highlight_cell(self.axes[0,axE.Meas], self.row, self.n//2, color="black", linewidth=1)
        self.axes[0,axE.Meas].imshow(1 - np.maximum(self.meas,0), cmap ="gray", vmin = 0, vmax = 1)

def highlight_cell(ax, row ,col, **kwargs):
    #https://stackoverflow.com/questions/56654952/how-to-mark-cells-in-matplotlib-pyplot-imshow-drawing-cell-borders
    rect = plt.Rectangle((col-.5, row-.5), 1,1, fill=False, **kwargs)
    ax.add_patch(rect)
    return rect

if __name__ == "__main__":
    p = plotter()
    p.show()
    plt.show()

