/*
    Programa exemplo/estudo fornecido na materia de Algoritmos e Programacao 2 da Universidade Federal
    de Mato Grosso do Sul

    ESSE PROGRAMA INPLEMENTA A ORDENACAO POR MERGESORT
*/

//#include <iostream>
#include <stdio.h>

#define MAX 50

void intercala(int p, int q, int r, int v[MAX]){
    int i,j,k, w[MAX];

    i=p; j=q; k=0;
    while(i < q && j<r){
        if(v[i] < v[j]){
            w[k] = v[i]; i++;
        }else{
            w[k] = v[j]; j++;
        }
        k++;
    }
    while(i < q){
        w[k] = v[i]; i++; k++;
    }
    while(j < r){
        w[k] = v[j]; j++; k++;
    }
    for(i = p; i < r; i++){
        v[i] = w[i - p];
    }
}

void mergeSort(int p, int r, int v[MAX]){//r=tamanho; p= posicao inicial
    int q;
    if(p < r - 1){
        q = (p + r)/2;
        printf("\nEntra no merge1 p=%d q=%d e o vetor\n Entra no merge2 q=%d r=%d e o vetor\n", p, q, q, r);
        mergeSort(p, q, v);
        mergeSort(q, r, v);
        printf("Entra no intercala %d %d %d e o vetor\n", p, q, r);
        intercala(p, q, r, v);
    }
    printf("\n");
}

int main()
{
    int i, tam;
    int v[MAX];

    printf("Digite o tamanho do vetor:\n");
    scanf("%d", &tam);

    printf("Digite os valores do vetor:\n");

    for(i = 0; i<tam; i++){
        scanf("%d", &v[i]);
    }

    mergeSort(0, tam, v);

    for(int i=0; i<tam; i++){
        printf("%d", v[i]);
    }
    printf("\n");
    return 0;
}
