"""
#1
print('=' * 150)
vet = []
for i in range(1,6):
    num = float(input(f'Informe o {i}° número:'))
    vet.append(num)
print('=' * 60, 'ESCOLHA OPÇÕES', '=' * 60)
print('Escolha - 0, 1, 2: ' )
print('0= finalizar\n1= mostrar ordem direta\n2= mostrar ordem inversa')
opt = int(input(f'Opção: n°'))
while True:
    if opt == 0:
       print('Você finalizou o programa!!')
       break

    if opt == 1:
        print(vet)
        break

    if opt == 2:
        vet.reverse()
        print(vet)
        break
    else:
        print('Atenção: opções 0, 1, 2:')
        print('0= finalizar\n1= mostrar ordem direta\n2= mostrar ordem inversa')
        opt = int(input(f'Opção: n°'))

# a opção 2 está duplicando o os números digitados no vetor e mostrando isso no print, quando os números são digitados em ordem direta.


#2
print('=' * 150)
vet = []
for i in range(1,6):
    num = float(input(f'Informe o {i}° número:'))
    vet.append(num)
print('=' * 60, 'ESCOLHA OPÇÕES', '=' * 60)
print('Escolha - 0, 1, 2: ' )
print('0= finalizar\n1= mostrar ordem direta\n2= mostrar ordem inversa')
opt = int(input(f'Opção: n°'))
while True:
    if opt == 0:
       print('Você finalizou o programa!!')
       break
    if opt == 1:
        vet.sort( )
        print(vet)
        vet.clear()
        print('=' * 150)
        for i in range(1, 6):
            num = float(input(f'Informe o {i}° número:'))
            vet.append(num)
        print('=' * 60, 'ESCOLHA OPÇÕES', '=' * 60)
        print('Escolha - 0, 1, 2: ')
        print('0= finalizar\n1= mostrar ordem direta\n2= mostrar ordem inversa')
        opt = int(input(f'Opção: n°'))

    if opt == 2:
        vet.reverse( )
        print(vet)
        vet.clear()
        print('=' * 150)
        for i in range(1, 6):
            num = float(input(f'Informe o {i}° número:'))
            vet.append(num)
        print('=' * 60, 'ESCOLHA OPÇÕES', '=' * 60)
        print('Escolha - 0, 1, 2: ')
        print('0= finalizar\n1= mostrar ordem direta\n2= mostrar ordem inversa')
        opt = int(input(f'Opção: n°'))

    if opt < 0 or opt > 2:
        print('Atenção: opções 0, 1, 2:')
        print('0= finalizar\n1= mostrar ordem direta\n2= mostrar ordem inversa')
        opt = int(input(f'Opção: n°'))

"""
#3
vetor = [ ]
while True:
    print('='*80)
    for i in range(1,6):
        num = float(input(f'Informe o {i}° número: '))
        vetor.append(num)
    print('Opções:\n0-Finaliza Programa\n1-Ordem Direta\n2-Ordem Invertida')
    opt = float(input('Informe uma opção: N° '))
    while opt < 0 or opt > 2 or opt != int(opt):
        print('Número inválido!')
        opt = float(input('Informe uma opção: N° '))
    if int(opt) == 0:
        print('Você saiu!')
        break
    elif int(opt) == 1:
        vetor.sort()
        print(vetor[::])
    elif int(opt) == 2:
        print(vetor[::-1])
    vetor.clear()

































