"""
#1
podemos imprimir os elementos dos vetorA usando indices conforme abaixo:
vetorA = [1, 0, 5, -2, -5, 7]
print(vetorA[0])
print(vetorA[1])
print(vetorA[5])

#2
soma = 0
vetorA = [1, 0, 5, -2, -5, 7]
soma += vetorA[0] + vetorA[1] + vetorA[5]
print(f'O valor da soma dos índices pedidos é {soma}.')
vetorA.pop(4)
vetorA.insert(4, '100')
print(f'Após a modificação do índice 4 a lista "vetorA" é {vetorA}')


#3
soma = 0
#a
vetorA = [1,0,5,-2,-5,7]
#b
soma += vetorA[0] + vetorA[1] + vetorA[5]
print(f'A soma dos números nos índices 0, 1 e 5 é {soma}!')
#c
vetorA.pop(4)
vetorA.insert(4,'100')
print(vetorA)
#d
for i in vetorA:
    print(i)

"""





















