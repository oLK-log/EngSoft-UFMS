/*
    Programa exemplo/estudo fornecido na materia de Algoritmos e Programacao 2 da Universidade Federal
    de Mato Grosso do Sul

    ESSE PROGRAMA ABRI UM ARQUIVO TEXTO CONTENDO VARIOS DADOS DE ALUNOS(NOME E DUAS NOTAS)
    LE OS DADOS E CALCULA A MEDIA ARITMETICA DAS DUAS NOTAS DO ALUNO
    POR FIM IMPRIME NOME E MEDIA NA TELA
    OBS: no arquivo tera no max 30 alunos

    EXERCICIO FEITO USANDO O CONCEITO DE REGISTROS
*/
#include <stdio.h>
#define MAX 30

struct tipoAluno{
    char nome[MAX];
    float  n1, n2;
    float media;
};

int main(){
    struct tipoAluno vetorAlunos[MAX];
    int numeroAluno = 0;
    FILE* arq;
    FILE* arqSaida;
    char nome[MAX];

    scanf(" %s", nome);

    //abertura do arquivo
    arq = fopen(nome, "r");
    //verificacao se foi aberto
    if(arq == NULL){
        printf("O arquivo %s nao pode ser aberto.\n", nome);
    }else{
        printf("O arquivo %s foi aberto", nome);
        arqSaida = fopen("mediaRegistro.txt", "a");
        if(arqSaida == NULL){
            printf("O arquivo de saida nao pode ser aberto\n");
        }else{
            //leitura dos dados do arquivo
            fscanf(arq, "%s %f %f", vetorAlunos[numeroAluno].nome, &vetorAlunos[numeroAluno].n1, &vetorAlunos[numeroAluno].n2);

            while(feof(arq) == 0){
                //calcula a media e imprime no arquivo
                vetorAlunos[numeroAluno].media = (vetorAlunos[numeroAluno].n1 + vetorAlunos[numeroAluno].n2)/2;
                fprintf(arqSaida, "Aluno %s media %.2f\n", vetorAlunos[numeroAluno].nome, vetorAlunos[numeroAluno].media);
                numeroAluno++;
                fscanf(arq, "%s %f %f", vetorAlunos[numeroAluno].nome, &vetorAlunos[numeroAluno].n1, &vetorAlunos[numeroAluno].n2);
            }
            //fechamento do arquivo
            fclose(arq);
            fclose(arqSaida);
        }
        printf("\n");
        return 0;
    }
}
