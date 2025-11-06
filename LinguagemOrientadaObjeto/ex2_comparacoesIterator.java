import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.ListIterator;
import java.util.Comparator;
//ListIterator
//hasPrevious() - retorna true se houver um elemento antes da posicao atual
//previous() - retorna o elemento 

public class Main {
    public static void main(String[] args){
        int numElementos;
        String elemento;
        Scanner input = new Scanner(System.in);
        List<String> listaPapelaria = new ArrayList<>();

        numElementos = input.nextInt();
        for(int i=0; i<numElementos; i++){
            elemento = input.next();
            listaPapelaria.add(elemento);
        }


        //for (TipoDoElemento nomeDaVariavel : nomeDaColecao)
        
        
        ListIterator<String> listaPapelariaIterator = listaPapelaria.listIterator(listaPapelaria.size());
        while(listaPapelariaIterator.hasPrevious()){
            System.out.print(listaPapelariaIterator.previous()+" ");
        }
        System.out.println();

        //reverseOrder() or naturalOrder()
        listaPapelaria.sort(Comparator.naturalOrder());

        /*while(listaPapelariaIterator.hasPrevious()){
            System.out.println(listaPapelariaIterator.previous());
        }*/
        System.out.println(listaPapelaria);
    }
}
/*
 import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;
import java.util.Scanner;

public class TesteReverso {
	public static void main(String[] args) {
		List<String> lista = new ArrayList<>();
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		for(int i=0;i<n;i++) {
			lista.add(sc.next());
		}        
		ListIterator<String> iterator = lista.listIterator(lista.size());        
        while (iterator.hasPrevious()) {
            String obj = iterator.previous();
            System.out.print(obj+" ");
        }
        Collections.sort(lista);
        System.out.println("\n"+lista);
	}
}

 */