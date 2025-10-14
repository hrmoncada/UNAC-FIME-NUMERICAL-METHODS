# Definir la función f(x) = x^2 - 2
def f(x):
    return x**2 - 2

# Intervalo inicial
a = 0
b = 2

# Tolerancia (precisión deseada)
tolerancia = 1e-6

# Verificar que f(a) y f(b) tengan signos opuestos
if f(a) * f(b) >= 0:
    print("El método de bisección no es aplicable: f(a) y f(b) deben tener signos opuestos.")
else:
    iteraciones = 0
    while (b - a) / 2 > tolerancia:
        c = (a + b) / 2  # Punto medio
        fc = f(c)

        print(f"Iteración {iteraciones}: a={a:.6f}, b={b:.6f}, c={c:.6f}, f(c)={fc:.6f}")

        if fc == 0:  # Encontramos la raíz exacta
            break
        elif f(a) * fc < 0:
            b = c  # La raíz está entre a y c
        else:
            a = c  # La raíz está entre c y b

        iteraciones += 1

    # Aproximación final
    raiz = (a + b) / 2
    print(f"\nRaíz aproximada encontrada: {raiz:.6f}")
