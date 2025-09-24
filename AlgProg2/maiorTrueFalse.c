#include <stdio.h>
//Programa:maiorTrueFalse.c
//Programador: Lorran Kaique
/* Esse programa le um vetor L inteiro e verifica se o primeiro valor do vetor
eh maior que todos os outros elementos. CAso positivo imprime True, caso negativo False
*/
int main(){
//Passo 0.Inicializar abstracoes
    int tam;//tamanho do vetor
    int cont = 1;//controle que inicia o primeiro sendo maior que os outros
//Passo 1. Receber valores
    //Passo 1.1 Ler tamanho vetor
    scanf("%d", &tam);
    //Passo 1.2 Ler vetor
    //Passo 1.2.1 Inicializar vetor
    int vetor[tam];
    for(int i=0; i<tam; i++){
        scanf("%d", &vetor[i]);
    }
//Passo 2. Verificar se primeiro elem[0] eh maior que demais
    for(int i=1; i<tam; i++){
        if(vetor[0]<=vetor[i]){
            cont = 0;
        }
    }
//Passo 3.Imprimir resultado
    if(cont == 0){
        printf("false");
    } else{
        printf("true");
    }

}
