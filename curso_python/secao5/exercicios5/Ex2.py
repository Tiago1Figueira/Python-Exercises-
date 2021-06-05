while True:
    print('=' * 50, 'CÁLCULO DA RAIZ QUADRADA', '=' * 50 )
    num = int(input('Informe um número positivo:'))
    if num >=0:
        raiz_quadrada = num ** 1/2
        print(f' A raiz quadrada do número {num} é {raiz_quadrada}')
        print('=' * 50, 'CÁLCULO DA RAIZ QUADRADA', '=' * 50)
    else:
        print(f'O número {num} é  inválido! ')

