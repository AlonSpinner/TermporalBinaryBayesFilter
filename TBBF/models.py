from .gaussians import gaussian1D as g1d
import numpy as np

def inverseSensorModel(z : str, S : g1d, x : int, t : float, m = "⬛"):
    '''
    z - meaurement "⬜" or "⬛"
    S - schedule of building
    x - location of cell
    t - world time
    
    returns probablity of m
    '''
    num = forwardModel(z, m) * scheduleModel(S, x, t , m)
    denum = forwardModel(z, m = "⬜") * scheduleModel(S, x, t , m = "⬜") + \
                forwardModel(z, m = "⬛") * scheduleModel(S, x, t , m = "⬛")
    return num/denum

def forwardModel(z : str, m : str):
    if m == "⬛":
        if z == "⬜":
            return 0.1
        elif z == "⬛":
            return 0.9

    elif m == "⬜":
        if z == "⬜":
            return 0.7
        elif z == "⬛":
            return 0.3
    
def scheduleModel(S : list[g1d], x : int, t : float , m : str = "⬛"):
    #returns proability of m being occupied given schedule and time
    s = S[x]
    if m == "⬛":
            return s.cdf(t)
    elif m == "⬜":
            return 1 - s.cdf(t)
    else:
        raise Exception("m is not ⬜ or ⬛")