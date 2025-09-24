#include <stdio.h>

int main(){
	/* //If Else
	float m;
	
	printf("Insira a nota:\n");
	scanf("%f", &m);
	
	if (m >= 7){
		printf("Aprovado(a)!\n)");
	}
	elif(m >= 4.0 && m < 7.0){
		printf("Tem direito a exame\n");
	}
	else{
		printf("Reprovado!\n");
	}
	*/
	
	/*
	//Switch
	
	int d;
	
	printf("Insira um valor de 1 a 7:\n");
	scanf("%d", &d);
	
	switch(d){
		case 1:
			printf("Domingo.\n");
			break;
		case 2:
			printf("Segunda.\n");
			break;
		case 3:
			printf("Terça.\n");
			break;
		case 4:
			printf("Quarta.\n");
			break;
		case 5:
			printf("Quinta.\n");
			break;
		case 6:
			printf("Sexta.\n");
			break;
		case 7:
			printf("Sabado.\n");
			break;
	}
	*/
	/*
	//while
	int i = 1;
	
	while(i <=10){
		printf("%d \n",i);
		i++;
	}
	*/
	/*
	// Do While
	int i=1;
	do{
		printf("%d ",i);
		i++;
	}while(i <= 10);
	*/
	
	//for
	int i;
	for(i=1; i<=10; i++){
		printf("%d ", i);
	}
	printf("\n");
	//Break and Continue
	
	for(i=1; i<10; i++){
		printf("%d ", i);
		
		if(i == 5){
			break;
		}
	}
	printf("\n");
	
	for(i=1; i<=10; i++){
		if(i == 5){
			continue;
		}
		
		printf("%d ", i);
	}
	
} 
