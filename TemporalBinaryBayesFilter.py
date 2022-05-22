
import numpy as np
import matplotlib.pyplot as plt
from prompt_toolkit import print_formatted_text

def p2logodds(p):
    return np.log(p / (1 - p))

def logodds2p(l):
    return  np.exp(l) / (1 + np.exp(l))

def logisticCurve(x, x0, k = 0.3, L = 1):
    y = L/(1 + np.exp(-k*(x-x0)))
    return y

# t = np.linspace(0,5)
# y = logisticCurve(t,3,0)
# plt.plot(t,y)
# plt.show()

gama = 1
p_xocc_zocc = lambda x: 0.8 * logisticCurve(x,0.5,gama)
p_xfree_zocc = lambda x: 1 - p_xocc_zocc(x)
p_xfree_zfree = lambda x: 0.7 * logisticCurve(x,0.5,gama)
p_xocc_zfree = lambda x: 1 - p_xfree_zfree(x)

p0 = 0.5
p0 = lambda x: logisticCurve(x,0.5,gama)
l0 = 

l = l0
z = ['occ','occ','occ','occ','occ']
t = [1,2,3,4,5]
for zi,ti in zip(z,t):
    if zi == 'occ':
        li = p2logodds(p_xocc_zocc(ti))
    elif zi == 'free':
        li = p2logodds(p_xocc_zfree(ti))
    l = l + li - l0

    print_formatted_text(logodds2p(l))
