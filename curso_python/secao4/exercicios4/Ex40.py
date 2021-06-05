valor_hora = 30
ir = 0.08
while True:
    print('=' * 150)
    dias = float(input('Informe quantos dias foram trabalhados:'))
    salario = (dias * valor_hora)
    salario_desc = salario - (salario * ir)
    print(f'O valor do salário descontado do I.R. é {salario_desc:.2f}!')

