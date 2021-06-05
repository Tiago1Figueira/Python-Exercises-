"""
#1
soma = 0
num1 = int(input('Informe o primeiro número do intervalo:'))
num2 = int(input('Informe o segundo número do intervalo:'))
while num1 > num2:
    print('Erro: intervalo inválido!!')
    break
for i in range(num1, num2 + 1):
    if i % 2 != 0:
        soma += i
print(soma, end= ' ')

#2
soma = 0
num1 = int(input('Informe o primeiro número do intervalo:'))
num2 = int(input('Informe o segundo número do intervalo:'))
while num1 > num2:
        print('Intervalo de valores inválidos!!')
        break
for i in range(num1, num2):
    if i % 2 != 0:
        soma += i
print(f'A soma dos números ímpares no intervalo dos números {num1} e {num2} é igual a {soma}!')
"""
#3
# devido ao while True inicial a variável soma fica somando os ímpares de todos os valores dados.
soma = 0
while True:
    print('='*80)
    num1 = float(input('Informe o primeiro número do intervalo:'))
    while num1 < 0 or num1 != int(num1):
        print('Atenção: digite número inteiro e positivo!')
        num1 = float(input('Informe o primeiro número do intervalo:'))

    num2 = float(input('Informe o segundo número do intervalo:'))
    while num2 < 0 or num2 != int(num2):
        print('Atenção: digite número inteiro e positivo!')
        num2 = float(input('Informe o segundo número do intervalo:'))

    while num1 > num2:
        print('Intervalo de valores inválidos!')
        break
    else:
        for i in range(int(num1), int(num2)):
            if i % 2 != 0:
                soma += i
    print(f'A soma dos números ímpares do intervalo dado é {soma}!')





















