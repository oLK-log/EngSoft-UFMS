#include <stdio.h>
#define MAX 30
#define TAM 10
//Program: ex5_struct_Person
//Programmer: Lorran Kaíque
//DAte: 02/09
/*This program allows you to store the name, height and
date of birth of up to 10 people.*/
//
//inicialize structs
struct tData{
    int dia,mes,ano;
};
struct tpessoa{
    char name[MAX+1];
    float altura;
    struct tData dtnasc;
};
//define functions
//function to list all system options
int menu(){
    int op;

    printf("\n\n[1] Inserir pessoa");
    printf("\n[2] Listar pessoas");
    printf("\n[3] Listar pessoas por data");
    printf("\n[4] Sair");
    printf("\n Digite sua opção:");
    scanf("%d", &op);

    return op;
};
//insert person
//Por que tem esse '&' do lado no n
//Por que passamos um vetor se ele nem está inicializado
//Por que não é usado '&' no scanf
void cadastrar(int (&n), tPessoa vetor[]){
    printf("Nome:");
    scanf("%[^\n]",vetor[n].nome);

    printf("Altura:");
    scanf("%f",vetor[n].altura);

    printf("Dt nascimento (dd/mm/aa):");
    scanf("%d/%d/%d", &vetor[n].dtnasc.dia,&vetor[n].dtnasc.mes,&vetor[n].dtnasc.ano);

    n++;
}
//list all names and heights
void listar(int &n, tPessoa vetor[]){
    for(int i=0; i<n; i++){
        printf("%s %.2f\n", vetor[n].nome, vetor[n].altura);
    }
    printf("\n");
}
//list the names od people who were born before a certain given date
void listagem2(int n, tPessoa vetor[], tDate D){
    for(int i=0;i<n;i++){
        if(vetor[i].dtnasc.ano<D.ano){
            printf("%s", vetor[i].nome);
        }else if(vetor[i].dtnasc.ano==D.ano && vetor[i].dtnasc.mes<D.mes){
            printf("%s",vetor[i].nome);
        }else if(vetor[i].dtnasc.ano==D.ano && vetor[i].dtnasc.dia<D.dia){
            printf("%s",vetor[i].nome);
        }
    }
}
//main
int main(){
    int opcao;
    tPessoa listaPessoas[TAM];

    int nCadastradas = 0;//numero de pessoas cadastradas inicia 0

    do{//faça...
        op = menu();

        if(op==1){//Cadastrar uma pessoa
            cadastrar(nCadastradas, listaPessoas);
        }else if(op==2){//Listar todos os nome e alturas
            listar(nCadastradas, listaPessoas)
        }else if(op==3){//listar nome que nasceram antes de x
            data A;
            printf("Digite a data a consultar (dd/mm/aa):");
            scanf("%d/%d/%d", &A.dia, &A.mes, &A.ano);
            listagem2(nCadastradas, listaPessoas, A);
        }
    }while(op != 4);

    return 0;
}
