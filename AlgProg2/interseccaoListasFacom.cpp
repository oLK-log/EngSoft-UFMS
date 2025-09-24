#include <stdio.h>
#include <string.h>
//Programa: interseccaoListasFacom.cpp
//Programador: Lorran Kaíque
//Data: 13/08
/* Este programa recebe dois inteiro tamA e tamB que indica o tamanho das listas e as listas. Ele encontra a interseccao das duas listas e imprimi a quantidade
equivalente a essa inteseccao*/
int main(){
//Passo 0. Inicializar as variaveis
	int tamA, tamB;
	int qtdInter = 0;
	//Passo 1. Ler elementos
	//Passo 1.1.1 Ler tamanho A
	scanf("%d", &tamA);
	//Passo 1.1.2 Ler lista
	int vetorA[tamA];
	for (int i=0; i<tamA; i++){
		scanf("%d", &vetorA[i]);
	}
	//Passo 1.2.1 Ler tamanho B
	scanf("%d", &tamB);
	//Passo 1.2.2 Ler vetor
	int vetorB[tamB];
	for(int i=0; i<tamB; i++){
		scanf("%d",&vetorB[i]);
	}
	//Passo 2. verificar se há rgas iguais
	//Passo 2.1 Inicializar vetor que contera os valores que se repetem
	//o vetor deve ter tamanho no max o tam do menor dos vetores a/b
	int vetorIguais[tamA];
	/*if (tamA > tamB){
		int vetorIguais[tamA+1] = {0};
	}else {
		int vetorIguais[tamB+1] = {0};
	}*/
	//char vetorIguais[5][100];
	//strcpy(vetorIguais[0], "vazia");
	//Passo 2.2 Verificar se o valor se repete
	for (int i=0; i<tamB; i++){
		for(int x=0; x<tamA; x++){
			if(vetorA[i] == vetorB[x]){
				vetorIguais[qtdInter] = vetorB[i];
				qtdInter ++;
				break;
			}
		}
	}
	//Passo 3. Imprimir vetores
	if (qtdInter == 0){
		printf("vazia\n");
	} else {
		for(int i=0; i<qtdInter; i++){
		printf("%d ",vetorIguais[i]);
	}
	printf("\n");
	}
}
