import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV
data = pd.read_csv("euler_results.csv")

# Graficar
plt.figure()
plt.plot(data["t"], data["Euler_Forward"], label="Euler Forward")
plt.plot(data["t"], data["Euler_Backward"], label="Euler Backward")
plt.plot(data["t"], data["Euler_Center"], label="Euler Center")
plt.plot(data["t"], data["Exact"], linestyle="--", label="Exact")

plt.xlabel("Time")
plt.ylabel("u(t)")
plt.title("1D ODE: du/dt = -λu")
plt.legend()
plt.grid(True)
plt.show()

