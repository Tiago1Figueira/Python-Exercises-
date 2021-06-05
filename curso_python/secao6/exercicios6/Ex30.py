"""
#1
soma1 = 0
soma2 = 0
soma3 = 0
while True:
    print('='*80)
    num = float(input('Informe um número:'))
    while num <= 0 or num != int(num):
        print('Número inválido!')
        num = float(input('Informe um número:'))
    for i in range(1, int(num) + 1):
        sequencia1 = i
        sequencia2 = ((-1) ** i - 1 ) * i
        sequencia3 = (2*i) - 1
        soma1 += sequencia1
        soma2 += sequencia2
        soma3 += sequencia3
    print(f'A 1ª soma é {soma1}!\nA 2ª soma é {soma2}!\nA 3ª soma é {soma3}!')
"""
#2
soma1 = 0
soma2 = 0
soma3 = 0
while True:
    print('='*80)
    num = float(input('Informe um número:'))
    while num <=0 or num != int(num):
        print('Número inválido!')
        num = float(input('Informe um número:'))
    for i in range(1, int(num) + 1):
        sequencia1 = i
        sequencia2 = (-1 ** i-1) * i
        sequencia3 = 2 * i - 1
        soma1 += sequencia1
        soma2 += sequencia2
        soma3 += sequencia3
    print(f'A 1ª soma é {soma1}!\nA 2ª soma é {soma2}!\nA 3ª soma é {soma3}!')





