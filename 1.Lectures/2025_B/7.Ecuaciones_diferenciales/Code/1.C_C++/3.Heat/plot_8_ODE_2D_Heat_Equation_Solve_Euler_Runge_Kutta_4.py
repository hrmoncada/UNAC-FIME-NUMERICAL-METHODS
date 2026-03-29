import numpy as np
import matplotlib.pyplot as plt

u_euler = np.loadtxt("euler.dat")
u_rk4   = np.loadtxt("rk4.dat")

plt.figure()
plt.imshow(u_euler, origin='lower')
plt.title("2D Heat Equation - Euler")
plt.colorbar()

plt.figure()
plt.imshow(u_rk4, origin='lower')
plt.title("2D Heat Equation - Runge-Kutta 4")
plt.colorbar()

plt.show()

