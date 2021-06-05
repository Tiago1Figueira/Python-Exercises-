"""
#1
lista = [ ]
for i in range(1,51):
    c = (i + 5 * i) % (i + 1)
    lista.append(c)
print(lista)

for indice, i in enumerate(lista):
    print(indice, i)# imprime todos os elementos colocando índices, usando o 'for'.

#2
vetor = [ ]
for i in range(1, 51):
    c = (i + 5 * i) % (i + 1)
    vetor.append(c)
print(vetor)

for indice, i in enumerate(vetor):
    print(indice, i)

"""
#3
lista = [ ]
for i in range(1,11):
    lista.append(i)
for indice, i in enumerate(lista):
    print(indice, i)






















