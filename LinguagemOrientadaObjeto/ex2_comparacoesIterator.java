/*Crie uma classe TesteItaratorPrevious em Java que utilize Coleções.

a) Inserir o método main
-> O método main, utilizando a interface List, crie um conjunto com objetos do tipo:

List<String> lista = new ArrayList<>();
Obs: Não esqueça de incluir os imports necessários. 

ENTRADA

-> um inteiro n, que será a quantidade de elementos da lista
-> n objetos do tipo String fornecidos pelo usuário, que serão adicionados na lista com o método add
->Utilizando o Iterator com o método hasPrevious(),  percorra a lista ao contrário imprimindo os objeto na ordem inversa que foram impressos.
->Com o método sort, ordene a lista e imprima da forma: System.out.println(lista);

SAIDA

1) a lista de entrada em ordem inversa
2) a lista ordenada

A entrada e saída deverão estar como no exemplo.
Não forneça nenhuma impressão diferente do esperado.
*/
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Iterator;
import java.util.ListIterator;

public class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        List<String> lista = new ArrayList<>();

        int numeroEntradas = input.nextInt();
        for(int i=0; i<numeroEntradas; i++){
            lista.add(input.next());
        }

        ListIterator<String> iterator = lista.listIterator(lista.size());
        while(iterator.hasPrevious()){
            String conteudo = iterator.previous();
            System.out.printf("%s ",conteudo);
        }
        System.out.println();
        Collections.sort(lista);      
        System.out.println(lista);
    }
}