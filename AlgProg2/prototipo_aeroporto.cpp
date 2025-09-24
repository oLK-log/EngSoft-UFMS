#include <stdio.h>
#include <string.h>

struct aeroporto{

	char nome[100];
	int capacidade;
	int identificador;
};

struct voo{

	char nome[100];
	int identificador;
	int destino;
	int origem;
};


int main(){


	int qtd_aeroporto;
	scanf(" %d", &qtd_aeroporto);

	int qtd_voos;
	scanf(" %d", &qtd_voos);

	/*declarar vetores*/

	/*ler os aeroportos */


	int j=0;
	int op;

	do{


		scanf(" %d", &op);

		if(op == 1){// Adicionar Voo (orgiem e destino)

			printf("op 1 \n");

		}else if (op == 2){// Consultar todos os Voos de origem ou destino de determinado aeroporto pelo ID, se tiver cancelado deve mostrar;

			printf("op 2 \n");

		}else if (op == 3){// Cancelar Voo pelo ID

			printf("op 3 \n");


	}while(op != 0);



	return 0;
}
