#include "include/aeroporto.h"

int main(){
    int nvoo=0;
//receive airport and flight number
    int qtd_aeroporto;
    scanf("%d", &qtd_aeroporto);

    int qtd_voos;
    scanf("%d",&qtd_voos);

//declare vectors
    Aeroporto aero[qtd_aeroporto+1];
    Voo voo[qtd_voos+1];
//receive data from the airport
    for(int i=0; i<qtd_aeroporto;i++){
        //printf("%d:\n", i);
        inserirAeroporto(i, aero);
    }
//go to menu
    int op;
    do {
        op = menu();
        if (op==1){
            inserirVoo(nvoo, voo);


        }else if(op==2){
            pesquisaAeroporto(qtd_voos, voo, qtd_aeroporto, aero);
        }else if(op==3){
            cancelarVoo(voo, qtd_voos);
        }
    }while (op!=0);

}
