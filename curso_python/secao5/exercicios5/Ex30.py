lista = [ ]
while True:
    print('=' * 50, 'INFORME 3 NÚMEROS', '=' * 50)
    for i in range(1,4):
        num = float(input(f'Informe o {i}° número:'))
        lista.append(num)
        lista.sort()
    print(f'A lista crescente dos números dados é {lista}!')
    lista.clear()
