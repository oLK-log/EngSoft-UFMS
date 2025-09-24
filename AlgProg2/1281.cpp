#include <stdio.h>
#include <string.h>
#define MAX 50
//Program: 1281.cpp
//Programmer: Lorran Kaique
//Date: 09/09/25
/* This program receives an integer N that indicates the number of test cases, and for each
test case an integer M that indicates the number of <fruits values> to
be received.
The first input line contains an integer N, which represents the number of trips to Dona Parcinova's market (which is simply the
number of test cases that follow). Each test case begins with an integer M, which represents the number of products available for
sale at the market. The M products follow with their respective prices per unit or kg. The next input line contains an
integer P (1 ≤ P ≤ M), which represents the quantity of different products Dona Parcinova wishes to purchase.
P lines follow, each containing text (up to 50 characters) and an integer value, which indicate the name of each
product and the quantity of that product, respectively. */
struct AvailableBuy{
    char name[MAX+1];
    double price;
};
struct Purchased{
    char name[MAX+1];
    int quantify;
};
void readAvailableBuy(AvailableBuy listAvailableBuy[], int qtdProducts);
void readBuy(Purchased listBuy[], int qtdProducts);
double purchaseCust(Purchased listBuy[], AvailableBuy listAvailableBuy[], int qtdProductsBuy, int qtdProductsAvailable);

int main(){
    int testCases;
    //read number of test cases
    scanf("%d", &testCases);
    //printf("LEu o numero de casos teste\n");
    for(int i=0; i<testCases; i++){
        int qtdProductsAvailable;
        scanf("%d", &qtdProductsAvailable);
        AvailableBuy listAvailableBuy[qtdProductsAvailable];
        //printf("Leu o numero de produtos disponiveis\n");
        readAvailableBuy(listAvailableBuy,qtdProductsAvailable);

        int qtdProductsBuy;
        scanf("%d", &qtdProductsBuy);
        Purchased listBuy[qtdProductsBuy];
        //printf("Leu o numero de produtos comprados: %d\n", qtdProductsBuy);
        readBuy(listBuy, qtdProductsBuy);
        printf("R$ %.2f\n", purchaseCust(listBuy, listAvailableBuy, qtdProductsBuy, qtdProductsAvailable));
    }

}

void readAvailableBuy(AvailableBuy listAvailableBuy[], int qtdProducts){
    for(int i=0; i<qtdProducts; i++){
        scanf(" %s %lf", listAvailableBuy[i].name, &listAvailableBuy[i].price);
        //printf("Imprimindo valor da posicao %d %s %.2lf\n", i, listAvailableBuy[i].name, listAvailableBuy[i].price);
    }
}
void readBuy(Purchased listBuy[], int qtdProducts){
    for(int i=0; i<qtdProducts; i++){
        scanf(" %s %d", listBuy[i].name, &listBuy[i].quantify);
        //printf("pos %d produto %s em qts %d\n", i, listBuy[i].name, listBuy[i].quantify);
    }
}
double purchaseCust(Purchased listBuy[], AvailableBuy listAvailableBuy[], int qtdProductsBuy, int qtdProductsAvailable){
    double totalCost=0;
    for(int i=0; i<qtdProductsAvailable; i++){
        for(int j=0; j<qtdProductsBuy; j++){
            if(strcmp(listAvailableBuy[i].name, listBuy[j].name)==0){
                totalCost+= listAvailableBuy[i].price*listBuy[j].quantify;
            }
        }
    }
    return totalCost;
}
