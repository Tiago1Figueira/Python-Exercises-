"""
#1
lista = []
for i in range(1,6):
    num = float(input(f'Informe o {i}° número:'))
    lista.append(num)
print(lista)
print(f'O maior valor é {max(lista)} e a sua posição é {lista.index(max(lista))}!')
print(f'O menor valor é {min(lista)} e a sua posição é {lista.index(min(lista))}!!')

"""
#2
lista = [ ]
while True:
    print('='*80)
    for i in range(1,6):
        num = float(input(f'Informe o {i}° número:'))
        lista.append(num)
    print(f'Posição maior valor {lista.index(max(lista))}\n'
          f'Posição menor valor {lista.index(min(lista))}')
    lista.clear()

