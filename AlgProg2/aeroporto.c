#include <stdio.h>
#define MAX 50
//program: aeroporto.java
//Programmer: Lorran Kaique
//Date: 02/09/25
/*This program is a simple menu with three options for manage a fly
has a 1-insert, 2- list all flights, 3-cancel flight*/
//define structs
struct aeroporto{
    char nome[100];
    int capacidade;
    int identificador;
};
struct voo{
    char nome[100];
    int identificador;
    int destino;
    int origem;
};
//Define functions
//insert airport
void inserirAeroporto(int n, struct aeroporto vetor[]){
    scanf("%s",vetor[n].nome);
    scanf("%d", vetor[n].capacidade);
    scanf("%d", vetor[n].identificador);
}

//1-Insert flight
void inserirVoo(int n, struct voo vetor[]){
    scanf("%s",vetor[n].nome);
    scanf("%d",vetor[n].origem);
    scanf("%d",vetor[n].destino);
    scanf("%d",vetor[n].identificador);
    printf("op 1");
}
//2-List all flight to a specific airport
void pesquisaAeroporto(int n, struct voo vetorVoo[]){
    int cod;
    scanf("%d", &cod);
    for(int i=0; i<n; i++){
        if(vetorVoo[i].origem == cod || vetorVoo[i].destino == cod){
            printf("s");
        }
    }

}
//3-Cancel flight
int main(){
//receive airport and flight number
    int qtd_aeroporto;
    scanf("%d", &qtd_aeroporto);

    int qtd_voos;
    scanf("%d",&qtd_voos);

//declare vectors

}


