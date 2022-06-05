from TBBF.probalistic_models import forwardSensorModel, binaryStateMeasurementModelEnhancer_Implicit
import numpy as np
import matplotlib.pyplot as plt

f = binaryStateMeasurementModelEnhancer_Implicit(forwardSensorModel)
gama = np.linspace(0,1,100)

plt.plot(gama,f(z = "⬛", m = "⬛",gama = gama))
plt.plot(gama,f(z = "⬜", m = "⬛",gama = gama))
plt.plot(gama,f(z = "⬛", m = "⬛",gama = gama) + f(z = "⬜", m = "⬛",gama = gama)) #intergral, showing that f(pz,gama) is a PDF
plt.xlabel('gama')
plt.ylabel('probability')
plt.legend(['f(pz.gama)','f(1-pz,gama)','f(pz,gama) + f(1-pz,gama)'])
plt.show()