#include "geometricas.h"
#include <stdio.h>

int main(){
    float r;
    float x;

    scanf("%f", &r);

    x = areaCirculo(r);

    printf("Area do circulo de raio %.2f = %.2f", r, x);
    printf("\nVolume da esfera %.2f\n", volumeEsfera(r));
    return 0;
}
