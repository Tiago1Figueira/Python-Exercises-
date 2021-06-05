"""
#1
lista = []
lista_pares = []
lista_impares = []
for i in range(1,7):
    num = int(input(f'Informe o {i}° número:'))
    lista.append(num)
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
print(lista_pares)
print(sum(lista_pares))
print(lista_impares)
print(len(lista_impares))

#2
vetor = [ ]
pares = [ ]
impares = [ ]
while True:
    print('#'*100)
    for i in range(1,7):
        num = float(input(f'Informe o {i}° número:'))
        vetor.append(num)
    for num in vetor:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    print('RESULTADOS:')
    print(f'Números Pares: {pares}\nNúmeros Ímpares: {impares}\n'
          f'Números Pares Somados: {sum(pares)}\nQuantidade Números Ímpares: {len(impares)}')
    vetor.clear()
    pares.clear()
    impares.clear()
"""
#3
vetor = [ ]
pares = [ ]
impares = [ ]
while True:
    print('#'*100)
    for i in range(1,7):
       num = float(input(f'Informe o {i}° número:'))
       vetor.append(num)
    for i in vetor:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    print('Resultados:')
    print(f'Números pares {pares}\nNúmeros ímpares {impares}\nSoma números pares {sum(pares)}\n'
          f'Quantidade números ímpares {len(impares)}')
































