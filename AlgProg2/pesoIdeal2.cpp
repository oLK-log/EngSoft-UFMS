#include <stdio.h>
#include <ctype.h>
//Programa: pesoIdeal2.cpp
//Programador: Lorran
//DAta: 08/08/25
/*Este programa um um valor inteiro n que representa o numero de pessoas
que o programa calculara o peso ideal a a partir da altura e sexo.
para H- (72.7*h)-58
para M- (62,1*h)-44,7
*/
int main(){
//Passo 0. Declarar variaveis
float altura;
float pesoIdeal;
char sexo;
int n;
int i;
//Passo 1. Ler n numero de pessoas
scanf("%d",n);
//Passo 2. Percorrer as n vezes
for(i=0; i<n; i++){
//Passo 3.Ler altura e sexo	
	printf("Altura:\n");
	scanf("%f",&altura);
	printf("Sexo:\n");
	scanf(" %c",&sexo);
//Passo 4.Verificar se h ou m
	if(toupper(sexo) == 'm'){
	pesoIdeal = (72.7*altura)-58;
	}
	else{
		pesoIdeal = (62.1*altura)-44.7;	
	}
//Passo 6.Imprimir peso ideal
	printf("Peso ideal: %.2f\n",pesoIdeal);
}
}

