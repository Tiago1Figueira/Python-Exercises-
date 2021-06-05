"""
#1
#ex8
vetor = [ ]
for i in range(1,7):
    num = float(input(f'Informe o {i}° número:'))
    while num != int(num):
        print('Número inválido!')
        num = float(input(f'Informe o {i}° número:'))
    vetor.append(num)

print(vetor[::-1])    #0 aqui o print é usado na reversão da posição dos números.
vetor.reverse()       #1 aqui o print não é usado, mas somente depois disso na linha abaixo!
print(vetor)

#2
#ex18
for i in range(10):
    numero = int(input(f'Digite o número {i+10}/10:'))
    vet.append(numero)

#3
lista = [ ]
for i in range(1,11):
    lista.append(i)
for indice, i in enumerate(lista):
    print(indice, i)

#4
lista = [ 1,2,3,4,5,6,7,8,9,10]
for i,item in enumerate(lista):
    if (i+1) % 4 == 0:
        print(item)
    else:
        print(item,end=' ')

#5
#ex12
vetor = [ ]
print('#'*100)
for i in range(1,11):
    num = float(input(f'Informe o {i}° número:'))
    vetor.append(num)
    for i in vetor:
        if i < 0:
            vetor.insert(vetor.index(i), 0)
            vetor.pop(vetor.index(i))
print(f'Os números digitados foram {vetor}. ')
vetor.clear()


#6
#ex25
vetor = [ ]
for i in range(1,101):
    if i % 7 != 0 and str(i)[-1] != '7':
        vetor.append(i)
print(f'Lista 1 a 100 sem divisores de 7 ou terminados em 7 {vetor}! ')

#7
#ex30
vetor1 = [1,2 ]
vetor2 = [1,3 ]
print(vetor1)
print(vetor2)
print(set(vetor1).intersection(vetor2))        # 'set' transforma a lista em set e dái fazemos a INTERSECTION.
print(f'Vetor1 {vetor1}\nVetor2 {vetor2}\nVetor3 {vetor3}')

#8
#ex31
vetor1 = [1,2 ]
vetor2 = [1,3 ]
print(vetor1)
print(vetor2)
vetor3 = (set(vetor1).union(vetor2))      # 'set' transforma a lista em set e dái fazemos a UNION.
print(f'Vetor1 {vetor1}\nVetor2 {vetor2}\nVetor3 {vetor3}')

#9
estudantes_python = {'Marcos', 'Patrícia','Ellen', 'Pedro', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patrícia'}
unicos2 = estudantes_java.union(estudantes_python)
print(unicos2)
#{'Ellen', 'Gustavo', 'Júlia', 'Pedro', 'Marcos', 'Guilherme', 'Fernando', 'Patrícia', 'Ana'}
"""
#10




























