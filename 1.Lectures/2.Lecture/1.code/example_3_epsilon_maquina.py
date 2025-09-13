'''
Implementacionepara calcular el épsilon de la máquina (machine epsilon), 
es decir, el número más pequeño que, al sumarse a 1.0, produce un resultado distinto de 1.0 en aritmética de punto flotante.
'''
eps = 1.0;
while ((1.0 + eps/2.0) != 1.0) {
    eps /= 2.0;
}
printf("Epsilon en double: %.20e\n", eps);

