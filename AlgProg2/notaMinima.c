#include <stdio.h>
//Programm: notaMinima.c
//Programmer: Lorran Kaique
//date: 26/08/25
/* This program receives two grades, the fist being the
minimium for approval and the second the grade.
Finally, it prints whether it was approved or failed*/
//0.2 function prototype
void checkGrade(float gradeAve, float grade);
int main(){
//0. Starting abstractions
//0.1 inicialize variables
    float gradeMin;
    float grade;
//1. read grade Average and grade
    scanf("%f %f", &gradeMin, &grade);
//2. call function
    checkGrade(gradeMin, grade);
    return 0;
}
//0.2 declareted function
void checkGrade(float gradeAve, float grade){
    if(grade>=gradeAve){
        printf("%.1f Aprovado",grade);
    }else{
        printf("%.1f Reprovado", grade);
    }
}
