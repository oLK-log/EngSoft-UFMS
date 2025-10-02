/*
Neste exercício não é preciso criar mais do que uma classe. Uma única classe poderá ser utilizada para resolver a questão.

Faça um programa em Java que leia 1(um) valor inteiro n, que é o tamanho da matriz quadrada M[n][n]. 
Leia mais 1(um) valor inteiro lin, que indica a linha de uma matriz na qual uma operação deve ser realizada.
Leia também (n*n) valores inteiros da matriz quadrada M[n][n]. 
Em seguida, procure o menor elemento na linha lin e guarde sua posição. Imprima o menor elemento e sua posição na matriz, linha e coluna (nesta ordem), contando a posição na linha e na coluna de 0 a n-1.

Entrada
A primeira linha de entrada contem 1(um) valor inteiro n, na segunda linha 1(um) valor inteiro lin, indicando a linha que será considerada para operação. Em seguida os (n*n) valores inteiros que compõem a matriz.

Saída
Imprima o menor valor, e na próxima linha imprima a linha e a coluna do menor valor, conforme exemplo abaixo.
*/
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int[][] matrizQuadrada = new int[n][n];
        
        int linhaOperacao = input.nextInt();
        
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                matrizQuadrada[i][j] = input.nextInt(); 
            }
        }
        
        int menorValor = matrizQuadrada[0][0];
        int coluna = 0;
        
        for(int i=0; i<n; i++){
            if(matrizQuadrada[linhaOperacao][i]<menorValor){
                menorValor = matrizQuadrada[linhaOperacao][i];
                coluna=i;
            }
        }
        
        System.out.printf("Menor=%d\nlinha:%d, coluna:%d", menorValor, linhaOperacao, coluna);
    }
}