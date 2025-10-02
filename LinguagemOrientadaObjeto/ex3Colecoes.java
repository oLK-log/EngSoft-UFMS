import java.util.Scanner;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Collections;
import java.util.Map;
import java.util.TreeMap;

public class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        List<Celular> listaDeCelular = new ArrayList<>();

        for(int i=0; i<5; i++){
            int codigo = input.nextInt();
            String marca = input.next();
            String modelo = input.next();

            Celular newCelular = new Celular(codigo, marca, modelo);
            listaDeCelular.add(newCelular);
        }
        
        //for(Celular celular : listaDeCelular){
        //    System.out.println(celular);
        //}
        System.out.println(listaDeCelular);
        input.close();
    }
}
class Celular{
    private int codigo;
    private String marca;
    private String modelo;
    public Celular(int codigo, String marca, String modelo){
        this.codigo = codigo;
        this.marca = marca;
        this.modelo = modelo;
    }
    
    public int getCodigo(){
        return this.codigo;
    }
    public String getMarca(){
        return this.marca;
    }
    public String getModelo(){
        return this.modelo;
    }

    @Override
    public String toString(){
        return "COD:"+ getCodigo() +",marca:"+ getMarca() +",modelo:"+ getModelo();
    }
}