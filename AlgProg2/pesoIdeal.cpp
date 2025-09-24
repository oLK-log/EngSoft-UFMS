#include <stdio.h>
//Programa: pesoIdeal.cpp
//Programador: Lorran Kaíque
//Data: 08/08/25
/*Este programa a partir de um valor real de altura e sexo, calcula o peso
ideal utilizando a formula:
para H- (72.7*h)-58
para M- (62,1*h)-44,7
*/
int main(){
//PAsso 0. Declarar variaveis
float altura;
float pesoIdeal;
char sexo;
//Passo 1.Ler os valores
printf("Altura:\n");
scanf("%f",&altura);
printf("Sexo:\n");
scanf(" %c",&sexo);
//Passo 2. Verificar se H ou M
if(sexo == 'M' || sexo == 'm'){
	pesoIdeal = (72.7*altura)-58;
}
else{
	pesoIdeal = (62.1*altura)-44.7;	
}
//Passo 3. Imprimir resultados
printf("Peso ideal: %.2f\n",pesoIdeal);
}
