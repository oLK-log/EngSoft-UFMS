#include <stdio.h>
//Programa: somaImpar
//Programador: Lorran Kaíque
//Data: 12/08
/* Este programa le dois numeros inteiros(inicio, fim) e calcula a soma
dos numeros inteiros impares maiores ou iguais ao inicio e menores ou iguais
ao fim */
int main(void){
//Passo 0.Inicializar as variaveis
int start, end, i;
int sum = 0;
//Passo 1. Ler valores
scanf("%d %d", &start, &end);
//Passo 2. Percorrer os numeros
//Passo 2.1 Iniciar em ímpar
if (start % 2 == 0){
	start ++;
}
//Passo 2.2 somar os numeros impares
for(i=start; i<= end; i+=2){
	sum += i;
}
//Passo 3. Imprimir resultados
printf("%d\n", sum);

}
