/*Neste exercício não é preciso criar mais do que uma classe. Uma única classe poderá ser utilizada para resolver a questão.

Faça um programa em Java que leia um inteiro n, o tamanho do vetor inteiro v.

Leia também um valor x, e faça com que o programa coloque o valor lido na primeira posição do vetor v[n]. Em cada posição subsequente, coloque o dobro do valor da posição anterior. Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente. Mostre o vetor em seguida.

Entrada

A entrada contém (2) dois valores inteiros positivos n e x ( 0<x<=30).

Saída

Para cada posição do vetor, escreva "v[i] = y", onde i é a posição do vetor e y é o valor armazenado na posição i. O primeiro número do vetor v (v[0]) irá receber o valor de x.
*/
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int tamanhoVetor = input.nextInt();
        int[] vetor = new int[tamanhoVetor];
        vetor[0] = input.nextInt();
        for(int i=1; i<tamanhoVetor; i++){
            vetor[i] = vetor[i-1]*2;
        }
        for(int i=0; i<tamanhoVetor; i++){
            System.out.printf("v[%d] = %d\n", i, vetor[i]);
        }
    }
}
