"""
# como fazer para que o print não repita as 4 frases, mas tão somente uma frase com 4 números?
#1
num = int(input('Informe um número positivo:'))
while num <=0:
    num = int(input('Informe um número positivo:'))
for i in range(1, num + 1):
    if num % i == 0:

        print(f'Os divisores do número {num} são {i}.')

#2
num = int(input('Informe um número positivo:'))
while num < 0:
    num = int(input('Informe um número positivo:'))
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end='  ')

#3
while True:
    num = float(input('\nInforme um número positivo e inteiro:'))
    while num < 0 or num != int(num):
        print('Número inválido!')
        num = float(input('\nInforme um número positivo e inteiro:'))
    for i in range(1, int(num) +1):
        if num % i == 0:
            print(i, end=' ')
"""

#4





























