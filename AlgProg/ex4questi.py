# -*- coding: utf-8 -*-
# Programa: exer4
# Programador:Lorran Kaíque
# Data: 16/05/2025
# Este programa le uma lista tam, um numero
#inteiro n e uma posição i. Por fim imprime
#a lista resultante com o numero n inserido
#entrada:list tam, int n, int i
#saida: list lista
#Passo 0: Iniciar variáveis
lista = []
#Passo 1: ler entradas
tam = list(map(int, input().split()))
n, i = map(int, input().split())
#Passo 2- Colocar o n na posição i
#Passo 2.1. calcular tamanho da lista
qtd = len(tam)
#a nova lista será a qtd+1
#Passo 2.2. Iterar na lista
for x in range(0, qtd):
    if x == i:
        lista.append(n)
        lista.append(tam[x])
    else:
        lista.append(tam[x])
#Passo 3- Imprimir
print('[',end='')
for x in range(qtd):
    print(lista[x],end=',')
print(lista[qtd],']',sep='')
#print(#'[{}]'.format(', '.join(map(str, lista))))

def inserir_elemento_na_lista():
    try:
        # Lê a primeira linha e cria a lista de inteiros
        lista_str = input().split()
        lista = [int(num) for num in lista_str]
        tam = len(lista)

        # Lê a segunda linha com o número a ser inserido e a posição
        entrada_segunda_linha = input().split()
        elemento_inserir = int(entrada_segunda_linha[0])
        posicao = int(entrada_segunda_linha[1])

        # Verifica se a posição é válida
        if 0 <= posicao <= tam:
            # Insere o elemento na posição desejada
            lista.insert(posicao, elemento_inserir)
            # Imprime a lista resultante
            print(lista)
        else:
            print("Posição inválida.")

    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números inteiros separados por espaços.")
    except IndexError:
        print("Entrada inválida. Certifique-se de fornecer dois números na segunda linha.")

if __name__ == "__main__":
    inserir_elemento_na_lista()