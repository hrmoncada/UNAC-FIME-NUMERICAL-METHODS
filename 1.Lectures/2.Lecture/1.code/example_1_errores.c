#include <stdio.h>

int main() {
    double x = 1.0 / 3.0;

    // Restamos x tres veces a 1
    double resultado = 1 - x - x - x;

    if (resultado == 0.0) {
        printf("verdadero\n");
    } else {
        printf("falso\n");
    }

    printf("Resultado: %.20f\n", resultado); // muestra el error
    return 0;
}

