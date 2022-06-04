from re import A
import numpy as np
import matplotlib.pyplot as plt
from math import erf


class gaussian1D:
    def __init__(self,mu : float,sigma : float) -> None:
        self.mu : float = mu
        self.sigma : float = sigma

    def pdf(self,x : float):
        return 1/(np.sqrt(2*np.pi)*self.sigma) * np.exp(-(x-self.mu)**2/(2*self.sigma**2))
        

    def sample(self, n : int = 1):
        return np.random.normal(self.mu, self.sigma, n)

    def cdf(self,x : float): #cumulative distibution function
        # https://en.wikipedia.org/wiki/Normal_distribution
        #returns integral from [-inf,x]

        return 0.5*(1+nperf((x-self.mu)/(self.sigma*np.sqrt(2))))

    def plot(self) -> None:
        dt = 0.1
        tmin = self.mu - 3 * self.sigma
        tmax = self.mu + 3 * self.sigma
        t = np.array(np.arange(tmin,tmax,dt))
        dydt = self.pdf(t)
        y = self.cdf(t)

        fig, axes = plt.subplots(1,2)
        axes[0].plot(t,y)
        axes[0].set_title('y(t)')
        axes[1].plot(t,dydt)
        axes[1].set_title('dydt(t)')
        plt.show()

class gaussian1DT:
#SOMETHING NOT WORKING HERE AT ALL

#https://en.wikipedia.org/wiki/Truncated_normal_distribution
    def __init__(self,mu,sigma,a,b):
        self.mu : float = mu
        self.sigma : float = sigma
        self.a = a
        self.b = b

        self.alpha = (a-mu)/sigma
        self.beta = (b-mu)/sigma
        self.Z = npPhi(self.beta) - npPhi(self.alpha)

    def pdf(self,x):
        zeta = (x-self.mu)/self.sigma
        phi = 1/np.sqrt(2*np.pi) * np.exp(-0.5*zeta**2)
        return phi/(self.sigma*self.Z)

    def cdf(self,x):
        zeta = (x-self.mu)/self.sigma
        return (npPhi(zeta)-npPhi(self.alpha))/self.Z

    def plot(self):
        dt = 0.1
        tmin = self.a - self.sigma
        tmax = self.b + self.sigma
        t = np.array(np.arange(tmin,tmax,dt))
        dydt = self.pdf(t)
        y = self.cdf(t)

        fig, axes = plt.subplots(1,2)
        axes[0].plot(t,y)
        axes[0].set_title('y(t)')
        axes[1].plot(t,dydt)
        axes[1].set_title('dydt(t)')
        plt.show()

def nperf(x):
    if np.isscalar(x):
        return erf(x)
    else:
        return np.array([erf(val) for val in x])

def npPhi(x):
    return 0.5*(1 + nperf(x/np.sqrt(2)))



    