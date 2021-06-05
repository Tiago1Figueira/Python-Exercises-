"""
#1
lista = []
pares = []
for i in range(1,11):
    num = int(input(f'Informe o {i}° número:'))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
        len(pares)
print(pares)
print(f'Neste grupo de números há {len(pares)} valores pares.')

"""
#2
pares = [ ]
while True:
    print('='*80)
    for i in range(1,5):
        num = float(input(f'Informe o {i}° número:'))
        while num != int(num):
            print('Número inválido!')
            num = float(input(f'Informe o {i}° número:'))
        if int(num) % 2 == 0:
            pares.append(num)
    print(f'Quantia de números pares: {len(pares)}\nNúmeros pares: {pares}')
    pares.clear()


