/*
Crie um projeto em Java que contenha as seguintes classes, atributos e métodos. 
-Ao final, coloque todas as classes em um único arquivo e envie no ava.
-A classe que contém o método main, deverá vir primeiro.
-Somente a classe Main com o método main poderá ser pública.

a) class Conta

//Utilizar a classe Conta do exercício anterior


b) class ContaCorrente  subclasse da classe Conta

b.1) herda os atributos e métodos da classe Conta

b.2) Construtor com os atributos de Conta

b.3) método public void gerarTarifa()
        variável double valor=14.5;
        saldo da conta recebe o saldo atual – valor
        //obs: mesmo que não tenha saldo o valor será debitado da conta.
        imprime a Conta, a tarifa e o saldo atualizado após pagamento da tarifa.

b.4) método toString() que chama o toString() da superclasse para imprimir as informações de conta corrente de acordo com o exemplo.

c) public class Teste com o método main para testar teste as funcionalidades da classe Conta

 -para ler as Strings utilizar o método next().

c.1) Ler as informações da ContaCorrete pelo Scanner e criar um objeto  cc1.
c.2) Ler as informações da ContaCorrete pelo Scanner e criar um objeto  cc2.
c.3) Ler um valor e depositar na cc1
c.4) Ler um valor e depositar na cc2
c.5) Ler um valor e transferir o valor da cc1 para a cc2
c.6) descontar a tarifa para da cc1
c.6) Imprimir a cc1 e a cc2
*/
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String agencia1 = input.next();
        int numero1 = input.nextInt();
        String nome1 = input.next();
        ContaCorrete conta1 = new ContaCorrete(agencia1, numero1, nome1);

        String agencia2 = input.next();
        int numero2 = input.nextInt();
        String nome2 = input.next();
        ContaCorrete conta2 = new ContaCorrete(agencia2, numero2, nome2);

        //ler um valor e depositar na conta1
        double valor1 = input.nextDouble();
        conta1.depositar(valor1);
        //ler um vaor e depositar na conta 2
        double valor2 = input.nextDouble();
        conta2.depositar(valor2);
        //ler um valor e transferir o valor da conta 1 para a conta 2
        double valorTranferencia = input.nextDouble();
        conta1.transferir(conta2, valorTranferencia);
        //descontar tarifa para conta 1
        conta1.gerarTarifa();
        //imprimir conta 1 e conta 2
        System.out.print(conta1.toString()+conta2.toString());
    }
}
class Conta{
    private String agencia;
    private int numero;
    private String titular;
    private double saldo;

    public Conta(String agencia, int numero, String titular){
        this.agencia = agencia;
        this.numero = numero;
        this.titular=titular;
        this.saldo=saldo;
    }

    public  void setNumero(int numero){
        this.numero = numero;
    }
    public void setSaldo(double saldo){
        this.saldo = saldo;
    }
    public int getNumero(){
        return numero;
    }
    public double getSaldo(){
        return saldo;
    }

    public boolean sacar(double valor){
        if(valor < getSaldo()){
            setSaldo((getSaldo()-valor));
            System.out.print("Conta="+numero+", saque de "+valor+". Saldo = "+saldo+"\n");
            return true;
        }else{
            System.out.print("Valor do saque não permitido\n");
            return false;
        }
    }
    public void depositar(double valor){
        setSaldo(getSaldo()+valor);
        System.out.print("Conta="+numero+", deposito de "+valor+". Saldo = "+saldo+"\n");
    }
    public boolean transferir(Conta contaDestino, double valor){
        if(sacar(valor)){
            contaDestino.depositar(valor);
            return true;
        }else{
            return false;
        }
    }
    @Override
    public String toString(){
        return titular+" Ag=" + agencia + ", num=" + numero + ", saldo=" + saldo+"\n";
    }
}
class ContaCorrete extends Conta{
    public ContaCorrete(String agencia, int numero, String titular){
        super(agencia,numero,titular);
    }

    public void gerarTarifa(){
        double valor=14.5;
        setSaldo(getSaldo()-valor);//mesmo sem saldo é debitado
        System.out.print("Conta="+getNumero()+", tarifa de "+valor+". Saldo = "+getSaldo()+"\n");
    }
    @Override
    public String toString(){
        return "ContaCorrente "+ super.toString();
    }
}