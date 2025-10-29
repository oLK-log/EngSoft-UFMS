/*
    Programa exemplo fornecido na materia de Algoritmos e Programacao 2 da Universidade Federal
    de Mato Grosso do Sul

    PROGRAMA PARA ABRIR UM ARQUIVO TEXTO CONTENDO VARIOS NUMEROS INTEIROS
    ELE LE OS NUMEROS DO ARQUIVO E IMPRIME ELES
*/
#include <stdio.h>
#define MAX 30

int main(){
    FILE *arqent;
    char nome[MAX];
    int num;

    printf("Nome do arquivo: ");
    scanf(" %s", nome);

    //abrir arquivo
    arqent = fopen(nome, "r");
    if(arqent == NULL){
        printf("Erro na abertura do arquivo %s", nome);
    }else{
        //ler os dados e processamento
        fscanf(arqent, "%d", &num);
        while(feof(arqent) == 0){//enquanto !(fim de arquivo)
            printf("%d\n", num);
            fscanf(arqent, "%d", &num);
        }
        //fecha o arquivo
        fclose(arqent);
    }
    printf("\n");
    return 0;
}
