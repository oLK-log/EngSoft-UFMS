#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char* argv[]) {
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
	return 0;
}
