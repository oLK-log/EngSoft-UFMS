#include <stdio.h>
/* Este programa calcula a media final da disciplina de AlgProg1 em que 75% da nota
e dada por meio de 3 provas e 25% por meio de 2 trabalhos. A entrada são 5 numeros reais
e a saida são as notas e suas respectivas medias */
//variaveis
//float n1,n2,n3,t1,t2,mp,mt,mf
int main(){
//Passo 0. Inicializar as variaveis
	double n1,n2,n3,t1,t2,mp,mt,mf;
//Passo 1. Ler entradas(notas)
	scanf("%lf",&n1);
	scanf("%lf",&n2);
	scanf("%lf",&n3);
	scanf("%lf",&t1);
	scanf("%lf",&t2);
//Passo 2. Calcular medias
//Passo 2.1 Calcular medias provas
	mp = (n1+n2+n3)/3;
//Passo 2.2 Calcular medias trabalho
	mt = (t1+t2)/2;
//Passo 2.3 Calcular media final
	mf = mp*0.75 + mt*0.25;
//Passo 3. Imprimir resultados
	printf("======= NOTAS ========\n");
	printf("Primeira Prova    %4.1f\n",n1);
	printf("Segunda Prova     %4.1f\n",n2);
	printf("Terceira Prova    %4.1f\n",n3);
	printf("Média Provas      %4.1f\n\n",mp);
	printf("Primeiro Trabalho %4.1f\n",t1);
	printf("Segundo Trabalho  %4.1f\n",t2);
	printf("Média Trabalhos   %4.1f\n",mt);
	printf("----------------------\n");
	printf("Média Final       %4.1f\n",mf);
	
}
