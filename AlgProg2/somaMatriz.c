#include <stdio.h>
//Programa: somaMatriz.c
//Programador: Lorran Kaique
//Data: 24/08
/*Esse programa recebe duas matrizes A e B, e entao realiza a soma das posicoes
Ai,j e Bi,j delas, gerando e imprimindo uma matriz C resultante*/
int main(){
//Passo 0.Inicializar abstracoes
    //Passo 0.1 Inicializar variaveis
    int m, n;//referentes aos tamanho das matrizes
    int a[100][100], b[100][100], c[100][100];//declarandi variaveis
//Passo 1. Receber valores
    //Passo 1.1Ler tamanhos
    scanf("%d %d", &m, &n);
    //Passo 1.2 Ler matrizes
    //a
    for(int i=0; i<m;i++){
        for(int j=0; j<n; j++){
            scanf("%d", &a[i][j]);
        }
    }
    //b
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            scanf("%d", &b[i][j]);
        }
    }
//Passo 2.Somar matrizes
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
           c[i][j] = a[i][j] + b[i][j];
        }
    }

//Passo 3.Imprimir matriz c
    for(int i=0; i<m;i++){
        for(int j=0; j<n; j++){
            printf("%d ", c[i][j]);
        }
        printf("\n");
    }

}
