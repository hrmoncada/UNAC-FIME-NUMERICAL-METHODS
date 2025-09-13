'''
Implementacionepara calcular el épsilon de la máquina (machine epsilon), 
es decir, el número más pequeño que, al sumarse a 1.0, produce un resultado distinto de 1.0 en aritmética de punto flotante.
'''
def machine_epsilon():
    epsilon = 1.0
    while (1.0 + epsilon/2.0) != 1.0:
        epsilon /= 2.0
    return epsilon

if __name__ == "__main__":
    eps = machine_epsilon()
    print("Epsilon de la máquina en Python:", eps)

