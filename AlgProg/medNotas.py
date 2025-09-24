#3 provas e 2 tabalhos
#float
#75% equivale as provas
#25% equivale aos trabalhos
#a aprox é feita da direita para esquerda
#aprox pra cima

nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
notaT1 = float(input())
notaT2 = float(input())

mediaProva = float(((nota1 + nota2 + nota3)/3)*0.75)
mediaTrab = float(((notaT1 + notaT2)/2)*0.25)
mediaFinal = mediaProva + mediaTrab

print('A nota final do aluno é {0:.1f}'.format(mediaFinal))
