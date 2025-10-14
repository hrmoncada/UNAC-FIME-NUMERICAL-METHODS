# Alexis Mendoza Valencia
# Estudiante Tecnológico de Monterrey, campus guadalajara

# Metodo Gauss Seidel

"""
Decripcion: El metodo de Gauss Seidel nos permite encontrar los valores
            x1, x2, x3, ..., xn de nuestro sistema de ecuaciones de
            n variables con n ecuaciones, es decir, de una matriz cuadrada.

Primero, los valores mas grandes de cada sistema de ecuaciones convertido
en matriz deben encontrarse en la diagonal principal.
1. Alineamos los valores más grandes en la diagonal.
2. Definimos el error.
3. x1 = x2 = x3 = 0
4. Ahora despejamos x1 en la primera fila, x2 en la segunda...
5. Utilizamos siempre los nuevos valores que vamos tomando para calcular lo siguiente.
"""

def getX1(x2, x3):
    return (7.85 + 0.1*x2 + 0.2*x3)/3

def getX2(x1, x3):
    return (-19.3 - 0.1*x1 + 0.3*x3)/7

def getX3(x1, x2):
    return (71.4 - 0.3*x1 + 0.2*x2)/10

def err(real, nuevo):
    return abs((real - nuevo) / real)

def GaussSeidel():
    x1 = 0
    x2 = 0
    x3 = 0
    x1a = 0.00001
    x2a = 0.00001
    x3a = 0.00001
    error = 0.001

    for i in range(100):
        x1 = getX1(x2, x3)
        x2 = getX2(x1, x3)
        x3 = getX3(x1, x2)
        print("itera %d"%i, x1, x2, x3)

        #Errores
        if err(x1a, x1) < error and err(x2a, x2) < error and err(x3a, x3):
            break
        x1a = x1
        x2a = x2
        x3a = x3
    print("Valores: ", x1, x2, x3, "\n")

GaussSeidel()


print("Como se ve en el resultado los valores son \n"
      + "x1 = 3.0, x2 = -2.5 y x3 = 7.0, solo que \n"
      + "el error requerido no permite tanta precisión.\n")

"""
Ejercicio 2
"""

def gauss_seidel_2():
    print("Ejercicio 2")
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    x1a = 0.00001
    x2a = 0.00001
    x3a = 0.00001
    x4a = 0.00001

    for i in range(5):
        x1a = x1
        x2a = x2
        x3a = x3
        x4a = x4

        x1 = getX1_2(x2, x3, x4)
        x2 = getX2_2(x1, x3, x4)
        x3 = getX3_2(x1, x2, x4)
        x4 = getX4_2(x1, x2, x3)
        print("itera %d" % i, x1, x2, x3, x4)

    print("Valores: ", x1, x2, x3, x4, "\n")
    print("Errores:")
    print("x1 = ", err(x1a, x1))
    print("x2 = ", err(x2a, x2))
    print("x3 = ", err(x3a, x3))
    print("x4 = ", err(x4a, x4))
    print("El error final sería el de x4 de ", err(x4a, x4))

def getX1_2(x2, x3, x4):
    return (3 + 2*x2 - x3 - 2*x4)/7

def getX2_2(x1, x3, x4):
    return (-2 - 2*x1 - 3*x3 - x4)/8

def getX3_2(x1, x2, x4):
    return (5 + x1 - 2*x4)/5

def getX4_2(x1, x2, x3):
    return (4 - 2*x2 + x3)/4

gauss_seidel_2()
