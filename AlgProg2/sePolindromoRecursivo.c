#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#define MAX 100
//Program: sePolindromoRecursivo.cpp
//Programmer: Lorran Kaique
//Date: 21/09
//This program check if the word is Polindromo
bool palindromo(char palavra[], int inicio, int fim);
int main(){
    char palavra[MAX];
    scanf("%[^\n]", palavra);
    int tamPalavra = strlen(palavra);
    bool result = palindromo(palavra, 0, tamPalavra-1);
    if(result){
        printf("É um palíndromo.\n");
    }else{
        printf("Não é um palíndromo.\n");
    }
}
bool palindromo(char palavra[], int inicio, int fim){
    if(inicio >= fim){
        return true;
    }else if(palavra[inicio]!=palavra[fim]){
        return false;
    }else{
        return palindromo(palavra, inicio+1, fim-1);
    }
}
