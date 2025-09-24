#include <stdio.h>
//Programa: soma2menossign.cpp
//Programador: Lorran Kaíque
//DAta: 07/08
//Esse programa le um numero inteiro e imprime a soma dos dois numeros menos significativos
int main(){
//Passo 0.Declarar variaveis
	int i;//variavel for
	int a;//salva a entrada
	int n=0;//somatorio dos 2 n menos significativo
	//Passo 1. Ler entrada
	scanf("%d",&a);
	//Passo 2. Encontrar os dois digitos menos significativos	
	for (i=0;i<2;i++){
		n+=a%10;
		a = a/10;
	}
	//Passo 3.Imprimit o somatorio
	printf("%d",n);
}
