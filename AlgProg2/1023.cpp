#include <stdio.h>
#include <string.h>
#include <math.h>
#define MAX 106
#define MAX2 200
//Program: 1023.cpp
//Programmer: Lorran Kaique
//Date: 10/09/25
struct Property{
    int numberResidents;
    double totalConsumption;
    int consPerPerson;
};
struct City{
    int numberProperties;
    Property property[MAX2+1];
    double averageConsumption;
};
void readValues(int &controler, City cities[], int numberCities);
void calcAverageCities(City cities[], int numberCities);
void orderConsPerPerson(City cities[], int numberCities);
void printGroupedConsumption(City cities[], int numberCities);
int main(){
    City cities[MAX+1];
    int numberCities = 0;
    int controler = 0;
    while(controler == 0){
        readValues(controler, cities, numberCities);
        if(controler == 0){
            printf("Cidade# %d:\n", numberCities+1);
            //orderConsPerPerson(cities, numberCities);
            printGroupedConsumption(cities, numberCities);
            calcAverageCities(cities, numberCities);
            numberCities++;
            printf("\n");
        }
    };
}

void orderConsPerPerson(City cities[], int numberCities){
    int propertyCount = cities[numberCities].numberProperties;
    if(propertyCount == 0)return;
    int vetor[propertyCount];
    int vetorPessoas[propertyCount];
    for (int i = 0; i < propertyCount; i++) {
        vetor[i] = cities[numberCities].property[i].consPerPerson;
        vetorPessoas[i] = cities[numberCities].property[i].numberResidents;
    }
    for( int i=0; i< propertyCount -1; i++){
        for(int j=0; j< propertyCount - i -1; j++){
            if(vetor[j]>vetor[j+1]){
                int aux = vetor[j];
                vetor[j] = vetor[j+1];
                vetor[j+1] = aux;
                int auxPes = vetorPessoas[j];
                vetorPessoas[j] = vetorPessoas[j+1];
                vetorPessoas[j+1] = auxPes;
            }
        }
    }
    for(int i=0; i< propertyCount; i++){
        printf("%d-%d", vetorPessoas[i], vetor[i]);
        if(i<propertyCount-1){
                printf(" ");
        }
    };
    printf("\n");
}
void calcAverageCities(City cities[], int numberCities){
    double sumConsumption=0.0;
    double sumPeople=0;
    for(int i=0; i < cities[numberCities].numberProperties; i++){
        sumConsumption+= cities[numberCities].property[i].totalConsumption;
        sumPeople+= cities[numberCities].property[i].numberResidents;
    }
    double trucatedAve = floor((sumConsumption/sumPeople)*100) / 100.0;
    cities[numberCities].averageConsumption = trucatedAve;
    printf("Consumo medio: %.2f m3.\n", cities[numberCities].averageConsumption);
}
void readValues(int &controler, City cities[], int numberCities){
    scanf("%d",&cities[numberCities].numberProperties);
    if(cities[numberCities].numberProperties!=0){
        for(int i=0; i<cities[numberCities].numberProperties; i++){
            scanf("%d %lf", &cities[numberCities].property[i].numberResidents, &cities[numberCities].property[i].totalConsumption);
            cities[numberCities].property[i].consPerPerson = cities[numberCities].property[i].totalConsumption/cities[numberCities].property[i].numberResidents;
        }
    }else{
        controler = 1;
    }
}
void printGroupedConsumption(City cities[], int numberCities) {
    int propertyCount = cities[numberCities].numberProperties;
    if (propertyCount == 0) return;
    int moradoresPorConsumo[201];
    memset(moradoresPorConsumo, 0, sizeof(moradoresPorConsumo));
    for (int i = 0; i < propertyCount; i++) {
        int consPerP = cities[numberCities].property[i].consPerPerson;
        int numResidents = cities[numberCities].property[i].numberResidents;
        moradoresPorConsumo[consPerP] += numResidents;
    }
    bool primeiroElemento = true;
    for (int i = 0; i <= 200; i++) {
        if (moradoresPorConsumo[i] > 0) {
            if (!primeiroElemento) {
                printf(" ");
            }
            printf("%d-%d", moradoresPorConsumo[i], i);
            primeiroElemento = false;
        }
    }
    printf("\n");
}
