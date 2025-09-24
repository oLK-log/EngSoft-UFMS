#número de caracteres de um texto lido
#o espaço não é considerado
#não utilizar len
#entrada: str texto
#saída: int numberText
text = str(input("Digite o texto:\n"));
tamanho = 0;
numVogais = 0;
numConsoantes = 0;
numOutros = 0;
vogais = 'aeiouAEIOU'
for caractere in text:
    codigo = ord(caractere);
    if caractere != " ":
        tamanho += 1;
    if codigo >= 65 and codigo <= 90 or codigo >= 97 and codigo <= 122:
        if caractere in vogais:
            numVogais += 1;
        else:
            numConsoantes += 1;
    else:
        numOutros += 1;
        
print("O tamanho do texto é {0:d}. \n Vogais = {1:d} \n Consoantes = {2:d} \n Outros = {3:d}".format(tamanho, numVogais, numConsoantes, numOutros))