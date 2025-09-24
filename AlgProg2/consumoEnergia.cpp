#include <stdio.h>
#define MAX 15
//Program: consumoEnergia.cpp
//Programmer: Lorran Kaique
//Date: 08/09/25
/* This program receives 5 data(name, wattage, timeActive) from home
appliances and the relative consumption
time of a house.
It calculates and prints the total and relative consumption of each appliance.
*/
//Starting abstractions
struct Eletro{
    char name[MAX+1];
    float wattage;
    float timeActive;
};
//Declare functions
void readEletros(Eletro eletro[]);
float calcTotalDia(Eletro eletro[], int n);
void calcRelative(Eletro eletro[], int n,float total);
//Initialize main program
int main(){
    int time;
    float totalExpenditure;
    int n =5;
    Eletro eletro[MAX+1];
    readEletros(eletro);
    scanf("%d", &time);
    totalExpenditure = time * calcTotalDia(eletro, n);
    printf("%.2f\n",totalExpenditure);
    calcRelative(eletro, n, totalExpenditure);

}
//Create functions
void readEletros(Eletro eletro[]){
    for(int i=0; i<5; i++){
        scanf(" %[^\n]", eletro[i].name);
        scanf("%f", &eletro[i].wattage);
        scanf("%f", &eletro[i].timeActive);
    }
}
float calcTotalDia(Eletro eletro[], int n){
        if(n==0){
            return eletro[0].wattage * eletro[0].timeActive;
        }else{
            return eletro[n].wattage * eletro[n]. timeActive + calcTotalDia(eletro, n-1);
        }
}
void calcRelative(Eletro eletro[], int n, float total){
    for(int i=0; i<n; i++){
        printf("%.2f\n", (((eletro[i].wattage * eletro[i]. timeActive * 30)/total) *100) );
    }
}
//x/29175 = 5.14
