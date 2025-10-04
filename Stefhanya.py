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

fig = plt.figure()  

ax1 = fig.add_axes([0.0, 0.0, 0.9, 0.9])  
ax2 = fig.add_axes([0.97, 0.35, 0.3, 0.5])
ax3 = fig.add_axes([0.12, 1, 0.3, 0.2])
ax4 = fig.add_axes([1.5, 0.1, 0.8, 0.4])
ax5 = fig.add_axes([0.55, 1.02, 0.5, 0.3])
ax6 = fig.add_axes([1.33, 0.7, 0.6, 0.5])

# 1) Barras con error
y = vtrans[0]
x = np.arange(len(y))
error = np.random.rand(len(y))
ax1.bar(x, y, yerr=error, capsize=5, color="purple", label="Valores con error")
ax1.set_title("Barras con error")
ax1.legend()
ax1.grid(True)

# 2) Histograma 2D
ax2.hist2d(vtrans[1], vtrans[2], bins=6, cmap="plasma")
ax2.set_title("Histograma 2D")
ax2.grid(True)

# 3) Boxplot
ax3.boxplot(vtrans[3])
ax3.set_title("Boxplot")
ax3.grid(True)

# 4) Histograma
ax4.hist(vtrans[2], bins=8, color="pink", alpha=0.7, label="Datos fila 2")
ax4.set_title("Histograma")
ax4.legend()
ax4.grid(True)

# 5) Línea
ax5.plot(vtrans[5], color="green", label="Fila 5")
ax5.set_title("Gráfico de línea")
ax5.legend()
ax5.grid(True)

# 6) Pie chart
fig = ax6.figure
labels = [f"Dato {i}" for i in range(len(vtrans[2]))]
wedges, texts = ax6.pie(vtrans[2])
ax6.set_title("Gráfico de Pie")

# leyenda solo del pie mostrando los datos
fig.legend(wedges, labels,
           loc="lower center",
           bbox_to_anchor=(0.5, -0.2),
           ncol=10,
           fontsize=8,
           title="Datos del Pie")
plt.subplots_adjust(bottom=0.25)

plt.show()
