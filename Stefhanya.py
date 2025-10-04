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
# 1) Barras con error en ax1
y = vtrans[0]
x = np.arange(len(y))
error = np.random.rand(len(y))
ax1.bar(x, y, yerr=error, capsize=5, color="purple")
ax1.set_xlim(0, 120)      
ax1.set_ylim(-1, 2)       

# 2) Histograma 2D en ax2
ax2.hist2d(vtrans[1], vtrans[2], bins=6, cmap="plasma")
ax2.set_xlim(-0.1 ,1.1)
ax2.set_ylim(-0.1, 1.1)

# 3) Boxplot en ax3
ax3.boxplot(vtrans[3])
ax3.set_xlim(0.5, 1.5)
ax3.set_ylim(min(vtrans[3])-0.1, max(vtrans[3])+0.1)

# 4) Histograma en ax4
ax4.hist(vtrans[2], bins=8, color="pink", alpha=0.7)
ax4.set_xlim(-0.1,1.1)
ax4.set_ylim(-1, 26)

# 5) Línea en ax5
ax5.plot(vtrans[5], color="green")
ax5.set_xlim(0, 120)
ax5.set_ylim(0, 1)

# 6) Pie chart en ax6
ax6.pie(vtrans[3])

plt.show()