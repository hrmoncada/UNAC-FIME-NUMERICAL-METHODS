import numpy as np
import matplotlib.pyplot as plt
U = np.loadtxt("u2d_tfinal.csv", delimiter=",")
plt.imshow(U, origin='lower', extent=[0,1,0,1])
plt.colorbar()
plt.show()

