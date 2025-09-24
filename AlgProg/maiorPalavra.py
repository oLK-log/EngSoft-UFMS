#A maior palavra entre tres
#tres entradas_string palavra1, palavra2, palavra3

palavra1 = str(input("Insira a primeira palavra:\n"))
palavra2 = str(input("Insira a segunda palavra:\n"))
palavra3 = str(input("Insira a terceira palavra:\n"))

maior = palavra1
if maior > palavra2:
    maior = maior;
else:
    maior = palavra2
if maior > palavra3:
    maior = maior
else:
    maior = palavra3
if palavra1 == palavra2 and palavra2 == palavra3:
    maior = "nenhuma, pois ambas são iguais"
print("Maior palavra =", maior)