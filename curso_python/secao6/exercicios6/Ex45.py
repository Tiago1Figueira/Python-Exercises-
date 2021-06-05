"""
#1
print('='*60, 'CONVERSÃO KM/H PARA M/S E VICE-VERSA', '='*60)
print('N° 1 km/h para m/s:')
print('N° 2 m/s para km/h:')
print('Nº 3 finaliza programa:')
opc = int(input('OPÇÃO: 1, 2 ou 3 ? N°'))
while opc >=1 and opc <=3:
    if opc == 1:
        kmh = float(input('Informe quantos km/h quer converter em m/s:'))
        valor = kmh * 3.6
        print(f'O valor de {kmh} km/h é igual a {valor:.2f} m/s !!')
    if opc == 2:
        ms = float(input('Informe quantos m/s quer converter em km/h:'))
        valor = ms / 3.6
        print(f'O valor de {ms} m/s é igual a {valor:.2f} km/h !!')
    if opc == 3:
        print('Você saiu!!')
    break

#2
print('=' * 55, 'Converta km/h para m/s e vice-versa', '=' * 65)
print('1- KM/H PARA M/S:\n2- M/S PARA KM/H:\n3- FINALIZAR PROGRAMA:')
opt = int(input('Informe o número escolhido: 1, 2 ou 3 - N°'))
while True:
    if opt < 1 or opt > 3:
        print('ATENÇÃO: opções entre 1, 2 e 3!')
        opt = int(input('Informe o número escolhido: 1, 2 ou 3 - N°'))
    if opt == 1:
        kmh = float(input('Informe quantos km/h deseja converter para m/s: '))
        ms = kmh / 3.6
        print(f'O valor de {kmh} km/h é igual a {ms} metros/s! ')
    if opt == 2:
        ms = float(input('Informe quantos m/s deseja converter para km/h:'))
        kmh = ms * 3.6
        print(f'O valor de {ms} metros/s é igual a {kmh} km\h:')
    if opt == 3:
        print('Você finalizou!')
        break
    print('=' * 55, 'Converta km/h para m/s e vice-versa', '=' * 65)
    print('1- KM/H PARA M/S:\n2- M/S PARA KM/H:\n3- FINALIZAR PROGRAMA:')
    opt = int(input('Informe o número escolhido: 1, 2 ou 3 - N°'))
"""
#3
while True:
    print('='*50, 'CONVERSÃO M/S PARA KM/H E VICE-VERSA!','='*50)
    print('1- KM/h para M/s\n2- M/s para KM/h\n0- finaliza programa')
    opt = float(input('Informe uma opção:N°'))
    while opt != int(opt):
        print('Número inválido!')
        opt = float(input('Informe uma opção:N°'))
    while int(opt) < 0 or int(opt) > 2:
        print('Número inválido!')
        opt = float(input('Informe uma opção:N°'))
    if opt == 1:
        kmh = float(input('Informe os KM/h:'))
        ms = kmh / 3.6
        print(f'{kmh} quilômetros por horas são {ms} metros por segundo!')
    elif opt == 2:
        ms = float(input('Informe os M/s:'))
        kmh = ms * 3.6
        print(f'{ms} metros por segundo são {kmh} quilômetros por hora!')
    elif opt == 0:
        print('Você saiu!')
        break


















