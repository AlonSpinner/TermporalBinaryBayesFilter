from .gaussians import gaussian1D as g1d
import numpy as np
EPS = 1e-15

def motionModel(source,dest,a_mu,a_sigma = 0.5):
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

def updateMapping(z : str, s : g1d, t : float, pkm1: float, pr :float = 1):
    '''
    z - meaurement "⬜" or "⬛"
    s - schedule of cell
    t - world time
    pkm1 - probability of cell being occupied before measuring
    pr - probability of measuring cell ~ probability of being infront of cell
    
    returns updated probablity of cell being occupied
    '''
    alpha = 0.5 ** (1-pr)
    ps = alpha *scheduleModel(s, t) ** pr
    pz = alpha * inverseSensorScheduleModel(z, s, t) ** pr
    
    odds =  (pz/(1-pz+EPS)) * pkm1/(1-pkm1+EPS) * ((1-ps)/(ps+EPS))
    return odds2p(odds)

def p2logodds(p):
    return np.log(p / (1 - p + EPS))

def logodds2p(l):
    return  np.exp(l) / (1 + np.exp(l))

def odds2p(odds):
    return odds / (1 + odds)