#include <stdio.h>
//Program: potencia.cpp
//Programmer: Lorran Kaique
//DAte 11/09/25
int potencia(int x, int n){
    if(n == 0){
        return 1;
    }else{
        return x* potencia(x, n-1);
    }
}

int main(){
    int x,n;
    scanf("%d %d", &x, &n);
    printf("%d\n", potencia(x, n));
}
