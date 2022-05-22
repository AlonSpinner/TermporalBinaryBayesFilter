
import numpy as np
from prompt_toolkit import print_formatted_text

def p2logodds(p):
    return np.log(p / (1 - p))

def logodds2p(l):
    return  np.exp(l) / (1 + np.exp(l))

p_xocc_zocc = 0.7
p_xfree_zocc = 0.3
p_xocc_zfree = 0.4
p_xfree_zfree=0.6

p0 = 0.3
l0 = p2logodds(p0)

l = l0
z = ['occ','occ','occ','occ','occ']
for zi in z:
    if zi == 'occ':
        li = p2logodds(p_xocc_zocc)
    elif zi == 'free':
        li = p2logodds(p_xocc_zfree)
    l = l + li - l0

    print_formatted_text(logodds2p(l))
