#include <stdio.h>
//Programa: multiMatriz
//Programador: Lorran Kaique
//Data: 24/08
/* Esse programa le uma matriz A e um vetor B, e entao calcula a multiplicacao
de A e B, que e a matriz C*/
int main(){
//Passo 0. Inicializar abstracoes
//Passo 0.1 Inicializar variaveis
//entradas: int m,n; elementos matriz A; elementos vetor
    int m,n;
//Passo 1 Ler valores
//Passo 1.1 Ler mxn elementos da matriz
    scanf("%d %d", &m, &n);
//Passo 1.2 Inicializar e ler matriz
    int matriz[m][n];//m linha e n coluna
    for(int i =0; i<m;i++){
        for(int j = 0; j<n; j++){
            scanf("%d", &matriz[i][j]);
        }
    }
//Passo 1.3 Inicializar e ler vetor
    int vetor[n];
    for(int i =0; i<n; i++){
        scanf("%d", &vetor[i]);
    }
//Passo 2. gerar multiplicacao/ vetor c
//vetorC[j] = somatorio(a[i][j]*b[j])
    int vetorC[m];
//Passo 2.1 Limpar lixo
    for(int i=0; i<m; i++){
        vetorC[i] = 0;
    }
//Calcular vetorC
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            vetorC[i]+= matriz[i][j]*vetor[j];
        }
    }
//Passo 3. Imprimir resultado(vetorC)
    for(int i = 0; i<m; i++){
        printf("%d ",vetorC[i]);
    }


}
