import numpy as np
import matplotlib.pyplot as plt

v = np.random.rand(720)
newv=v.reshape(120,6)
vtrans = newv.T
f = np.array(vtrans, order='F')  
c = np.array(vtrans, order='C') 
print('--------------vector v------------------')
print(v)
print('--------------nuevo v------------------')
print(newv)
print('--------------v transpuesta------------------')
print(vtrans)
print('--------------v transpuesta F------------------')
print(f)
print('--------------v transpuesta C------------------')
print(v)

ax1 = plt.axes()
ax2 = plt.axes([0.97, 0.35, 0.3, 0.5])
ax3=plt.axes([0.12,0.95,0.3,0.2])
ax4=plt.axes([1.35,0.1,0.8,0.4])
ax5=plt.axes([0.5,0.95,0.5,0.3])
ax6=plt.axes([1.33,0.7,0.6,0.5])
plt.show()