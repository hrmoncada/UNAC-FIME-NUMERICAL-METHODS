/*
Implementacionepara calcular el épsilon de la máquina (machine epsilon), 
es decir, el número más pequeño que, al sumarse a 1.0, produce un resultado distinto de 1.0 en aritmética de punto flotante.
*/
#include <stdio.h>

void largodoble(){
  long double eps = 1.0;
  while ((1.0 + eps/2.0) != 1.0) {
    eps /= 2.0;
  }
  printf("Epsilon en double: %.20Lf\n", eps);
  printf("Epsilon en double: %.20e\n", eps);
}

void doble(){
  double eps = 1.0;
  while ((1.0 + eps/2.0) != 1.0) {
    eps /= 2.0;
  }
  printf("Epsilon en double: %.20e\n", eps);
}

int main() {
    float eps = 1.0f;
    while ((1.0f + eps/2.0f) != 1.0f) {
        eps /= 2.0f;
    }
    printf("Epsilon de la máquina en C: %.10e\n", eps);

    doble();
    largodoble();
    return 0;
}

