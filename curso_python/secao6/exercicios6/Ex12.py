"""
#1
from time import sleep
num = int(input('Informe um número:'))
for i in range (num, -1, -1):
    sleep(0.3)
    print(i, end= ' ')

#2
from time import sleep
num = int(input('Informe um número:'))
while num < 0:
    print('Atenção: digitar número inteiro e positivo:')
    num = int(input('Informe um número:'))
for i in range(num, -1, -1):
    sleep(0.2)
    print(i, end=' ')
#3
while True:
    num = int(input('\nInforme um número:'))
    while num < 0:
        print('Atenção: número inválido!')
        num = int(input('Informe um número:'))
    for i in range(num, - 1 , -1):
        print(i,end= ' ')

"""
#4
while True:
    num = float(input('\nInforme um número inteiro:'))
    while num <= 0 or num != int(num):
        print('Número inválido!')
        num = float(input('Informe um número inteiro:'))
    for i in range(int(num), -1, -1):
        print(i,end=' ')

























