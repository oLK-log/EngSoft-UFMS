#include <stdio.h>
//Program: ackermann.cpp
//Programmer: Lorran Kaique
//Date: 11/09
int a(int m, int n){
    if(m==0){
        return n+1;
    }else{
        if(n ==0){
            return a(m-1, 1);
        }else{
            return a(m-1, a(m, n-1));
        }
    }
}
int main(){
    int m,n;
    scanf("%d %d", &m, &n);
    printf("%d", a(m, n));
}
