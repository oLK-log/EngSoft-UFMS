#include <stdio.h>
//Funcoes
//tipo nome(parametros[tipo nome]){
    //}
//declaração de funções(protótipo de funcao
float maior(float num1, float num2);
void imprime1(int v[], int n);
void imprimir2(int v[5]);
void imprime3(int *v, int n);
void imprimeMatriz(int m[][4], int n);


int main(){
    float x,y,m;
    printf("Insira um valor:\n");
    scanf("%f", &x);
    printf("Insira um valor:\n");
    scanf("%f", &y);

    m = maior(x,y);
    printf("%.2f eh o maior\n", m);

    //func passando vetor como parametro
    int vet[5]={1,2,3,4,5};
    imprime1(vet,5);
    imprimir2(vet);
    imprime3(vet,5);
    printf("\n");

    //func passando matriz como parametro
    int mat[3][4] = {{1,2,3,4},{10,20,30,40},{91,101,111,121}};
    imprimeMatriz(mat, 3);
}
float maior(float num1, float num2){
    //essa func recebe dois n e retorna o maior entre eles
    if(num1>num2){
        return num1;
    }else{
        return num2;
    }
}
void imprime1(int v[], int n){
    int i;
    for(i=0;i<n;i++){
        printf("%d ", v[i]);
    }
    printf("\n");
}
void imprimir2(int v[5]){
    int i;
    for(i=0; i<5; i++){
        printf("%d ", v[i]);
    }
    printf("\n");
}
void imprime3(int *v, int n){
    int i;
    for(i=0; i<n; i++){
         printf("%d ", v[i]);
    }
    printf("\n");
}
//matriz
void imprimeMatriz(int m[][4], int n){
    int i, j;
    for(i=0; i<n; i++){
        for(j=0; j<4; j++){
            printf("%d ", m[i][j]);
        }
        printf("\n");
    }
}
