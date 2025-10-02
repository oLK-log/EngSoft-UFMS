/*
Crie um projeto em Java que contenha as seguintes classes, atributos e métodos. 
-Ao final, coloque todas as classes em um único arquivo e envie no ava.
-A classe que contém o método main, deverá vir primeiro.
-Somente a classe Main com o método main poderá ser pública.

a) class Conta

 a.1) atributos privados:  agencia String, numero int, titular String, saldo double

 a.2) construtor com agencia, numero e titular

 a.3) métodos getter e setter para os atributos: numero e saldo

 a.4) método public boolean sacar(double valor)
        se o valor do saque for menor que o saldo
             saldo=saldo-valor
             imprime("Conta="+numero+", saque de "+valor+". Saldo = "+saldo)
             retorna true
        senão
              imprime(“Valor do saque não permitido”)
              retorna false

a.5) método public void depositar(double valor)
         saldo=saldo+valor;
         imprime("Conta="+numero+", deposito de "+valor+". Saldo = "+saldo)

a.6) método public boolean transferir(Conta contaDestino, double valor)
        um boleano confirma recebe sacar(valor)
        se confirma for igual a true
                 contaDestino chama o método depositar(valor)
                 retorna true;
        senão
                 retorna false;

a.7) método toString que retorna uma String com os atributos no seguinte formato          
     return titular+" Ag=" + agencia + ", num=" + numero + ", saldo=" + saldo ;

b) classe Main com o método main para testar teste as funcionalidades da classe Conta

 -para ler as Strings utilizar o método next().

b.1) Ler as informações da Conta pelo Scanner e criar um objeto  conta1.
b.2) Ler as informações do Conta pelo Scanner e criar um objeto  conta2.
b.3) Ler um valor e depositar na conta1
b.4) Ler um valor e depositar na conta2
b.5) Ler um valor e transferir o valor da conta1 para a conta2
b.6) Ler e sacar um valor da conta1
b.7) Imprimir a conta1 e a conta2
*/
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String ag1 = input.next();
        int num1 = input.nextInt();
        String nome1 = input.next();
        Conta conta1 = new Conta(ag1, num1, nome1);

        String ag2 = input.next();
        int num2 = input.nextInt();
        String nome2 = input.next();
        Conta conta2 = new Conta(ag2, num2, nome2);

        //ler um valor e depositar na conta um
        double valorDeposito1 = input.nextDouble();
        conta1.depositar(valorDeposito1);
        //ler um valor e depositar na conta 2
        double valorDeposito2 = input.nextDouble();
        conta2.depositar(valorDeposito2);
        //ler um valor e transferir da conta1 para a conta2
        double valorTransferencia = input.nextDouble();
        conta1.transferir(conta2, valorTransferencia);
        //Ler e sacar um valor da conta 1
        double valorSaque = input.nextDouble();
        conta1.sacar(valorSaque);
        //imprimir a conta 1 e 2
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