#include <stdio.h>
//Programa: contaDig.cpp
//Programador: Lorran Kaíque
//Data: 12/08
/*Este programa lê dois numeros inteiros, um indicando a quantidade de numeros a serem
lidos e o outro o valor de um digito de 1 a 9. O programa computa a quantidade de vezes q o digito
esta presente no numero*/
int main(void){
//Passo 0. Inicializar as variaveis
int num, dig, qtd, menos;
//Passo 1. Ler valores
scanf("%d %d", &num, &dig);
//Passo 2. percorrer num
while(num != 0){
	if(num%10 == dig){
		qtd ++;
	}
	num = num/10;
}
//Passo 3. Imprimir resultado
printf("%d", qtd);
}
