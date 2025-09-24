#include <stdio.h>
#include <string.h>
#include <locale.h>//permite que use as regras gramaticais br

#define TAM 50
//DAte: 03/09
//Struct
 struct tipo_pessoa{
        int idade;
        float peso;
        char nome[TAM];
    };

    typedef struct tipo_pessoa tipo_pessoa;
    // define que (struct tipo_pessoa) == tipo_pessoa
//Matriz
int main(){
    /*
    int linha, coluna;
    scanf("%d",&linha);
    scanf("%d", &coluna);
    int matriz[linha][coluna];


    for(int i=0; i<linha; i++){
        for(int j=0; j<coluna; j++){
            scanf("%d", &matriz[i][j]);
        }
    }

    for(int i=0; i<linha; i++){
        for(int j=0; j<coluna; j++){
            printf("%d ",matriz[i][j]);
        }
        printf("\n");
    }
    */

    //Structs
    setlocale(LC_ALL, "Portuguese");

    //Criando e inicializando
    tipo_pessoa pes = {0, 0.0, "Teste"};

    printf("Inicio:\n");
    printf("pes.idade: %d\n", pes.idade);
    printf("pes.peso: %.2f\n", pes.peso);
    printf("pes.nome: %s\n", pes.nome);

    //Atribuindo valores aos campos
    pes.idade=10;
    pes.peso=63.2;
    strcpy(pes.nome, "Lorena");

    printf("pes.idade: %d\n", pes.idade);
    printf("pes.peso: %.2f\n", pes.peso);
    printf("pes.nome: %s\n", pes.nome);





return 0;
}
