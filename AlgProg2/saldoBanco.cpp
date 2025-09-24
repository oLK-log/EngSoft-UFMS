#include <stdio.h>
#include <ctype.h>
//Programa:
//Programador: Lorran Ka�que Silveira Fernandes
//Data: 07/08/25
/*Este programa calcula o saldo da conta corrente de
um cliente de um determinado banco. O programa l� o
cr�dito dispon�vel da conta corrente e a opera��o a
ser realizada, (D) para dep�sito ou (S) para saque, o
valor da opera��o e calcula o saldo ap�s a opera��o.*/
int main(){
//Passo 0. Inicializar variaveis
double saldoInicial;
double saldoFinal;
double valorOp;
char operacao;
//Passo 1. Ler as entradas
scanf("%lf %c %lf", &saldoInicial, &operacao, &valorOp);
//Passo 2. fazer calculo do saldo final
//Passo 2.1 Verificar se deposito
if (toupper(operacao) == 'D'){
	saldoFinal = saldoInicial + valorOp;
//Passo 2.2 Se nao for deposito
}else{
	saldoFinal = saldoInicial - valorOp;
}
//Passo 3. Imprimir
printf("Saldo atual: R$%+10.2f",saldoFinal);
}
