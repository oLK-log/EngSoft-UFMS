/* Esse programa cadastra o nome, matricula e duas notas de N alunos
(N<=50). Por fim, ele imprime a matrícula, o nome e a media de cada um deles.*/

#include <stdio.h>
#include "include/aluno.h"
#define TAM 50

int main(){
    tipoAluno vetor[TAM];
    int n;
    printf("Digite o numero de alunos a ser cadastrado: \n");
    scanf("%d", &n);

    leitura(n, vetor);
    printf("Iniciando impressao: \n");
    impressao(n,vetor);

    printf("\n");
    return 0;
}
