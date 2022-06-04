import numpy as np
import matplotlib.pyplot as plt

from TBBF.gaussians import gaussian1D, gaussian1DT

g = gaussian1D(3,1)
g.plot()

g = gaussian1DT(2,1,2,3)
g.plot()



