"""
#1
num = input('Informe um número entre 100 e 999:')
for n in num:
    print(n, end=' ')

#2
num = input('Informe um número entre 100 a 999:')
for i in num:
    print(i, end=' ')
"""
#3
while True:
    num = float(input('\nInforme um número inteiro entre 100 e 999:'))
    while num < 100 or num > 999 or num != int(num):
        print('Número inválido!')
        num = float(input('\nInforme um número inteiro entre 100 e 999:'))
    for i in str(num):
        print(i)

#checar pq o a casa decimal está aparecendo no print.





