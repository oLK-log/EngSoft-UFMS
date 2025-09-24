#include <stdio.h>

int main(){
	int idade = 0;
	int ano = 1950;
	float peso = 0;
	printf("Valor inicial da idade: %d. \n", idade);
	
	printf("Digite uma idade e um ano: \n");
	scanf("%d %d", &idade, &ano);
	printf("Digite um peso:\n");
	scanf("%f", &peso);
	
	printf("Idade informada: %d. \n", idade);
	printf("O ano informado e %d. \n", ano);
	printf("O peso informado e %.2f.\n", peso);
}
