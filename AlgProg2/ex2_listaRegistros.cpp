#include <stdio.h>
#include <string.h>
#define MAX 30
//Program: ex2_listaRegistros.cpp
//Programmer: Lorran Kaique
//Date: 06/09/25
/* This program receive information from five users(number, name and course).
Then it reads the name of the course and list all the students (number and name)
taking the course*/
//Initialize abstractions
struct tAluno{
    int cod;
    char nome[MAX+1];
    char curso[MAX+1];
} ;
//declare functions
void findCourse(tAluno alunos[],char cursoP[]){
    //Find course students
    for(int i=0; i<5; i++){
        if(strcmp(alunos[i].curso, cursoP)==0){
            printf("%d %s\n",alunos[i].cod, alunos[i].nome);
        }
    }
}
int main(){
    //declare variables
    tAluno alunos[6];
    char cursoP[MAX+1];
    //receive students
    for(int i=0;i<5; i++){
        scanf("%d", &alunos[i].cod);
        scanf(" %[^\n]", alunos[i].nome);
        scanf(" %[^\n]", alunos[i].curso);
    }
    //read researched course
    scanf(" %[^\n]", cursoP);
    findCourse(alunos, cursoP);

}
