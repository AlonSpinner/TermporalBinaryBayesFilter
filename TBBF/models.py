import numpy as np

def forwardSensorModel(self,z,x,pm):
    #return probability of achieving measurement z given probablistic estimate on cell's occpunacy
        # if z == "⬜":
        #     return logisticCurve(t,gama,sigma)
        # elif z == "⬛":
        #     return 1 - logisticCurve(t,gama)
    pass

def inverseSensorModel(z, S, x, t, m = "⬛"):
    '''
    z - meaurement "⬜" or "⬛"
    S - schedule of building
    x - location of cell
    t - world time
    
    returns probablity of m
    '''
    gama, sigma = S[x]

    if m == "⬛":
        if z == "⬜":
            return logisticCurve(t,gama,sigma)
        elif z == "⬛":
            return 1 - logisticCurve(t,gama)

    elif m == "⬜":
        if z == "⬜":
            return logisticCurve(t,gama,sigma)
        elif z == "⬛":
            return 1 - logisticCurve(t,gama)
    
    else:
        raise Exception("m is not ⬜ or ⬛")

    
def scheduleModel(S, x, t, m = "⬛"):
    #returns proability of m being occupied given schedule and time
    gama, sigma = S[x]
    if m == "⬛":
            return logisticCurve(t,gama,sigma)

    elif m == "⬜":
            return logisticCurve(t,gama,sigma)  
    else:
        raise Exception("m is not ⬜ or ⬛")

def logisticCurve(t, gama, sigma):
    y = 1/(1 + np.exp(-sigma*(t-gama)))
    return y