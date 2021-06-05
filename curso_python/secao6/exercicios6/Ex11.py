"""
#1
from time import sleep
n = int(input('Informe um número:'))
for i in range(0, n + 1):
    sleep(0.2)
    print(i, end= ' ')

#2
from time import sleep
num = int(input('Informe um número inteiro e positivo:'))
while num < 0:
    print('Atenção: o número deve ser inteiro e positivo! ')
    num = int(input('Informe um número inteiro e positivo:'))
for i in range(0, num + 1):
    sleep(0.2)
    print(i, end=' ')
"""
#3
while True:
    num = float(input('\nInforme um número:'))
    while num != int(num):
        print('Número inválido!')
        num = float(input('\nInforme um número:'))
    for i in range(0, int(num) + 1):
        print(i,end=' ')





















