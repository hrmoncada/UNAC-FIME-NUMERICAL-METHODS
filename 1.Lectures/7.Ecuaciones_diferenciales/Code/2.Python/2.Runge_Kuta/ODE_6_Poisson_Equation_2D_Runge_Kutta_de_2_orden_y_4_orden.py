'''
La ecuación de Poisson

\nabla^2 u(x,y) = f(x,y)

es elíptica y estacionaria, no depende del tiempo. Por ello, no se resuelve directamente con métodos de Runge–Kutta, que son métodos explícitos para EDO dependientes del tiempo.

👉 La forma correcta (y muy usada en computación científica) es convertir Poisson en un problema parabólico artificial usando una relajación temporal:

\frac{\partial u}{\partial t} = \nabla^2 u(x,y) - f(x,y)

Cuando t -> \infty, la solución converge a la solución de Poisson.
Sobre esta ecuación sí se pueden aplicar RK2 y RK4.

Abajo te dejo un programa completo, documentado y claro, con:

1.Malla 2D
2.Diferencias finitas espaciales
3.RK2 y RK4 en tiempo
4.Condiciones de frontera de Dirichlet
5.Gráficos 2D

📌 Problema de ejemplo

Resolver en [0,1]×[0,1]:

\nabla^2 u(x,y) = -2\pi^2sin(\pi x)sin(\pi y)

Solución exacta:

u(x,y) = sin(\pi x)sin(\pi y)

'''
import numpy as np
import matplotlib.pyplot as plt

# =====================================================
# Parámetros del dominio
# =====================================================
Nx, Ny = 50, 50
Lx, Ly = 1.0, 1.0
dx = Lx / (Nx - 1)
dy = Ly / (Ny - 1)

x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y)

# =====================================================
# Fuente f(x,y)
# =====================================================
def f(x, y):
    return -2.0 * np.pi**2 * np.sin(np.pi * x) * np.sin(np.pi * y)

# =====================================================
# Laplaciano con diferencias finitas 2D
# =====================================================
def laplacian(u):
    lap = np.zeros_like(u)
    lap[1:-1, 1:-1] = (
        (u[2:, 1:-1] - 2*u[1:-1, 1:-1] + u[:-2, 1:-1]) / dx**2 +
        (u[1:-1, 2:] - 2*u[1:-1, 1:-1] + u[1:-1, :-2]) / dy**2
    )
    return lap

# =====================================================
# RHS de la ecuación parabólica
# u_t = ∇²u - f
# =====================================================
def rhs(u):
    return laplacian(u) - f(X, Y)

# =====================================================
# Método RK2
# =====================================================
def RK2_step(u, dt):
    k1 = rhs(u)
    k2 = rhs(u + dt*k1)
    return u + 0.5*dt*(k1 + k2)

# =====================================================
# Método RK4
# =====================================================
def RK4_step(u, dt):
    k1 = rhs(u)
    k2 = rhs(u + 0.5*dt*k1)
    k3 = rhs(u + 0.5*dt*k2)
    k4 = rhs(u + dt*k3)
    return u + (dt/6.0)*(k1 + 2*k2 + 2*k3 + k4)

# =====================================================
# Inicialización
# =====================================================
u = np.zeros((Ny, Nx))

# Condiciones de frontera (Dirichlet: u = 0)
u[0, :] = 0.0
u[-1, :] = 0.0
u[:, 0] = 0.0
u[:, -1] = 0.0

# =====================================================
# Tiempo ficticio
# =====================================================
dt = 0.25 * min(dx, dy)**2   # estabilidad
nsteps = 5000

# Escoge método: RK2 o RK4
method = "RK4"

for n in range(nsteps):
    if method == "RK2":
        u = RK2_step(u, dt)
    else:
        u = RK4_step(u, dt)

    # Reimponer frontera
    u[0, :] = 0.0
    u[-1, :] = 0.0
    u[:, 0] = 0.0
    u[:, -1] = 0.0

# =====================================================
# Solución exacta para comparación
# =====================================================
u_exact = np.sin(np.pi*X) * np.sin(np.pi*Y)
error = np.max(np.abs(u - u_exact))
print("Error máximo:", error)

# =====================================================
# Gráficos
# =====================================================
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.contourf(X, Y, u, 50, cmap="viridis")
plt.colorbar()
plt.title("Solución numérica (Poisson)")

plt.subplot(1,2,2)
plt.contourf(X, Y, u_exact, 50, cmap="viridis")
plt.colorbar()
plt.title("Solución exacta")

plt.tight_layout()
plt.show()




