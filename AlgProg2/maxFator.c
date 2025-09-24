#include <stdio.h>
#include <stdlib.h>
//Program: maxFator
//Programmer: Lorran KAique
//Date: 26/08
/* this program receives an integer N and calculates the maximum
factor of that number
--> greatest proper divisor
*/
//Step 0.2 declare functions
int maxFactor(int num);
int main(){
//Step 0. Inicialize abstractions
//0.1 Start variables
    int factor;
    int max;
//1. receive inputs
    scanf("%d",&factor);
//2.Find the greatest factor
    max = maxFactor(factor);
//3. Print response
    printf("%d %d", factor, max);
}
int maxFactor(int num){
    num = abs(num);
    int primeFactor = num;
    if(num%2==0){
        primeFactor = 2;//if num is even, in the all cases the prime factor is '2'
    }else{
        for(long long i =3; i*i<= num; i+=2){//if num is odd, it is necessary to find the value, because the prime factor changes
//start in 3, while raiz quadrada <= num, i+2 because is odd number
            if(num%i == 0){
                primeFactor = i;//Find the prime factor
                break;
            }
        }
    }
    return (num/primeFactor);
}
