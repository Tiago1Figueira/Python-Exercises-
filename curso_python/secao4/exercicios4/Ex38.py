aumento = 0.25
while True:
    print('=' * 50, 'CALCULE VALOR DO SALÁRIO:', '=' * 50)
    sal = float(input('Informe um salário:'))
    sal_aumento = sal + (sal * aumento)
    print(f'O salário com 25% de aumento é {sal_aumento} reais!')
