import java.util.Scanner;
import java.util.Iterator;
import java.util.List;
import java.util.ArrayList;
//Iterator eh um controle universal para colecoes
//fornece uma maneira padronizada de percorrer l]elementos de uma colecao
//hasNext() - Tem um prox elemento? (retorna True se ainda houver)
//next() - Qual esse prox elemento? (retorna o proc e move o ponteiro)
//remove() remove um elemento 
public class Main{
    public static void main(String args[]){
        int numElementosListaProdutos;
        String produto, produtoProcurado;
        Scanner input = new Scanner(System.in);
        List<String> listaProdutos = new ArrayList<>();

        numElementosListaProdutos = input.nextInt();

        for(int i=0; i<numElementosListaProdutos; i++){
            produto = input.next();
            listaProdutos.add(produto);
        }

        System.out.println(listaProdutos);

        produtoProcurado = input.next();
        Iterator<String> listaProdutosIterator = listaProdutos.iterator();
        while(listaProdutosIterator.hasNext()){
            if(listaProdutosIterator.next().equals(produtoProcurado)){
                listaProdutosIterator.remove();
            }
        }

        System.out.println(listaProdutos);
    }
}

/*
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;

public class TesteIterator {

	public static void main(String[] args) {
		List<String> lista = new ArrayList<>();
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		for(int i=0;i<n;i++) {
			lista.add(sc.next());
		}
		System.out.println(lista);
		String procura=sc.next();
        Iterator<String> iterador = lista.iterator(); 
        while (iterador.hasNext()) { 
            String lista2 = iterador.next();            
            if (lista2.equals(procura)) 
                iterador.remove();            
        }
        System.out.println(lista); 
    }

}

 */