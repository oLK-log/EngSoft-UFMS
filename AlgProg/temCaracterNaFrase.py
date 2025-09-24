#Quantas vezes um caracter aparece na palavra
#não fazer distinção entre maiuscula e minuscula
#entrada: str text
igual = 0
text = input("Digite a palavra:\n");
caractere = input("Digite o caractere:\n");
caracterI = "";
if ord(caractere) >= 65 and ord(caractere) <= 90:
    caracterI = chr(ord(caractere) + 32)
else:
    caracterI = chr(ord(caractere) - 32)

for car in text:
    if car == caractere or car == caracterI:
        igual += 1;
        
print(igual)




#for letra in text:
 #   if ord(letra) >= 65 and ord(letra) <= 90:
  #      letraI = chr(ord(letra) + 32)
   #     print(letraI)
    #else:
     #   letraI = chr(ord(letra) - 32)
      #  print(letraI)
#print(igual)
        
        
