#include <stdio.h>

int main( int argc, char *argv[]){
    //argc - contador
    //argv[] - conteudo

    int i;

    if(argc > 1){
        printf("Foram inseridos %d argumentos: \n", argc);
        for(i=0; i<argc; i++){
            printf("%s %d\n", argv[i], i);
        }
    }else{
        printf("Não foram inseridos argumentos no programa.\n");
    }
}
