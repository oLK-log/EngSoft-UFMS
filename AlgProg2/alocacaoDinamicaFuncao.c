#include <stdio.h>
#include <stdlib.h>

int** alocacaoMatriz(int m, int n);
int ** desalocaMatriz(int m, int **matriz);
void leitura(int m, int n, int **mat);
void impressao(int m, int n, int **mat);

int main(){
    int **matriz;
    int m,n;

    scanf("%d %d", &m, &n);

    matriz = alocacaoMatriz(m, n);
    if(matriz == NULL){
        printf("Erro de alocacao de memoria.\n");
        return 0;
    }
    leitura(m, n, matriz);

    printf("Matriz:\n");
    impressao(m, n, matriz);

    //desalocacao
    matriz = desalocaMatriz(m, matriz);
    return 0;
}
int** alocacaoMatriz(int m, int n){
    int **A;
    int i;

    A = (int **) calloc(m, sizeof(int *));
    if(A == NULL){
        return NULL;
    }
    for(i = 0; i<m; i++){
        A[i] = (int *) calloc(n, sizeof(int));
        if(A[i] == NULL){
            return NULL;
        }
    }
    return A;
}

int** desalocaMatriz(int m, int **matriz){
    int i;
    for(i = 0; i<m; i++)
        free(matriz[i]);
    free(matriz);
    return NULL;
}

void leitura(int m, int n, int **mat){
    int i, j;
    for(i = 0; i < m; i++)
    for(j =0; j<n; j++){
        scanf("%d", &mat[i][j]);
    }
}

void impressao(int m, int n, int **mat){
    int i, j;
    for(i =0; i<m; i++){
        for(j=0; j<n; j++){
            printf("%d ", mat[i][j]);
        }
        printf("\n");
    }
}
