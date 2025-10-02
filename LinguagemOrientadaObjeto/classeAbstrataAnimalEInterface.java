import java.util.Scanner;
public class Main{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String nome1 = input.next();
        int patas1 = input.nextInt();
        Cachorro c1 = new Cachorro(nome1, patas1);
        System.out.println(c1.toString());

        String nome2 = input.next();
        int patas2 = input.nextInt();
        Gato g1 = new Gato(nome2, patas2);
        System.out.println(g1.toString());

        String nome3 = input.next();
        int patas3 = input.nextInt();
        Papagaio g2 = new Papagaio(nome3, patas3);
        System.out.println(g2.toString());
    }
}
interface EmitirSom {
    abstract String fazerBarulho();
}
abstract class Animal implements EmitirSom{
    //Qualquer modificador, quando nao coloca nada, eh packde-private
    protected String nome;
    protected int nPatas;
    public Animal(String nome, int nPatas){
        this.nome = nome;
        this.nPatas = nPatas;
    }
    abstract int numeroDePatas();
    
    public String getNome(){
        return nome;
    }
    public int getnPatas(){
        return nPatas;
    }
}

class Cachorro extends Animal{
    public Cachorro(String nome, int nPatas){
        super(nome, nPatas);
    }
    @Override
    public int numeroDePatas(){
        return nPatas;
    }
    @Override
    public String fazerBarulho(){
        return "auau";
    }

    @Override
    public String toString(){
        return "O cachorro "+ getNome() + " com "+numeroDePatas()+
        " patas fez " + fazerBarulho();
    }
}


class Gato extends Animal{
    public Gato(String nome, int nPatas){
        super(nome, nPatas);
    }
    @Override
    public int numeroDePatas(){
        return nPatas;
    }
    @Override
    public String fazerBarulho(){
        return "miau";
    }

    @Override
    public String toString(){
        return "O gato "+ getNome() + " com "+numeroDePatas()+
        " patas fez " + fazerBarulho();
    }
}
class Papagaio extends Animal{
    public Papagaio(String nome, int nPatas){
        super(nome, nPatas);
    }
    @Override
    public int numeroDePatas(){
        return nPatas;
    }
    @Override
    public String fazerBarulho(){
        return "loro";
    }

    @Override
    public String toString(){
        return "O papagaio "+ getNome() + " com "+numeroDePatas()+
        " patas fez " + fazerBarulho();
    }
}