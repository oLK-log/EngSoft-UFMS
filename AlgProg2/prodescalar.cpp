/*
Escreva uma funcao que recebe dois vetores de inteiros com n (n <= 20) elementos como entrada,
calcula e retorna o valor do produto escalar entre eles. Utilize aritmetica de ponteiros
 para percorrer o vetor. Nao utilize indices em qualquer parte do programa. Exemplo:

n = 5
v1 = <2, 3, 4, 0, -1>
v2 = <1, 2, 1, -1, 1>
Saida:
valor = 2*1 + 3*2 + 4*1 + 0*-1 + -1*1 =
      = 2   + 6   + 4   + 0    - 1
      = 11
Crie uma funcao para ler um vetor de tamanho n, com o prototipo abaixo:
void leitura(int n, int *v);
Crie uma funcao para calcular e retornar o produto escalar entre dois vetores de tamanho n, com o prototipo
abaixo:

int prodescalar(int n, int *v1, int *v2); // int v1[MAX], int v2[MAX]
*/
#include<stdio.h>
#define MAX 20


void leitura(int n, int *v);

int  prodescalar(int n, int *v1, int *v2);


int main()
{
    int n, v1[MAX], v2[MAX];
    int soma;


    scanf("%d", &n);
    /*leitura de n e dos elementos do vetor*/
    printf("Leitura do vetor 1: \n");
    leitura(n, v1);

    printf("Leitura do vetor 2: \n");
    leitura(n, v2);
    /*produto escalar - chamada da funcao*/
    soma = prodescalar(n, v1, v2);

    printf("Prod escalar: %d\n", soma);

    /*saida */

    return 0;
}
/*funcao le um vetor usando um ponteiro para acessar as posicoes*/
void leitura(int n, int *v){
    for(int i=0; i<n; i++){
        scanf("%d", v+i);
    }
}

/*funcao calcula e retorna o produto escalar entre dois vetores*/
int  prodescalar(int n, int *v1, int *v2){
    if(n==0){
        return *(v1+n)* *(v2+n);
    }else{
        return (*(v1+n)* *(v2+n)) + prodescalar(n-1, v1, v2);
    }
}



