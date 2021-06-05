"""
#1
num = int(input('Informe um número:'))
for num in range(1, num+num):
    if num % 2 != 0:
        impares = num
        print(impares, end=' ')

#2
impares = 0
num = int(input('Informe um número inteiro:'))
for i in range(0, num + 1):
    if i % 2 != 0:
        impares = i
        print(impares, end=' ')

#3
"""
impares = 0
num = float(input('Informe um número inteiro:'))
while num != int(num):
    print('Número inválido!')
    num = float(input('Informe um número inteiro:'))
    for i in range(0, int(num) + 1):
        if i % 2 != 0:
            impares = i
            print(impares,end=' ')






