/*
Neste exercício não é preciso criar mais do que uma classe. Uma única classe poderá ser utilizada para resolver a questão.

Faça um programa em Java que leia um valor inteiro n, que é o tamanho do vetor inteiro vet[n]. 
Leia também n valores inteiros do vetor.
Encontre o maior valor par do vetor e imprima conforme o exemplo.
Se não encontrar nenhum valor par, imprima: "Maior=0, posicao=-1".

Entrada
A entrada contém 1(um) valor inteiro (tamanho do vetor) e mais n valores inteiros, podendo ser positivos ou negativos.

Saída
O maior valor e sua posição conforme o exemplo (contando a posição de 0 a n)
*/
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int tamanhoVetor = input.nextInt();
        int[] vet = new int[n];
        for(int i=0; i<tamanhoVetor; i++){
            vet[i]=input.nextInt();
        }
        int maiorPar = 0;
        int pos=0;
        for(int i=0; i<tamanhoVetor; i++){
            if(vet[i] %2==0){
                if(maiorPar<vet[i]){
                    maiorPar=vet[i];
                    pos = i;
                }
            }
        }
        System.out.printf("Maior=%d, posicao=%d", maiorPar, pos);
    }
}