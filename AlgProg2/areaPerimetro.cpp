#include <stdio.h>
#include <math.h>
//Programa: areaPerimetro.cpp
//Programador: Lorran Ka�que
//Data: 12/08/25
/*Este programa recebe os lados de um tri�ngulo e calcula/imprimi os lados, per�metro e �rea
*/
int main(void){	
//Passo 0. Inicializar variaveis
double l1, l2, l3, per, sPer, area;
//Passo 1. Ler os lados do tri�ngulo
scanf("%lf", &l1);
scanf("%lf", &l2);
scanf("%lf", &l3);
//Passo2. Calcular perimetro, semiPerimetro e Area
//Passo 2.1 Calcular Perimetro
per = l1 + l2 + l3;
//Passo 2.2 Calcular sPer
sPer = per / 2;
//Passo 2.3 Calcular area
//Formula de Heron area = (sPer*(sPer-l1)*(sPer-l2)*(sPer-l3))�/2
area = sqrt(sPer*(sPer-l1)*(sPer-l2)*(sPer-l3));
//Passo 3 Imprimir
printf("Lados = %5.2f, %5.2f, %5.2f\n", l1, l2, l3);
printf("Per�metro = %5.2f\n", per);
printf("�rea = %5.2f\n", area);
}

