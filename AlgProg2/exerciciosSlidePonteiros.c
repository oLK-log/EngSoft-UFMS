//Qual o conteudo do vetor v após a execucao dp seguinte trecho de codigo
#include <stdio.h>
#define N 10
int main (){
    int v[N] = {1,2,3,4,5,6,7,8,9,10};
    int *p = &v[0], *q = &v[N - 1], temp, cont = 0;

    while (p < q) {
        //troca os valores para quais o p e q apontam, mandando o p para frente o q pra tras(vao se aproximando)
        printf("Iteracao %d, temp = %d, *p = %d, *q = %d\n", cont, temp, *p, *q);
        temp = *p;
        *p++ = *q;
        *q-- = temp;
        cont ++;
    }

    printf("Iteracao %d, temp = %d, *p = %d, *q = %d\n", cont, temp, *p, *q);
    int *ptr;
    printf("\n Imprimindo Vetor\n");
    for(ptr = v; ptr < N+v; ptr++){
        printf("Endereco %p Valor %d\n", ptr, *ptr);
    }

    free(ptr);
    free(p);
    free(q);

}
