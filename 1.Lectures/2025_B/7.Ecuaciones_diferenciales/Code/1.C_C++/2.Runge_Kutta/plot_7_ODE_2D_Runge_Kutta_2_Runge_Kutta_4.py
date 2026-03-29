import numpy as np
import matplotlib.pyplot as plt

rk2 = np.loadtxt("rk2.csv", delimiter=",", skiprows=1)
rk4 = np.loadtxt("rk4.csv", delimiter=",", skiprows=1)

plt.figure()
plt.plot(rk2[:,1], rk2[:,2], label="RK2")
plt.plot(rk4[:,1], rk4[:,2], label="RK4")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Runge–Kutta 2 vs Runge–Kutta 4 (2D)")
plt.legend()
plt.axis("equal")
plt.grid(True)
plt.show()

