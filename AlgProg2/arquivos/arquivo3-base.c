/*
    Programa exemplo/estudo fornecido na materia de Algoritmos e Programacao 2 da Universidade Federal
    de Mato Grosso do Sul

    ESSE PROGRAMA ABRI UM ARQUIVO TEXTO CONTENDO VARIOS DADOS DE ALUNOS(NOME E DUAS NOTAS)
    LE OS DADOS E CALCULA A MEDIA ARITMETICA DAS DUAS NOTAS DO ALUNO
    POR FIM IMPRIME NOME E MEDIA NA TELA
*/
#include <stdio.h>
#define MAX 30
int main(){
    FILE* arq;//criando variavel tipo FILE
    FILE* arqSaida;//criando variavel do tipo FILE pra receber a saida
    char nome[MAX];
    char nomeA[MAX];
    float media, n1, n2;

    scanf(" %s", nome);

    //abrindo arquivo
    arq = fopen(nome, "r"); //'r' indica leitura
    //verificando se o arquivo foi aberto
    if(arq == NULL){
        printf("\n\n\nO arquivo %s nao pode ser aberto\n\n\n", nome);
    }else{
        printf("O arquivo %s foi aberto", nome);
        //abrir/criar um arquivo de saida
        arqSaida = fopen("media.txt", "a");
        if(arqSaida == NULL){
            printf("O arquivo de saida nao pode ser criado");
        }else{
            //leitura dos dados do arquivo
            fscanf(arq, "%s %f %f", nomeA, &n1, &n2);
            while(feof(arq)==0){
                media = (n1+n2)/2;
                fprintf(arqSaida,"Aluno %s media = %f\n", nomeA, media);
                fscanf(arq, "%s %.2f %.2f", nomeA, &n1, &n2);
            }
            fprintf(arqSaida,"\n");
            fclose(arq);
            fclose(arqSaida);
        }
        printf("\n");
        return 0;
    }

}
