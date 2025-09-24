#include <stdio.h>
//Program: pisoLog.cpp
//Programmer: Lorran KAique
//Date: 11/09/25
int piso_log2(int n){
    if(n == 1){
        return 0;
    }else{
        return 1+ piso_log2(n/2);
    }
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%d", piso_log2(n));
}
