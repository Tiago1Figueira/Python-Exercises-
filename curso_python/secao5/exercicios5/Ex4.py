while True:
    num = int(input('Informe um número positivo:'))
    if num < 0:
        print('Atenção: número negativo! ')
        num = int(input('Informe um número positivo:'))
    else:
        raiz_quadrada = num ** 1/2
        quadrado = num ** 2
        print(f'O número {num} tem raiz quadrada igual a {raiz_quadrada} e seu quadrado é {quadrado}!')
