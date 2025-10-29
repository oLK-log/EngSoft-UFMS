#include "../include/aluno.h"

void leitura(int n, tipoAluno vetor[]){
    for(int i = 0; i < n; i++){
        printf("Matricula: \n");
        scanf("%d", &vetor[i].mat);
        printf("Nome: \n");
        scanf(" %[^\n]", vetor[i].nome);
        printf("Duas notas: \n");
        scanf("%f %f", &vetor[i].n1, vetor[i].n2);

        //media aluno
        vetor[i].media = (vetor[i].n1 + vetor[i].n2)/2;
    }
}

void impressao(int n, tipoAluno vetor[]){
    for(int i=0; i<n; i++){
        printf("%d %s %.1f\n", vetor[i].mat, vetor[i].nome, vetor[i].media);
    }
}
