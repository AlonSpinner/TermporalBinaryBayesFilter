from .gaussians import gaussian1D as g1d
import numpy as np
EPS = 1e-15

def inverseSensorScheduleModel(z : str, S : g1d, x : int, t : float, m = "⬛") -> float:
    '''
    z - meaurement "⬜" or "⬛"
    S - schedule of building
    x - location of cell
    t - world time
    
    returns probablity of m
    '''
    num = forwardSensorModel(z, m) * scheduleModel(S, x, t , m)
    denum = forwardSensorModel(z, m = "⬜") * scheduleModel(S, x, t , m = "⬜") + \
                forwardSensorModel(z, m = "⬛") * scheduleModel(S, x, t , m = "⬛")
    return num/denum

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
            return 0.05
        elif z == "⬛":
            return 0.95

    elif m == "⬜":
        if z == "⬜":
            return 0.9
        elif z == "⬛":
            return 0.1
    
def scheduleModel(S : list[g1d], x : int, t : float , m : str = "⬛") -> float:
    '''
    S - schedule of building
    x - location of cell
    t - world time
    
    returns probablity of m given schedule
    '''
    s = S[x]
    if m == "⬛":
            return s.cdf(t)
    elif m == "⬜":
            return 1 - s.cdf(t)
    else:
        raise Exception("m is not ⬜ or ⬛")

def sampleMeasurement(x : int, buildingState : list[bool]) -> str:
    '''
    x - location
    buildingState - list of booleans. True if built
    
    returns measurement z
    '''

    p = np.random.rand()
    
    if buildingState[x] == "⬛": #occupied
        if p < forwardSensorModel(z = "⬛", m = "⬛"):
            return "⬛"
        else:
            return "⬜"

    if buildingState[x] == "⬜": #free
        if p < forwardSensorModel(z = "⬜", m = "⬜"):
            return "⬜"
        else:
            return "⬛"

def updateMapping(z : str, S : list[g1d], x : int, t : float):
    if z:
        return p2logodds(inverseSensorScheduleModel(z,S,x,t,m = "⬛")) -p2logodds(scheduleModel(S, x, t, m = "⬛"))
    else:
        return +p2logodds(scheduleModel(S, x, t, m = "⬛"))

def p2logodds(p):
    return np.log(p / (1 - p + EPS))

def logodds2p(l):
    return  np.exp(l) / (1 + np.exp(l))