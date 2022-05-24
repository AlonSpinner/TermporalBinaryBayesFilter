import numpy as np
from math import erf

class gaussian1D:
    def __init__(self,mu,sigma):
        self.mu : float = mu
        self.sigma : float = sigma

    def pdf(self,x):
        return 1/(np.sqrt(2*np.pi)*self.sigma) * np.exp(-(x-self.mu)**2/(2*self.sigma**2))
        

    def sample(self, n = 1):
        return np.random.normal(self.mu, self.sigma, n = 1000)

    def cdf(self,x): #cumulative distibution function
        # https://en.wikipedia.org/wiki/Normal_distribution
        #returns integral from [-inf,x]

        return 0.5*(1+nperf((x-self.mu)/(self.sigma*np.sqrt(2))))

def nperf(x):
    #erf on arrays
    return np.array([erf(val) for val in x])

    