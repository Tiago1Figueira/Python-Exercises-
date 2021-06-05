while True:
    print('=' * 150)
    valor_hora = float(input('Informe o valor a ser pago por hora:'))
    horas = int(input('Informe o número de horas trabalhadas:'))
    salario = valor_hora * horas
    salario_final = salario + (salario * 0.10)
    print(f'O valor do seu salário salário final é {salario_final:.2f} !')
    



