#include <stdio.h>
#define linhas 3
#define colunas 3
#define MAX 10

int max(int n, int v[MAX]);

int main(){
    /*
    int *p, cont = 0;
    int A[linhas][colunas];

    for(p = &A[0][0]; p <= &A[linhas-1][colunas-1]; p++){
        *p = cont;
        cont++;
    }
    cont = 1;
    for(p = &A[0][0]; p <= &A[linhas-1][colunas-1]; p++){
        printf("%d ", *p);
        if(cont % 3 == 0){
            printf("\n");
        }
        cont ++;
    }
    */

    int A[linhas][colunas] = {0}, *p, i, cont = 0;
    printf("Digite a linha: ");
    scanf("%d", &i);
    for(p = A[i] ; p < A[i] + colunas; p++){
        *p = cont;
        cont++;
    }
    printf("\nlinha %d = ",i);
    for(p = A[i] ; p < A[i] + colunas; p++){
        printf("%d ", *p);
    }
    printf("\n");
    cont = 1;
    for(p = &A[0][0]; p <= &A[linhas-1][colunas-1]; p++){
        printf("%d ", *p);
        if(cont % 3 == 0){
            printf("\n");
        }
        cont ++;
    }

    printf("\nO max da linha %d = %d", i, max(colunas, A[i]));
}

int max(int n, int v[MAX]){
    int i, maior;
    maior = v[0];
    for( i = 1; i < n; i++){
        if (v[i] > maior){
             maior = v[i];
        }
    }
    return maior;
}
