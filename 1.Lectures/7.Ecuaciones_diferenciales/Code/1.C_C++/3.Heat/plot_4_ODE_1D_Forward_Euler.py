import numpy as np
import matplotlib.pyplot as plt

u = np.loadtxt("u1d_euler_forward.csv", delimiter=",")
x = np.linspace(0,1,u.size)
plt.plot(x,u)
plt.show()

