#include <stdio.h>
#include <string.h>
#include <locale.h>

#define N 20
#define X 50
//Curso C/Progressivo
//STRINGS
int main(){
    setlocale(LC_ALL,"Portuguese");//permite impressao de caractere especial
    /*
    char s[10];//le no max 0 caracteres, o ultimo e resenvado para o \0

    //scanf convencional
    printf("Digite algo(scanf convencional):\n");
    scanf("%s", s);
    fflush(stdin);

    printf("Resultado: %s\n\n", s);
    //scanf aprimorado
    printf("Digite algo: (scanf aprimorado):\n");
    scanf("%9[^\n]s", s);//limita a uma leitura de 9 campos e aceita espacos
    fflush(stdin);

    printf("Resultado: %s\n\n", s);
    //gets
    printf("Digite algo(leitura pelo gets):\n");
    gets(s);
    fflush(stdin);
    //puts
    puts("Resultado: ");
    puts(s);
    puts("");

    //fgets
    printf("Digite algo (leitura pelo fgets):\n");
    fgets(s, 10, stdin);
    fflush(stdin);
    puts("Resultado");
    puts(s);
    */
    /*
    //STRCPY
    char origem[N] = {"Olá, mundo!"};
    char destino[N];

    printf("Antes do strcpy:\n");
    puts(origem);
    puts(destino);

    strcpy(destino, origem);

    printf("Depois do strcpy:\n");
    puts(origem);
    puts(destino);
    */
    /*
    //STRCAT
    char s1[X] = {"Lógica de"};
    char s2[X] = {" Programação"};

    printf("Antes do strcat:\n");
    printf("str1: %s\n", s1);
    printf("str2: %s\n",s2);

    strcat(s1,s2);

    printf("Depois do strcat:\n");
    printf(s1);
    */
    /*
    //STRLEN
    char n[X];
    int i;

    printf("Digite um texto:\n");
    gets(n);
    i = strlen(n);
    printf("\nTamanho do texto: %d\n\n",i);

    printf("Impressão de posição a posição:\n");
    for(i=0; i<strlen(n);i++){
        printf("%c",n[i]);
    }
    */
    //STRCMP
    char hardText[N] = {"exit"};
    char senha_usr[N];
    int ok;

    printf("Digite um texto:\n");
    gets(senha_usr);

    ok = strcmp(hardText, senha_usr);

    if(ok==0){
        printf("Textos iguais.\n");
    }else{
        printf("Textos diferentes.\n");
    }
}

