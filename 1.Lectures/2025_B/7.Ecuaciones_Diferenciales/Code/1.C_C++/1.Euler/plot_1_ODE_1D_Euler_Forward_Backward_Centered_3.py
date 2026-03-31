import numpy as np
import matplotlib.pyplot as plt

# Load data
data = np.loadtxt("euler_data.dat", comments="#")

t = data[:,0]
u_forward = data[:,1]
u_backward = data[:,2]
u_center = data[:,3]
u_exact = data[:,4]

# Plot
plt.figure()
plt.plot(t, u_forward, label="Euler Forward")
plt.plot(t, u_backward, label="Euler Backward")
plt.plot(t, u_center, label="Euler Centered")
plt.plot(t, u_exact, linestyle="--", label="Exact solution")

plt.xlabel("Time")
plt.ylabel("u(t)")
plt.title("Comparison of Euler Methods (1D)")
plt.legend()
plt.grid(True)
plt.show()

