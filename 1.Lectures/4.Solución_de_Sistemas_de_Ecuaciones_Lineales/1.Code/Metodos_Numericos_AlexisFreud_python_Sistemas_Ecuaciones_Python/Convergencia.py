# Alexis Mendoza Valencia
# Estudiante Tecnológico de Monterrey, campus guadalajara

# Convergencia

"""
Nota: Para explicar este método recomiendo utilizar
      una pagina web llamada Cocalc para correr el metodo.
      Al menos es la pagina que yo utilice, pues ya tiene
      incluidas las librerias necesarias: numpy y mathplotlib.
      La liga es: cocalc.com
"""

import numpy as np
import matplotlib.pyplot as plt

"""
Definicion: La convergencia es un termino que se utiliza en 
            limites. Decimos que una funcion converge a un
            valor cuando se acerca hasta este. 
            Por ejemplo, si graficamos un logaritmo natural,
            podemos ver que si el numero se hace mas pequeño
            el valor tiende a cero. En este caso se acerca, 
            mas nunca lo toca (sabemos que ln(0) no esta definido.
            
            Vamos a ver ejemplos entonces.
"""

import math
def logaritmo(x):
    return math.log(x)


def convergencia(funcion, valor_inferior, valor_superior):
    valores_X = np.linspace(valor_inferior, valor_superior, 100)
    valores_Y = [funcion(valores_X[i]) for i in range(len(valores_X))]

    plt.plot(valores_X, valores_Y)
    plt.grid()
    plt.show()


print("Ejemplo 1")
convergencia(logaritmo, 0.01, 10)
convergencia(logaritmo, 0.000001, 1)
"""
Veremos entonces al correr el programa que mientras el valor inferior
sea mas pequeño tendremos un valor de Y que se acerca cada vez mas a cero.

Pero ahora, podemos ver esto de diferentes formas. Un ejemplo es la raiz 
de dos.

Si tenemos que x = raiz(2)
podemos decir que x^2 = 2
Por lo tanto, x^2 - 2 = 0

Estariamos buscando entonces el valor mas pequeño para el cual es valida
esta funcion, que buscamos que tenga convergencia a cero.
"""

def raiz_dos(x):
    return abs(x**2 - 2)


print("Ejemplo 2")
convergencia(raiz_dos, 0, 2)
convergencia(raiz_dos, 1.25, 1.75)
convergencia(raiz_dos, 1.4, 1.44)

"""
Y asi, poco a poco, nos acercamos al valor deseado.
"""
