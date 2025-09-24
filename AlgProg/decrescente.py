# este programa, dada uma lista,verifica se os numeros
#dessa lista estão em ordem decrecente
#inicio do mod principal
#descrição das variaveis utilizadas
lista: list
tam: int
i: int
msg: str
#list lista
#int tam, i
#str msg

#pré: lista[0], lista[1], ..., lista[tam-1]

#Passo 1: Leia a lista
#Passo 1.1- Leia os elementos da lista
lista = list(map(int, input().split()))
#Passo 1.2- Calcule o tamanho da lista
tam = len(lista)
#Passo 2: Verifica se a lista é decrescente
msg= 'verdadeiro'
i = 0
while i < tam-1:
    if lista[i] <= lista[i+1]:
        msg = 'falso'
        i = tam
    else:
        i += 1
#Passo 3: Imprima o resultado
print(msg)