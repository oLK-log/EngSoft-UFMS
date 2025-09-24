#include <stdio.h>
//Program: contaRecursiva.cpp
//Programmer: Lorran Kaique
//Date: 21/09/25
int conta(int n, int w[], int k);
int main(){
    int n,k;
    scanf("%d", &n);
    int w[n];
    for(int i=0; i<n; i++){
        scanf("%d", &w[i]);
    }
    scanf("%d", &k);
    printf("%d", conta(n-1, w, k));
}
int conta(int n, int w[], int k){
    if(n==0){
        if(w[n] == k){
            return 1;
        }else{
            return 0;
        }
    }else{
        if(w[n]== k){
            return 1+ conta(n-1, w, k);
        }else{
            return conta(n-1, w, k);
        }
    }
}
