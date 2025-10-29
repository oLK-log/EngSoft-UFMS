#include "../include/aeroporto.h"

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
