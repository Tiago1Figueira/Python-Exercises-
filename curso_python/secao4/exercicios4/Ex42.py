grat = 0.05
imposto = 0.07
while True:
    print('=' * 150)
    salario_base = float(input('Informe o salário base:'))
    salario_liquido = salario_base - (salario_base * imposto)
    salario_receber = salario_liquido + (salario_liquido * grat)
    print(f'O seu salário será {salario_receber}!')



