#ler uma palavra e falar se é políndromo
#entra:str palavra
palavra = str(input("Digite a palavra:\n"))
inversa = ""
for letra in palavra:
     inversa = letra +inversa

if palavra != inversa:
    print(" A palavra ", palavra, " não é um políndromo.")
    print('A palavra {0:s} não é um políndromo'.format(palavra))
else:
    print("A palavra", palavra, "é um políndromo.")
    print('A palavra {0:s} é um políndromo.'.format(palavra))