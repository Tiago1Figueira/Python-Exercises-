"""
#1
lista = []
cont = 0
valores = 0
media = ' '
for i in range(1,6):
    num = int(input(f'Informe o {i}° número:'))
    lista.append(num)
    cont += 1
    valores += num
    #media = valores / cont
    media = sum(lista) / len(lista)
print(lista)
print(max(lista))
print(min(lista))
print(media)
"""
#2
lista = [ ]
while True:
    print('='*80)
    for i in range(1,6):
        num = float(input(f'Informe o {i}° número:'))
        lista.append(num)
    print(f'Números digitados {lista}\nMaior número {max(lista)}\n'
          f'Menor número {min(lista)}\nMédia {sum(lista)/ len(lista)}')
    lista.clear()














