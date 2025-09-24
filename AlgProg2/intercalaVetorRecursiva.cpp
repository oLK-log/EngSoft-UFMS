#include <stdio.h>
#define MAX 50
//Program: intercalaVetorRecursiva.cpp
//Programmer: Lorran KAique
//Date: 21/09/25
void intercala(int vetorA[], int vetorB[],int vetorC[], int n, int controle, int controleC);
int main(){
    int n;
    int controle=0;
    int controleC = 0;
    scanf("%d", &n);
    int vetorA[n], vetorB[n], vetorC[n+n];
    for(int i=0; i<n; i++){
        scanf("%d", &vetorA[i]);
    }
    for(int i=0; i<n; i++){
        scanf("%d", &vetorB[i]);
    }

    intercala(vetorA, vetorB, vetorC, n*2, controle, controleC);
    for(int i=0; i<n*2; i++){
        //printf("pos[%d] = %d \n", i, vetorC[i]);
        printf("%d ", vetorC[i]);
    }



}
void intercala(int vetorA[], int vetorB[],int vetorC[], int n, int controle, int controleC){
    if(controle == n){
        return;
    }else if(controleC%2==0){
        vetorC[controleC] = vetorA[controle];
        return intercala(vetorA, vetorB, vetorC,n, controle, ++controleC);
    }else{
        vetorC[controleC] = vetorB[controle];
        return intercala(vetorA, vetorB, vetorC, n, ++controle, ++controleC);
    }
}
