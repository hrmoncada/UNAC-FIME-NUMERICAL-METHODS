import numpy as np
import matplotlib.pyplot as plt

# Cargar datos
rk2 = np.loadtxt("rk2.dat")
rk4 = np.loadtxt("rk4.dat")

# Extraer columnas
t2, y2 = rk2[:,0], rk2[:,1]
t4, y4 = rk4[:,0], rk4[:,1]

plt.figure()
plt.plot(t2, y2, label="RK2")
plt.plot(t4, y4, label="RK4")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Runge–Kutta 1D: RK2 vs RK4")
plt.legend()
plt.grid()
plt.show()

