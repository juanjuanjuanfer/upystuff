# Create a regression example using the formula y = b*x + a


import numpy as np
import matplotlib
matplotlib.use('TkAgg') # Usa 'TkAgg' como backend
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# Define los datos

from matplotlib.cm import viridis
from matplotlib.colors import Normalize

# Define los datos
x = np.array(range(1, 1000))
b = 5
a = 6
y = b * x + a

# Prepara la figura y el eje para la animación
fig, ax = plt.subplots()
ax.set_xlim((0, 1000))
ax.set_ylim((min(y), max(y)))

# Etiquetas y título
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('y = 5x + 6')
ax.grid(True)

# Normaliza los valores para el colormap
norm = Normalize(vmin=0, vmax=len(x))

# Función de inicialización para la animación
def init():
    return []

# Función de animación que matplotlib llamará secuencialmente
def animate(i):
    color = viridis(norm(i))  # Selecciona un color del colormap
    ax.plot(x[i], y[i], 'o', ms=3, color=color)  # Dibuja un nuevo punto con el color seleccionado
    return []

# Crea la animación usando FuncAnimation
ani = FuncAnimation(fig, animate, frames=len(x), init_func=init, interval=10, blit=False)

# Muestra la animación
plt.show(block=True)
