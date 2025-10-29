/*
    Programa exemplo fornecido na materia de Algoritmos e Programacao 2 da Universidade Federal
    de Mato Grosso do Sul
    ESSE PROGRAMA ABRI UM ARQUIVO TEXTO CONTENDO VARIOS DADOS DE ALUNOS(NOME E DUAS NOTAS)
    LE OS DADOS E CALCULA A MEDIA ARITMETICA DAS DUAS NOTAS DO ALUNO
    POR FIM IMPRIME NOME E MEDIA NA TELA
*/
#include <stdio.h> // *FILE, printf, scanf
#define MAX 30

int main(){
    FILE* arq; /*variavel para acessar um arquivo */
    char nome[MAX]; /*nome do arquivo a ser aberto*/
    char nomeA[MAX]; /*nome do aluno*/
    float n1, n2, media;

    scanf(" %s", nome);

    /*abertura de um arquivo*/
    arq = fopen(nome, "r");

    /*verificando se o arquivo foi aberto*/
    if(arq == NULL){
        printf("\n\nArquivo %s nao pode ser aberto.\n\n", nome);
    }else{
        printf("Arquivo foi aberto!\n\n");


        /* leitura dos dados do arquivo*/
        fscanf(arq, "%s %f %f", nomeA, &n1, &n2);/*JOAO 2.5 7.5*/
        //fscanf(arq, "%f", n1)//nota 1
        //fscanf(arq, "%f", n2)//nota 2

        while( feof(arq) == 0){//verifica se chegou ao final do arquivo
            /* calcula a media e imprime na tela*/
            media = (n1+n2)/2;
            printf("%s %.2f\n", nomeA, media);
            //leitura dos proximos dados do arquivo
            fscanf(arq, "%s %f %f", nomeA, &n1, &n2);
        }
        //fechamento do arquivo
        fclose(arq);
    }
    printf("\n");
    return 0;
}
