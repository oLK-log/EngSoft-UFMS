import java.util.Scanner;
import java.util.LinkedList;

public class Main{
    public static void main(String[] args){
        String marca, modelo;
        int marcha, indiceRemocao;
        try{
            Scanner input = new Scanner(System.in);
            LinkedList<Bicicleta> listaBicicleta = new LinkedList<>();
            //Lendo o numero de elementos da colecao
            int numElementos = input.nextInt();
            //Lendo os numElementos bicicletas
            for(int i=0; i<numElementos; i++){
                marca = input.next();
                modelo = input.next();
                marcha = input.nextInt();

                Bicicleta bici = new Bicicleta(marca, modelo, marcha);

                listaBicicleta.add(bici);
            }
            //Lendo o numero
            try{
                indiceRemocao = input.nextInt();

                //Imprimindo lista inicial
                System.out.printf("Lista Inicial:\n");
                    for(Bicicleta bici : listaBicicleta){
                        System.out.print(bici.toString());
                }
                //removendo item
                    listaBicicleta.remove(indiceRemocao);
                //Imprimindo lista após remoção
                    System.out.printf("Lista Final:\n");
                for(Bicicleta bici : listaBicicleta){
                    System.out.print(bici.toString());
                }

            }catch(Exception v){
                System.out.print("Índice Inválido");
            }
        }catch(Exception e){
            System.out.print("Entrada Inválida");
        }
    }
}
 class Bicicleta {
    private String marca;
    private String modelo;
    private int numMarcha;

    public Bicicleta(String marca, String modelo, int numMarcha){
        this.marca = marca;
        this.modelo = modelo;
        this.numMarcha = numMarcha;
    }

    public int getNumMarcha(){
        return numMarcha;
    }

    @Override
    public String toString(){
        return "Bicicleta "+ marca + " " + modelo + ", " + numMarcha + " marchas\n";
    }
 }