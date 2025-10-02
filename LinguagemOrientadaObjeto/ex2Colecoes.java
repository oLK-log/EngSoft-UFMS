import java.util.Scanner;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Collections;
import java.util.Map;
import java.util.TreeMap;

public class Main{
    public static void main(String[] args){
        int nElementos=5;
       Scanner input = new Scanner(System.in);
       String chave, valor;
       Map<String,String> mapa = new TreeMap<>();
       for(int i=0; i<nElementos; i++){
            chave= input.next();
            valor= input.next();
            mapa.put(chave,valor);
       }
       //receber informacao
       String busca = input.next();
       //buscar no MAp
       if(mapa.containsKey(busca)){
            System.out.printf("Valor da chave(%s)=%s\n",busca, mapa.get(busca));
       }else{
            System.out.printf("não encontrado\n");
       }
       System.out.printf("Quantidade de elementos: %s\n", nElementos);

    }
}