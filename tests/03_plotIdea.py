import numpy as np
import matplotlib.pyplot as plt

f = lambda v,c: np.stack((np.expand_dims(v, axis = 0),)*3,axis=-1) * c
n = 5

x = np.random.rand(n) #robot hypothesied location
b = np.random.rand(n) #belief of occpuancy from algorithm
a = np.random.rand(n) #actual state of building
r = np.array([4,2.2]) #actual location of robot
m = np.array([4,1.8]) #measurement
s = np.random.rand(n) #schedule of occpuancy
t = 5 #time

xshow = f(x,np.array([0,1,0]))
bshow = f(b,np.array([0,0,1]))
sshow = f(s,np.array([0.7,0.5,0]))
ashow = f(a,np.array([1,0,0]))
im = np.concatenate((xshow,bshow,ashow,sshow),axis = 0)
plt.imshow(im)
plt.scatter(r[0],r[1], s = 50 ,color = 'g') #actual location of robot
plt.scatter(m[0],m[1], s = 50 ,color = 'w', marker = 's') #actual location of robot
plt.title(f"t = {t}")
plt.show()

