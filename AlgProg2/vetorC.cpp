#include <stdio.h>
#define MAX 50
//Program: vetorC.cpp
//Programmer: Lorran Kaique
//Date: 11/09/25
void CreatevetorC(int a[], int b[],int c[], int n){
    if(n==0){
        c[n]=a[n];
    }else{
        if(n%2!=0){
            c[n]=b[n];
        }
        CreatevetorC(a,b,c,n-1);
        c[n]=a[n];
        c[n]=b[n];
    }

}
int main(){
   int a[MAX];
   int b[MAX];
   int c[MAX*2];
   int n;
   scanf("%d", &n);
   for(int i=0; i<n; i++){
    scanf("%d", &a[i]);
   }
   for(int i=0; i<n; i++){
    scanf("%d", &b[i]);
   }
   for(int i=0; i<n*2; i++){
    printf("%d ", c[i]);
   }

}
