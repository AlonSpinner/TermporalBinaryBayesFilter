from TBBF.models import forwardSensorModel
import numpy as np
import matplotlib.pyplot as plt

f = lambda pz, gama: 0.5**(1-gama) * pz**gama

pz1 = forwardSensorModel("⬛", "⬛")
pz2 = forwardSensorModel("⬜", "⬛")

print(f"pz1 + pz1 = {pz1 + pz2}")

gama = np.linspace(0,1,100)
int_pzgama = np.zeros_like(gama)
for i, g in enumerate(gama):
    alpha = 2**(1-g) / (pz1**g + pz2**g) #can we find a closed formula not depended on pz1 or pz2 for this?
    int_pzgama[i] = alpha * (f(pz1,g) + f(pz2,g))

plt.plot(gama,int_pzgama)
plt.xlabel('gama')
plt.ylabel('int(p(z|m = occ, gama)')
plt.show()