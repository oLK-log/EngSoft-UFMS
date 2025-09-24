#Dada uma string, calcular:
#Vogais Maiusculas e Vogais minusculas
#Consoantes MAiusculas e consoantes minusculas
#dígitos
#informações importantes:
#maiúsculas estão entre 65 e 90(incluindo extremos)
#minúsculas estão entre 97 e 122(incluindo extremos)
#a=97,e=101,i=105,o=111,u=117,A=65,E=69,I=73,O=79,U=85 

text = str(input("Digite a palavra:\n"))
vMai = 0
vMin = 0
cMai = 0
cMin = 0
digito = 0
vogaisMai = "AEIOU"
vogaisMin = "aeiou"

for caractere in text:
    codigo = ord(caractere);
    #Se Maiusculo
    if codigo >= 65 and codigo <= 90:
        if caractere in vogaisMai:
            vMai += 1;
        else:
            cMai += 1;
    #se minusculo
    elif codigo >= 97 and codigo <= 122:
        if caractere in vogaisMin:
            vMin += 1
        else:
            cMin += 1
    elif codigo >=48 and codigo <= 57:
        digito += 1;
#Imprimir
print('Num. Vogais Maiúsculas = {0:d}'.format(vMai))
print('Num. Consoiantes Maiúsculas = {0:d}'.format(cMai))
print('Num. Vogais Minúsculas = {0:d}'.format(vMin))
print('Num. Consoantes Minúsculas = {0:d}'.format(cMin))
print('Num. Dígitos = {0:d}'.format(digito))