/*
 Crie uma classe MainTestGeneric em Java 

a) Faça um método genérico void removeValores que receba um ArrayList de Tipo Genérico(podendo ser vetor de Integer, String, etc) e remove os valores do Array cujo índice do Array é ímpar e depois imprime os valores do Array
    public static <T>void removeElemento(List<T> list)

b) Faça um método main: public static void main(String[] args)

b.1) Ler n>2 (fornecido pelo usuário), que será a quantidade de elementos de dois vetores,

b.2) Ler os n elementos (fornecidos pelo usuário), dos dois ArrayLists (Um de Integer e outro de String) 

   Utilize next() para ler os elementos do vetor de Strings.

    Obs: Não esqueça de incluir os imports necessários. 

b.3) A entrada e saída deverão estar como no exemplo. Não forneça nenhuma impressão diferente do esperado.
 */
import java.util.ArrayList;
import java.util.Scanner;
import java.util.List;

public class MainGenerico{
    public static double somaList(ArrayList<? extends Number> list){
        double soma = 0.0;

        for(Number elemento : list){
            soma += elemento.doubleValue();
        }
        return soma;
    }
    public static void main(String[] args){        
        Scanner input = new Scanner(System.in);
        int n;

        n = input.nextInt();
        ArrayList<Integer> listaInteiros = new ArrayList<>();
        for(int i=0; i<n; i++){
            listaInteiros.add(input.nextInt());
        }

        ArrayList<Double> listaDoubles = new ArrayList<>();
        for(int i=0; i<n; i++){
            listaDoubles.add(input.nextDouble());
        }

        System.out.println("Lista Inteiros: " + listaInteiros);
        System.out.println("Soma Inteiros: "+ somaList(listaInteiros));

        System.out.println("Lista Doubles: " + listaDoubles);
        System.out.println("Soma Doubles: "+ somaList(listaDoubles));

    }

}

/*
 import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.util.InputMismatchException;

public class MainGeneric {
	public static double somaList(ArrayList<? extends Number> list) {
		double soma=0;
		for(Number element : list) {
			soma+=element.doubleValue();
		}
		return soma;
	}
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		List <Integer> listInt=new ArrayList<Integer>();
		List <Double> listDouble=new ArrayList<Double>();
		int n=sc.nextInt();
		try {
			for(int i=0;i<n;i++) 
				listInt.add(sc.nextInt());
			for(int i=0;i<n;i++) 
				listDouble.add(sc.nextDouble());
			System.out.println("Lista Inteiros: " + listInt);
			System.out.println("Soma Inteiros: " + somaList((ArrayList<? extends Number>) listInt));
			System.out.println("Lista Doubles: " + listDouble);
			System.out.println("Soma Doubles: " + somaList((ArrayList<? extends Number>) listDouble));
		}catch(InputMismatchException e) {
			System.out.println("Entrada Inválida");
		}
	}
}

 */