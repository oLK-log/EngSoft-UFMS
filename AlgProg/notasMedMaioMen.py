#ler uma lista de notas float
#a nota varia de 0.0 a 10,0
#Computar a maior, a menor e a média
#Uma nota negativa indica o final da lista
#Pensamento: a entrada ser feita em um loop
#para calcular maior e menor utilizar
#variaveis para cada e variaveis para a anterior
#para a media, criar um contador e ir somando as entradas em uma variável
#entrada
nota = 0.0
maior = 0.0
menor = 10.0
media = 0.0
notaAnterior = 0.0
contador = 0

while nota != -1.0:
    nota = float(input("Digite a nota:\n"))
    if nota > maior and nota != -1.0:
        maior = nota
    if nota < menor and nota != -1.0:
        menor = nota
    if nota != -1.0:
        media +=nota
        contador += 1
media = media / contador

print('Maior Nota  ={0:.1f}\nMenor Nota  ={1:.1f}\nMédia Notas ={2:.1f}'.format(maior, menor, media))
    