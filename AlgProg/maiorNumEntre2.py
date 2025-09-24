#Dado dois números inteiros, deseja-se saber qual é o maior
#se forem iguais, estarão indicados nas duas respostas
#entrada na mesma linha- numbers
numbers = str(input("Digite dois números inteiros:\n"))
n1, n2 = numbers.split(" ")
n1 = int(n1)
n2 = int(n2)
if n1 > n2:
    maior = n1
    menor = n2
elif n2 > n1:
    maior = n2
    menor = n1
else:
    maior = n1
    menor = n2
print('Maior = {0:d}\nMenor = {1:d}'.format(maior, menor))
    
