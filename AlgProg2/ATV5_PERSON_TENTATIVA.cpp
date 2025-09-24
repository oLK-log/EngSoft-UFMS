#include <stdio.h>
#include <locale.h>
#define MAX 30
#define TAM 10
//Program: person.cpp
//Programmer: Lorran KAique
//This program stores the name, height, and date of birth of up to 10 people
//Define Structs
struct dataNascimento{
    int dia,mes,ano;
};
typedef struct dataNascimento dataNascimento;
struct Pessoa {
    char nome[MAX+1];
    float altura;
    dataNascimento dtNas;

};
typedef struct Pessoa Pessoa;
//prototype functions
int menu();
void inserir(Pessoa vetor[], int &np);
void listarTodos(Pessoa vetor[], int nP);
void listarPorData(Pessoa vetor[], int nP, dataNascimento dt);

//MAin
int main(){
    setlocale(LC_ALL, "Portuguese");
    Pessoa lista[TAM];
    int op;
    int np=0;
    int controler=0;
    do{
        op = menu();
        if(op==1){
            inserir(lista, np);
    }else if(op==2){
            listarTodos(lista, np);
        }else if(op==3){
            dataNascimento D;
            listarPorData(lista, np, D);

        }else{
            controler=1;
        }

    }while(controler==0);

}
//Declaration of functions
//menu
int menu(){
    int res;
    printf("Esse é o menu.\n Escolha uma opção:\n");
    printf("------------\n 1 -Inserir Pessoa\n------------\n 2 -listar todos os nomes e altura\n------------\n 3 -nomes que nasceram antes de determinada data\n");
    scanf("%d",&res);
    return res;
}
//1-Insert person
void inserir(Pessoa vetor[], int &np){
    printf("VAlor de np:%d\n",np);
    printf("Você está adicionando uma pessoa!\nDigite o nome:\n");
    scanf(" %[^\n]",vetor[np].nome);
    printf("Digite a altura:\n");
    scanf("%f",&vetor[np].altura);
    printf("Digite a data de nascimento:\n");
    //Por que aqui(baixo) usa '&' e antes não(cima)?
    //Quando eu devo usar, quando é facultativo
    scanf("%d/%d/%d",&vetor[np].dtNas.dia,&vetor[np].dtNas.mes,&vetor[np].dtNas.ano);
    np++;
}
//2-list all names and their respective heights
void listarTodos(Pessoa vetor[], int nP){
    for(int i=0; i<nP; i++){
        printf("Nome: %s Altura: %.2f\n", vetor[i].nome, vetor[i].altura);
    }
}
//3- list the names of people who were born before a certain given date
void listarPorData(Pessoa vetor[], int nP, dataNascimento dt){
    printf("Digite a data desejada:\n");
    scanf("%d/%d/%d",&dt.dia, &dt.mes, &dt.ano);
    for(int i=0; i<nP; i++){
        if(dt.ano > vetor[i].dtNas.ano){
            printf("%s\n", vetor[i].nome);
        }else if(dt.ano == vetor[i].dtNas.ano && dt.mes > vetor[i].dtNas.mes){
            printf("%s\n", vetor[i].nome);
        } else if(dt.ano == vetor[i].dtNas.ano && dt.mes == vetor[i].dtNas.mes && dt.dia>vetor[i].dtNas.dia){
            printf("%s\n", vetor[i].nome);
        }
    }
}
