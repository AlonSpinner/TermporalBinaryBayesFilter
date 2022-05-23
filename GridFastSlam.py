import numpy as np
from dataclasses import dataclass

@dataclass
class particle:
    location : int
    logOddsGrid : np.ndarray
    weight : float

class GridFastSlam: 
    def __init__(self, n : int, schedule : np.ndarray):
        self.n = n #number of cells
        
        initialLogOddsMap = np.zeros(n)
        
        self.particles : list[particle] =  [particle(ip, initialLogOddsMap, 1/n) for ip in range(n)]
        self.schedule : np.ndarray = schedule
        

    def updateMaps(self,z,t):
        for p in self.particles:
            for i in range(self.n):
                p.logOddsGrid[i] -= p2logodds(self.scheduleModel(i,t))
                if p.location == i:
                    if z == "⬜":
                        p.logOddsGrid[i] += p2logodds(self.inverseSensorModel(z,i,t))
                    elif z == "⬛":
                        p.logOddsGrid[i] += p2logodds(self.inverseSensorModel(z,i,t))

    def moveParticles(self,a):
        for p in self.particles:
            p.location += a
        self.particles = [p for p in self.particles if 0 <= p.location < self.n] #delete particles not in range

    def reWeight(self,z,t):
        for p in self.particles:
            p.weight *= self.forwardSensorModel(z,p.location,logodds2p(p.logOddsGrid))
        pass

    def forwardSensorModel(self,z,x,pm):
        scheduleModel(x,t)
        if z == "⬜"
        pass
    
    def inverseSensorModel(self,z,x,t):
        gama = self.schedule[x]
        if z == "⬜":
            return logisticCurve(t,gama)
        elif z == "⬛":
            return 1 - logisticCurve(t,gama)
    
    def scheduleModel(self,x,t):
        gama = self.schedule[x]
        return 0.8*logisticCurve(t,gama)

def logisticCurve(x, x0, k = 0.3, L = 1):
    y = L/(1 + np.exp(-k*(x-x0)))
    return y

def p2logodds(p):
    return np.log(p / (1 - p))

def logodds2p(l):
    return  np.exp(l) / (1 + np.exp(l))
    