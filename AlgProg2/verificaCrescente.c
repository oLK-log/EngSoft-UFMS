#include <stdio.h>
//Program: verificaCrescente.c
//Programmer: Lorran Kaique
//Date: 26/08/25
/* This program receives an integer N and a vector of N positions.
It checks whether the elements of the vector are in ascending order
, and then prints true if so, and false otherwise.
*/
//0.1 declare function
int Ascending(int v[], int size);
int main(){
//Step 0. Inicialize abstractions
//0.2 variables
    int vectorSize;
//Step 1. Receive inputs
    scanf("%d",&vectorSize);
    int vector[vectorSize];
    for(int i=0; i<vectorSize; i++){
        scanf("%d", &vector[i]);
    }
//Step 2. Call function Ascending
    if(Ascending(vector, vectorSize)==0){
        printf("verdadeiro\n");
    }else{
        printf("falso");
    }
}
int Ascending(int vet[], int size){
    int previous = vet[0];
    for(int i=1; i<size; i++){
        if(previous >= vet[i]){
            return 1;
        }
        previous = vet[i];
    }
    return 0;

}
