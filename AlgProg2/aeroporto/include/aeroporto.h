#include <stdio.h>
#include <string.h>

#define MAX 50

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

void inserirAeroporto(int n, Aeroporto vetor[]);
void inserirVoo(int &n, Voo vetor[]);
void pesquisaAeroporto(int v, Voo vetorVoo[], int a, Aeroporto vetorAero[]);
void cancelarVoo(Voo vetor[], int v);
int menu();
