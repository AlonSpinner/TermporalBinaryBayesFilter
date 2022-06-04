from TBBF.models import forwardSensorModel
import numpy as np
import matplotlib.pyplot as plt

f = lambda pz, gama: (0.5**(1-gama) * pz**gama) * (2**(1-gama) / (pz**gama + (1-pz)**gama))

pz = forwardSensorModel("⬛", "⬛")

gama = np.linspace(0,1,100)

plt.plot(gama,f(pz,gama))
plt.plot(gama,f(1-pz,gama))
plt.plot(gama,f(pz,gama) + f(1-pz,gama)) #intergral, showing that f(pz,gama) is a PDF
plt.xlabel('gama')
plt.ylabel('probability')
plt.legend(['f(pz.gama','f(1-pz,gama)','f(pz,gama) + f(1-pz,gama)'])
plt.show()