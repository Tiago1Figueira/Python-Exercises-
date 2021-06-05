"""
#1
num = int(input('Informe um número inteiro e par:'))
while num <=0:
    num = int(input('Atenção: Informe um número inteiro e par:'))
    for i in range(num, -1, -1):
        print(i, end=' ')

#2
num = int(input('Informe um número inteiro, positivo e par:'))
while num < 0:
    num = int(input('Informe um número inteiro, positivo e par:'))
for i in range(num, -1, -1):
    if i % 2 == 0:
        print(i, end=' ')
"""
#3
while True:
    num = float(input('\nInforme um número inteiro e par:'))
    while num % 2 != 0 or num != int(num):
        print('Número inválido!')
        num = float(input('\nInforme um número inteiro e par:'))
    for i in range(int(num), -1, -1):
        print(i, end=' ')











