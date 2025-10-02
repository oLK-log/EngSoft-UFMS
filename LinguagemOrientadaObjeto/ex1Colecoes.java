import java.util.Scanner;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Collections;

public class Main{
    public static void main(String[] args) {
        int achou = 0;
        Scanner input = new Scanner(System.in);
        List<String> list = new LinkedList<String>();
        for(int i=0; i<6; i++){
            list.add(input.next());
        }
        
        for(int i=0; i<6; i++){
            System.out.printf("%s ", list.get(i));
        }
        System.out.println();
        // ordenar lista
        List<String> listaOrdenada = new ArrayList<String>(list);
        Collections.sort(listaOrdenada);
        for(int i=0; i<6; i++){
            System.out.printf("%s ",listaOrdenada.get(i));
        }
        System.out.println();
        String procurado = input.next();
        for(int i=0; i<6; i++){
            if(list.get(i).equals(procurado)){
                achou = 1;
            }
        }
        if(achou == 1){
            System.out.printf("encontrado");
        }else{
            System.out.printf("não encontrado");
        }
    }
}