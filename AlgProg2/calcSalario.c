#include <stdio.h>
//programm: calcSalario
//Programmer: Lorran Kaique
/* This program receives an integer number employees,
the amount paid per hour and the number of hours worked, and
then calculates and displays the employee's salary.
Hours over 40 must be paid x1.5
*/
//0. Inicialize abstractions
//0.1 Declareted functions
double calcSalary(double payH, int numH);
int main(){
//0.2 Inicialize variables
    double payH;
    int IdFun, hoursWork;
//1. Read values
    scanf("%d %lf %d",&IdFun, &payH, &hoursWork);
//Calculate salary per employee
    printf("%d %d %.2lf %.2lf",IdFun, hoursWork, payH,calcSalary(payH, hoursWork));
}
double calcSalary(double payH, int numH){
    if(numH <= 40.0){
        return(payH*numH);
    }else{
        return((numH-40)*(payH*1.5))+(payH*40);
    }
}
