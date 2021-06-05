while True:
    print('=' * 50, 'CÁLCULO DOS 20% DO EMPRÉSTIMO:', '=' * 50)
    sal = float(input('Informe o valor do salário:'))
    prestacao = float(input('Informe o valor da prestação:'))
    if prestacao > sal * 20/100:
        print('Empréstimo não concedido!')
    else:
        print('Empréstimo concedido!')
