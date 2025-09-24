#include <stdio.h>
#include <stdbool.h>
//Program: seTrianguloRet.c
//Programmer: Lorran Kaique
//Date: 26/08/25
/* This program receives three double values A,B C than is
sides of a triangule. If the values form a right triangle, the
program displays "formam um tri�ngulo ret�ngulo", otherwise "n�o
formam um tri�ngulo ret�ngulo"
*/
//0.2 declare function
bool testTri(double a, double b, double c);
int main(){
//Step 0. Inicialize abstractions
//0.1 Start variables
    double a,b,c;
//Step 1. receives input
    scanf("%lf %lf %lf",&a, &b, &c);
//Step 2. check if right triangle and print
    if(testTri(a,b,c)){
        printf("%.1lf %.1lf %.1lf formam um tri�ngulo ret�ngulo",a,b,c);
    }else{
        printf("%.1lf %.1lf %.1lf n�o formam um tri�ngulo ret�ngulo", a,b,c);
    }
}
bool testTri(double a,double b, double c){
    if(a*a+b*b == c*c){
        return true;
    }else{
        return false;
    }
}
