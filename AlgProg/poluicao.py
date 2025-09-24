#leitura dada por n inteiro
#são 3 leituras
#a média é dada por n real
#menos que 35-Condição agradável, >35 and <= 60-Condição desagradável, >60 Cond Perigosa
#entrada
ind1 = int(input())
ind2 = int(input())
ind3 = int(input())
#media
med = (ind1 + ind2 + ind3) / 3
#Condição
if med < 35:
    cond = "Condição Agradável"
elif med >=35 and med <= 60:
    cond = "Condição Desagradável"
else:
    cond = "Condição Perigosa"
print(cond)