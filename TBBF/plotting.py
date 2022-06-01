import numpy as np
import matplotlib.pyplot as plt

f = lambda v,c: np.stack((np.expand_dims(v, axis = 0),)*3,axis=-1) * c

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

