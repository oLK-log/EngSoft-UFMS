#include <stdio.h>
#define NUM 5
#define MAX 20
//Program: salaAluno.cpp
//Programmer: Lorran Kaique
//Date: 09/09/25
/* This program receives a struct Sala{aluno[5], cod}, where
student{name, average} is a struct. Finally, the program prints the
name and average of each student and the overall average of the class.
*/
// Initialize Abstractions
//Declaring structs
struct Student{
    char name[MAX+1];
    float average;
};
struct Room{
    Student student[NUM+1];
    int cod;
};
//Declaring functions
float generalAverage(Room room[]);
void readStudents(Room room[]);

//Starting Main program
int main(){
    Room room[NUM];
    scanf("%d", &room[0].cod);
    readStudents(room);
    printf("Sala: %d\n", room[0].cod);
    for(int i=0; i<5; i++){
        printf("%s %.2f\n", room[0].student[i].name, room[0].student[i].average);
    }
    printf("Media: %.2f", generalAverage(room));

}
//creating functions
float generalAverage(Room room[]){
    float media = 0;
    for(int i=0; i<5; i++){
        media+= room[0].student[i].average;
    }
    return media/5.0;
}
void readStudents(Room room[]){
    for(int i=0; i<5; i++){
        scanf(" %[^\n]", room[0].student[i].name);
        //printf("%s\n", room[0].student[i].name);
        scanf("%f", &room[0].student[i].average);
        //printf("%f", room[0].student[i].average);
    }
}
