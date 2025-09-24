#include <stdio.h>
#include <string.h>
#define MAX 50
//program: aeroporto.java
//Programmer: Lorran Kaique
//Date: 02/09/25
/*This program is a simple menu with three options for manage a fly
has a 1-insert, 2- list all flights, 3-cancel flight*/
//define structs
struct Aeroporto{
    char nome[100];
    int capacidade;
    int identificador;
};
struct Voo{
    char nome[100];
    int identificador;
    int destino;
    int origem;
    char status[100];
};
//prototype functions
void inserirAeroporto(int n, Aeroporto vetor[]);
void inserirVoo(int &n, Voo vetor[]);
void pesquisaAeroporto(int v, Voo vetorVoo[], int a, Aeroporto vetorAero[]);
void cancelarVoo(Voo vetor[], int v);
int menu();

int main(){
    int nvoo=0;
//receive airport and flight number
    int qtd_aeroporto;
    scanf("%d", &qtd_aeroporto);

    int qtd_voos;
    scanf("%d",&qtd_voos);

//declare vectors
    Aeroporto aero[qtd_aeroporto+1];
    Voo voo[qtd_voos+1];
//receive data from the airport
    for(int i=0; i<qtd_aeroporto;i++){
        //printf("%d:\n", i);
        inserirAeroporto(i, aero);
    }
//go to menu
    int op;
    do {
        op = menu();
        if (op==1){
            inserirVoo(nvoo, voo);


        }else if(op==2){
            pesquisaAeroporto(qtd_voos, voo, qtd_aeroporto, aero);
        }else if(op==3){
            cancelarVoo(voo, qtd_voos);
        }
    }while (op!=0);

}

//Define functions
int menu(){
    int op;
    scanf("%d", &op);
    return op;
}
//insert airport
void inserirAeroporto(int n, Aeroporto vetor[]){
    scanf(" %[^\n]",vetor[n].nome);
    //printf("%s\n",vetor[n].nome);
    scanf("%d", &vetor[n].capacidade);
    //printf("%d\n", vetor[n].capacidade);
    scanf("%d", &vetor[n].identificador);
    //printf("%d\n", vetor[n].identificador);

}

//1-Insert flight
void inserirVoo(int &n, Voo vetor[]){
    printf("op 1\n");
    scanf("%s",vetor[n].nome);
    //printf("%s", vetor[n].nome);
    scanf("%d",&vetor[n].origem);
    //printf("%d", vetor[n].origem);
    scanf("%d",&vetor[n].destino);
    //printf("%d", vetor[n].destino);
    scanf("%d",&vetor[n].identificador);
    //printf("%d", vetor[n].identificador);
    n++;
}
//2-List all flight to a specific airport
void pesquisaAeroporto(int v, Voo vetorVoo[], int a, Aeroporto vetorAero[]){
    printf("op 2\n");
    int cod;
    scanf("%d", &cod);
    for(int i=0; i<a; i++){
        if(vetorVoo[i].origem == cod || vetorVoo[i].destino == cod){
            printf("%s", vetorVoo[i].status);
            if(strcmp(vetorVoo[i].status, "Cancelado") == 0){
                printf("%s - %s - %d - %d\n",vetorVoo[i].status, vetorVoo[i].nome, vetorVoo[i].origem, vetorVoo[i].destino);
            }else{
                printf("%s - %d - %d\n",vetorVoo[i].nome, vetorVoo[i].origem, vetorVoo[i].destino);
            }
        }
    }
}
//3-Cancel flight
void cancelarVoo(Voo vetor[], int v){
    printf("op 3\n");
    int nVoo;
    scanf("%d", &nVoo);
    for(int i=0; i<v-1; i++){
        if(vetor[i].identificador == nVoo){
            //printf("copiando");
            strcpy(vetor[i].status,"Cancelado");
            break;
        }
    }
}
