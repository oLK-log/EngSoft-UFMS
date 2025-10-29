/*
    a.Escreva uma funcao com a seguinte interface: 'void maiuscula(char cadeia[])' ,que receba uma cadeia de caracteres
    arbitrarios e substitua os caracteres que sao letras maiusculas por minusculas. Use a cadeia apenas como um vetor, juntamente com os indices necessarios.
    b.Escreva uma funcao com a seguinte interface: 'void maiuscula(char *cadeia)' ,que receba a cadeia de caracteres arbitraios e
    substitua os caracteres que são letras minusculas por maiusculas
    *Use apenas ponteiros e aritmetica com ponteiros
*/
#include <stdio.h>
#include <ctype.h>
void minuscula(char *cadeia);
void maiuscula(char cadeia[]);

int main(int argc, char *argv[]){
    if(argc < 2){
        printf("Forneca pelo menos um argumento!\n");
    }

    printf("Convertendo para Minusculo...\n");
    for(int i=1; i<argc;i++){
        minuscula(argv[i]);
        printf("%s ", argv[i]);
    }

    printf("\nConvertendo para Maiusculo...\n");
    for(int i=1; i<argc;i++){
        maiuscula(argv[i]);
        printf("%s ", argv[i]);
    }
}
void minuscula(char cadeia[]){
    char *p;
    for(p = cadeia; *p; p++){
        if(isupper(*p)){
            *p = tolower(*p);
        }
    }
}
void maiuscula(char *cadeia){
    char *p;
    for(p = cadeia; *p; p++){
        if(islower(*p)){
            *p = toupper(*p);
        }
    }
}
