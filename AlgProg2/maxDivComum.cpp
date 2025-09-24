#include <stdio.h>
//Program: maxDivComum.cpp
//Programmer: Lorran KAique
//Date: 11/09/25
/* This program calculetes the mdc of two numbers*/
int mdc(int a, int b){
    if(a%b == 0){
        return b;
    }else{
        return mdc(b, a%b);
    }
}
int main(){
    int a,b;
    scanf("%d %d", &a, &b);
    printf("%d",mdc(a,b));
}
