#include <stdio.h>
#include <string.h>
#define MAX 20
//Program: graoIdeal.cpp
//Programmer: Lorran Kaique
//Date: 08/09/25
/* This program receives data from three grains.
Then, it calculates and prints the ideal grain.
To decide which is ideal, compare the type(A>B>C);
If they are same, receive a quatify and choice a small price(quantify*PricePerUnid).
*/
//Declare struct
struct Grao{
    char nome[MAX+1];
    char tipo;
    float peso;
    float precoKG;
    int quantidade;
};
//declare functions
int melhorGrao(Grao graos[]);
void lerStruct(Grao graos[]);
//MAin program
int main(){
    Grao graos[MAX+1];
    lerStruct(graos);
    int indice = melhorGrao(graos);
    printf("O grão ideal é o/a %s", graos[indice].nome);

}
int melhorGrao(Grao graos[]){
        int indice=0;
        for(int i=0; i<3; i++){
            if(graos[i].tipo<graos[indice].tipo){
                indice = i;
            }else if(graos[i].tipo == graos[indice].tipo){
                scanf("%d", &graos[indice].quantidade);
                scanf("%d", &graos[i].quantidade);
                if(graos[i].precoKG* graos[i].quantidade < graos[indice].precoKG * graos[indice].quantidade){
                    indice=i;
                }
            }
        }
        return indice;
}
void lerStruct(Grao graos[]){
    for(int i=0; i<3; i++){
        scanf(" %s", graos[i].nome);
        scanf(" %c", &graos[i].tipo);
        scanf("%f", &graos[i].peso);
        scanf("%f", &graos[i].precoKG);
    }
}
