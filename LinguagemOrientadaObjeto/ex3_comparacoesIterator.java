import java.util.Scanner;
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class Main {
    public static void main(String[] args){
        int numElementos = 5;
        int codigo;
        String marca, modelo;

        Scanner input = new Scanner(System.in);
        List<Celular> listaDeCelular = new ArrayList<>();

        for(int i = 0; i<numElementos; i++){
            codigo = input.nextInt();
            marca = input.next();
            modelo = input.next();
            Celular cel = new Celular(codigo, marca, modelo);
            listaDeCelular.add(cel);
        }

        System.out.println(listaDeCelular);

        //Encontrar o menor elemento da lista(por marca)
        Celular menorCelular = Collections.min(listaDeCelular);
        System.out.println("O menor elemento é: "+ menorCelular.toString());
        //Ordenar os celulares pelo atributo da marca
        //reverseOrder() or naturalOrder()
        listaDeCelular.sort(Comparator.naturalOrder());
        System.out.println(listaDeCelular);
    }
}
class Celular implements Comparable<Celular> {
    private int codigo;
    private String marca;
    private String modelo;
    public Celular(int codigo, String marca, String modelo){
        this.codigo = codigo;
        this.marca = marca;
        this.modelo = modelo;
    }

    @Override
    public String toString(){
        return "COD:"+ codigo +",marca:"+marca+",modelo:"+modelo;
    }
    @Override
    public int compareTo(Celular outroCelular){
        return this.marca.compareTo(outroCelular.marca);
    }
    /*Se fosse pelo codigo
    public int compareTo(celular outroCelular){
        return Integer.compare(this.codigo, outroCelular.codigo);
    }
     */
}

/*
 import java.util.ArrayList;
import java.util.Collections;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;

public class Celular implements Comparable<Object>{
	private int cod;
	private String marca;
	private String modelo;
	public Celular(int cod, String marca, String modelo) {		
		this.cod = cod;
		this.marca = marca;
		this.modelo=modelo;
	}
	public String getMarca() {
		return marca;
	}
	public void setMarca(String marca) {
		this.marca = marca;
	}
	@Override
	public String toString() {
		return "COD:"+cod+ ",marca:" + marca+",modelo:"+modelo;	}
	@Override
	public int compareTo(Object obj) {
		//return getNum()-((Aluno) obj).getNum();
		return getMarca().compareTo(((Celular)obj).getMarca());
	}
	
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);		
		int cod;
		String modelo;
		String marca;
		List<Celular> list1=new ArrayList<Celular>();
		try {
			for(int i=0;i<5;i++) {
				cod=sc.nextInt();
				marca=sc.next();
				modelo=sc.next();
				list1.add(new Celular(cod,marca,modelo));
			}
			System.out.println(list1);
			System.out.println("O menor elemento é: "+Collections.min(list1));
			Collections.sort(list1);
			System.out.println(list1);
		}catch(InputMismatchException e) {
			System.out.println("Entrada Inválida!");
		}
	}	
}

 */