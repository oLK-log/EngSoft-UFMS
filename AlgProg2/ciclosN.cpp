#include <stdio.h>
//Program: ciclosN.cpp
//Programmer: Lorran
//Date: 11/09/25
int ciclo(int n){
    printf("%d ", n);
    if(n == 1){
        return 1;
    }else{
        if(n%2 == 0){
            return 1 + ciclo(n/2);
        }else {
            return 1 + ciclo(n*3+1);
        }
    }
}
int main(){
    int n;
    scanf("%d", &n);
    printf("%d", ciclo(n));
}
