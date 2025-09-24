#procurando Substrings numa sequencia de DNA
#{A,T,C,G}
#A entrada é uma string e 3 subString
#string stext, sst1, sst2, sst3
print("Leia uma sequencia de DNA:")
stext = input()
print("Leia a subsequencia 1")
sst1 = input()
print("Leia a subsequencia 2")
sst2 = input()
print("Leia a subsequencia 3")
sst3 = input()
#temos que contar quantas vezes cada sub aparece
num1 = stext.count(sst1)
num2 = stext.count(sst2)
num3 = stext.count(sst3)
print(' {0:s} - {1:d} \n {2:s} - {3:d} \n {4:s} - {5:d}'.format(sst1, num1, sst2, num2, sst3, num3))