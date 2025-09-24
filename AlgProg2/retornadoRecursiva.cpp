#include <stdio.h>
//Program: retornadoRecursiva.cpp
//Programmer: Lorran KAíque
//Date: 21/09/25
int f1(int x){
    if (x==1){
        return -x;
    }else{
        return -5* f1(x-1)+x;
    }
}
int main(){
    int x=4;
    printf("%d\n",f1(x));
}
