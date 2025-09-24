#include <stdio.h>
#include <math.h>
//Programa:raizesEq.cpp
//Programador:Lorran Kaique
/*Esse programa a partir de 3 coeficientes a,b e c, sendo a!=0,
calcula e imprime as raizes da equacao
formula: (-b-+(b²-4ac)1/2)/2a
sqrt(num);
*/
int main(){
//Passo 0. Inicializar as variaveis
	double a, b, c, r1, r2, med;
//Passo 1. Ler as entradas
	scanf("%lf %lf %lf", &a, &b, &c);
//Passo 2. Calcular as raizes
//Passo 2.1 Calcular raiz quadrada de b²-4ac
	med = (b*b)-(4*a*c);
	med = sqrt(med);
//Passo 2.2 Verificar se há raizes
	if (med>=0){
//Passo 2.3 Calcular raizes
//Passo 2.3.1 Calcula r1(para positivo)
		r1 = (-b+med)/(2*a);
//Passo 2.3.2 Calcular r2(para negativo)
		r2 = (-b-med)/(2*a);	
//Passo 4 Imprimir
	printf("%.2lf, %.2lf",r2,r1);
	} else {
		printf("A equação não possui raízes reais");
	}
}
