#texto: str
#palavra: str
#resposta: str
#tam: int
#i: int
#P1: Leia as strings e compute o tamanho
#P1 Leia o texto
texto = str(input())
#P1.2 Leia a palavra
palavra = str(input())
#P1.3 Calcule o tamanho do texto
tam = len(texto)
#P2: Encontre palavra em texto
#P 2.1 Inicialize os índices das strings
i = 0
resposta = 'não'
#P 2.2 Compare os caracteres da palavra com o texto
while i < tam-2:
    if texto[i] == palavra[0] and texto[i+1] == palavra[1] and texto[i+2] == palavra[2]:
        resposta = 'sim'
        i = tam
    else:
        i += 1
#Passo 3: Imprima o resultado
print(resposta)

#Pos: ('sim' and existes i em {0..tam-3}:texto[i]==palavra[0]
# and texto[i+1]==palavra[1] and texto[i+2]