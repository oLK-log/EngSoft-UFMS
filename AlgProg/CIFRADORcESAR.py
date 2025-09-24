#Cifrador de César
#vamor ter que converter para cod(número) somar o deslocamento e converter de volta para número
#a entrada tem 6 caracteres
#usar for por 6
palavra = input()
deslocamento = int(input())
l1 = l2 = l3 = l4 = l5 = l6 = " "
cont = 0
for letra in palavra:
    cont += 1
    cod = deslocamento + ord(letra)
    if cont == 1:
        l1 = chr(cod)
    elif cont == 2:
        l2 = chr(cod)
    elif cont == 3:
        l3 = chr(cod)
    elif cont == 4:
        l4 = chr(cod)
    elif cont == 5:
        l5 = chr(cod)
    elif cont == 6:
        l6 = chr(cod)
print(l1,l2,l3,l4,l5,l6, sep="")