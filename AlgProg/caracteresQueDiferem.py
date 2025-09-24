entrada = input()
string_invertida = ""
indice = len(entrada) - 1

# Inverter a string caractere por caractere
while indice >= 0:
    caractere = entrada[indice]
    string_invertida = string_invertida + caractere
    indice = indice - 1

print(string_invertida)

# Comparar a string original com a invertida e contar as diferenças
diferencas = 0
for i in range(len(entrada)):
    if entrada[i] != string_invertida[i]:
        diferencas += 1

print(diferencas)