"""
#1
num = int(input('Informe um número inteiro positivo e ímpar:'))
while num % 2 == 0 or num < 0:
    num = int(input('Informe um número inteiro positivo e ímpar:'))
for i in range(num, 0, -1):
        if i % 2 !=0:
            print(i, end= ' ')

#2
num = int(input('Informe um número inteiro, positivo e ímpar: '))
while num < 0 or num % 2 == 0:
    print('Atenção: digite número inteiro, positivo e ímpar:')
    num = int(input('Informe um número inteiro, positivo e ímpar: '))
for i in range(num, 0, -1):
    if i % 2 != 0:
        print(i, end=' ')
"""
#3
while True:
    num = float(input('\nInforme um número inteiro positivo ímpar:'))
    while num % 2 == 0 or num <= 0 or num != int(num):
        print('Número inválido!')
        num = float(input('\nInforme um número inteiro positivo ímpar:'))
    for i in range(int(num), -1, -1):
        print(i, end=' ')




























