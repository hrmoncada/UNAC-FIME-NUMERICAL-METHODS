import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Parameters (must match C++ code)
# -----------------------------
L = 1.0
N = 201
dx = L / (N - 1)

# Spatial grid
x = np.linspace(0, L, N)

# -----------------------------
# Load data from CSV
# -----------------------------
u = np.loadtxt("u1d_advection_central.csv", delimiter=",")

# -----------------------------
# Plot solution
# -----------------------------
plt.figure(figsize=(8, 4))
plt.plot(x, u, label="Numerical solution", linewidth=2)
plt.xlabel("x")
plt.ylabel("u(x,t)")
plt.title("1D Advection Equation\nCentral Space + Forward Euler")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

