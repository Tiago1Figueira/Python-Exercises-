"""
soma = 0
num = str(input('Informe um número:'))
if num > 0:
    for n in num:
        soma = soma + n
        print(f'A soma dos algarítmos do número {num} é igual a {soma}!')
else:
    print(f'Número inválido! Forneça números positivos!')
"""
soma = 0
numero = int(input('Informe um número inteiro e maior que 0:'))
if numero > 0:
    for i in str(numero):
        soma = soma + i
        print(f'A soma dos algarísmos é {soma}!')
else:
    print('Número inválido!')
# há problemas entre 'int' e 'str'.