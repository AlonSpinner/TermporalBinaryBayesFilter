from .gaussians import gaussian1D as g1d
import numpy as np
from typing import Union,Callable
EPS = 1e-15

def motionModel(source,dest,a_mu,a_sigma = 0.2):
    g = g1d(source + a_mu,a_sigma)
    return  g.pdf(dest)
    
def forwardSensorModel(z : str, m : str) -> float:
    '''
    z - meaurement "⬜" or "⬛"
    S - schedule of building
    x - location of cell
    t - world time
    
    returns probablity of achieving measurement z
    '''
    if m == "⬛":
        if z == "⬜":
            return 0.1
        elif z == "⬛":
            return 0.9

    elif m == "⬜":
        if z == "⬜":
            return 0.85
        elif z == "⬛":
            return 0.15

def scheduleModel(s : g1d, t : float , m : str = "⬛") -> float:
    '''
    S - schedule of cell
    t - world time
    
    returns probablity of m given schedule
    '''
    if m == "⬛":
            return s.cdf(t)
    elif m == "⬜":
            return 1 - s.cdf(t)
    else:
        raise Exception("m is not ⬜ or ⬛")


def sampleMeasurement(m : str) -> str:
    '''
    m:  "⬜" or "⬛"
    
    returns measurement z
    '''

    p = np.random.rand()
    
    if m == "⬛": #occupied
        if p < forwardSensorModel(z = "⬛", m = "⬛"):
            return "⬛"
        else:
            return "⬜"

    if m == "⬜": #free
        if p < forwardSensorModel(z = "⬜", m = "⬜"):
            return "⬜"
        else:
            return "⬛"

def forwardSensorScheduleModel(z : str, s : g1d, t):
    '''
    s - schedule of cell
    t - world time
    z - measurement

    returns probablity of obtaining measurement
    '''
    return forwardSensorModel(z, m = "⬜") * scheduleModel(s, t , m = "⬜") + \
                forwardSensorModel(z, m = "⬛") * scheduleModel(s, t , m = "⬛")

def inverseSensorScheduleModel(z : str, s : g1d, t : float, m = "⬛") -> float:
    '''
    z - meaurement "⬜" or "⬛"
    s - schedule of cell
    t - world time
    
    returns probablity of m
    '''
    num = forwardSensorModel(z, m) * scheduleModel(s, t , m)
    denum = forwardSensorScheduleModel(z, s, t)
    return num/denum

def updateCell(z : str, s : g1d, t : float, pkm1: float, gama = 1) -> float:
    '''
    z - meaurement "⬜" or "⬛"
    s - schedule of cell
    t - world time
    pkm1 - probability of cell being occupied before measuring
    gama - probability of measuring cell ~ probability of being infront of cell
    
    returns updated probablity of cell being occupied
    '''

    psg = binaryStateMeasurementModelEnhancer_Explicit(scheduleModel(s, t), gama)
    pzg =  binaryStateMeasurementModelEnhancer_Explicit(inverseSensorScheduleModel(z, s, t) , gama)
    odds =  (pzg/(1-pzg+EPS)) * pkm1/(1-pkm1+EPS) * ((1-psg)/(psg+EPS))
    return odds2p(odds)

def updateCellDynamicWorld(z : str, s : g1d, t : float, gama = 1) -> float:
    ps = scheduleModel(s, t)
    psg = binaryStateMeasurementModelEnhancer_Explicit(scheduleModel(s, t), gama)
    pzg =  binaryStateMeasurementModelEnhancer_Explicit(inverseSensorScheduleModel(z, s, t) , gama)
    odds = (pzg/(1-pzg+EPS)) * ((1-psg)/(psg+EPS)) *  (1+ps)/(1-ps+EPS)
    return odds2p(odds)

def binaryStateMeasurementModelEnhancer_Explicit(pz : float, gama : Union[float,np.ndarray])-> Union[float,np.ndarray]:
    '''
    pz - probability of measurement z occuring given that we measure the thing [0,1]
    gama - probability of measuring the correct thing [0,1]
    
    assumption: z measures a binary state
    see test 09
    '''
    return (0.5**(1-gama) * pz**gama) * (2**(1-gama) / (pz**gama + (1-pz)**gama))

def binaryStateMeasurementModelEnhancer_Implicit(measurementModel : Callable)-> Callable:
    '''
    measurementModel - measurement model of a binary state
    gama - probability of measuring the correct thing [0,1]
    
    see test 09
    '''
    def enhancedModel(z, m, gama):
        pz = measurementModel(z, m)
        return (0.5**(1-gama) * pz**gama) * (2**(1-gama) / (pz**gama + (1-pz)**gama))
    return enhancedModel

def p2logodds(p) -> Union[float,np.ndarray]:
    return np.log(p / (1 - p + EPS))

def logodds2p(l) -> Union[float,np.ndarray]:
    return  np.exp(l) / (1 + np.exp(l))

def odds2p(odds):
    return odds / (1 + odds)