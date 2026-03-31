import numpy as np
import matplotlib.pyplot as plt

ef = np.loadtxt("euler_forward.dat")
eb = np.loadtxt("euler_backward.dat")
ec = np.loadtxt("euler_center.dat")

plt.figure()
plt.plot(ef[:,0], ef[:,1], label="Euler Forward")
plt.plot(eb[:,0], eb[:,1], label="Euler Backward")
plt.plot(ec[:,0], ec[:,1], label="Euler Centered")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Comparación Euler 2D")
plt.legend()
plt.axis("equal")
plt.show()

