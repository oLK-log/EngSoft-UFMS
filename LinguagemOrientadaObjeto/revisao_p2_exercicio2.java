import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        String origem, destino, pais;
        double preco;
        Scanner input = new Scanner(System.in);
        try{
            origem = input.next();
            destino = input.next();
            preco = input.nextDouble();
            pais = input.next();
            VooInternacional novoVoo = new VooInternacional(origem, destino, preco, pais);

            novoVoo.comprarPassagem();
            novoVoo.alterarPassagem();
            novoVoo.embarcar();

        }catch(Exception a){
            System.out.print("Entrada Inválida!");
        }
    }
}
interface Passageiro{
    void comprarPassagem();
    void alterarPassagem();
    void embarcar();
}
abstract class Voo implements Passageiro{
    protected String origem;
    protected String destino;
    protected double preco;

    public Voo(String origem, String destino, double preco){
        this.origem = origem;
        this.destino = destino;
        this.preco = preco;
    }
}
class VooInternacional extends Voo{
    private String pais;
    public VooInternacional(String origem, String destino, double preco, String pais){
        super(origem, destino, preco);
        this.pais = pais;
    }

    @Override
    public void comprarPassagem(){
        System.out.print("Passagem voo de "+ origem +" para "+ destino + " "+pais+" valor "+ preco+"\n");
    }
    @Override
    public void alterarPassagem(){
        System.out.print("Passagem para "+destino+" "+pais+ " alterada!\n");
    }
    @Override
    public void embarcar(){
        System.out.print("Embarcando no voo internacional de "+ origem + " para " +destino+" "+pais+"\n");
    }

}