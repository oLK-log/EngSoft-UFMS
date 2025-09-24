#ler 3 strings
#ordenar as strings em descrecente
#não pode ser usado for, while, sort, sorted

st1 = input()
st2 = input()
st3 = input()

#para 1
if st1 > st2:
    if st1 > st3:
        n1 = st1
        if st3>st2:
            n2 = st3
            n3 = st2
        else:
            n2 = st2
            n3 = st3
    else:
        n1 = st3
        n2 = st1
        n3 = st2
else:
    if st2 > st3:
        n1 = st2
        n2 = st3
        n3 = st1
    else:
        n1 = st3
        n2 = st2
        n3 = st1

print(n3,n2,n1)