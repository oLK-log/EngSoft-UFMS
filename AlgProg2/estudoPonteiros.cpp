#include <stdio.h>
#define MAX 100
//EStudo Ponteiros
void min_max1(int n, int v[], int &maxi, int &mini);

void min_max(int n, int v[], int *maxi, int *mini);

int main(){
    /*int i, *p;
    p = &i;
    scanf("%d",&i);
    printf("Conteudo de i/ *p = %d\n",*p);
    printf("Endereco de i/ conteudo de p= %d\n", p);
    printf("Endereco de p = %d\n", &p);
    */
    int n, maxi, mini;
    int *ma = &maxi;
    int *mi = &mini;
    scanf("%d", &n);
    int vetor[n];
    for(int i=0; i<n;i++){
        scanf("%d", &vetor[i]);
    }
    min_max(n, vetor, ma, mi);
    printf("Max=%d Min=%d \n", maxi, mini);
    min_max1(n, vetor, maxi, mini);
    printf("Max=%d Min=%d \n", maxi, mini);
}
void min_max1(int n, int v[], int &maxi, int &mini){
    maxi = v[0];
    mini = v[0];
    for(int i=1; i<n; i++){
        if(maxi<v[i]){
            maxi=v[i];
        }
        if(mini>v[i]){
            mini=v[i];
        }
    }
}
void min_max(int n, int v[], int *ma, int *mi){
    *ma = v[0];
    *mi = v[0];
    for(int i=1; i<n; i++){
        if(*ma<v[i]){
            *ma=v[i];
        }
        if(*mi>v[i]){
            *mi=v[i];
        }
    }
}
