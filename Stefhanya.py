import numpy as np
import matplotlib.pyplot as plt

v = np.random.rand(10)
newv=v.reshape(5,2)
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