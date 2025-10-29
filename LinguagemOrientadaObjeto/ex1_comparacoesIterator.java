/*
Crie uma classe TesteItarator em Java que utilize Coleções.

a) Inserir o método main
-> O método main, utilizando a interface List, crie um conjunto com objetos do tipo:

List<String> lista = new ArrayList<>();
Obs: Não esqueça de incluir os imports necessários. 

ENTRADA

-> um inteiro n, que será a quantidade de elementos da lista
-> n valores do tipo String fornecidos pelo usuário, que serão adicionados na lista com o método add
->Imprima a lista na forma: Sytem.out.println(lista);
->Em seguida ler uma String a ser procurada na lista.
->Utilizar o Iterator para percorrer a lista e o método remove para remover o objeto, se encontrado.
->Imprima a lista após a remoção na forma: Sytem.out.println(lista);

SAIDA

1) a lista de entrada
2) a lista após a remoção de um elemento

A entrada e saída deverão estar como no exemplo.
Não forneça nenhuma impressão diferente do esperado.
*/
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int numeroElementos;
        List<String> lista = new ArrayList<>();
        
        numeroElementos = input.nextInt();
        
        for(int i=0; i<numeroElementos; i++){

            lista.add(input.next());
        }
        System.out.println(lista);
        
        String procurada = input.next();
        Iterator<String> ponteiro = lista.iterator();
        while(ponteiro.hasNext()){
            String conteudo = ponteiro.next();
            if(conteudo.equals(procurada)){
                ponteiro.remove();
                break;
            }
        }

        System.out.println(lista);
    }
}