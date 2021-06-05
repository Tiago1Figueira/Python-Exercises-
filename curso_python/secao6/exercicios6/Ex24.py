"""
#1
soma = 0
num = int(input('Informe um número positivo:'))
while num <=0 :
    num = int(input('Informe um número positivo:'))
for i in range(1, num):
    if num % i == 0:
        soma += i
print(soma, end=' ')

#2
soma = 0
num = int(input('Informe um número inteiro e positivo:'))
while num <= 0:
    num = int(input('Informe um número inteiro e positivo:'))
for i in range(1, num +1):
    if num % i == 0:
        soma += i
print(soma)

"""
#3
soma = []
while True:
    num = float(input('Informe um número inteiro e positivo:'))
    while num <=0 or num != int(num):
        print('Número inválido!')
        num = float(input('Informe um número inteiro e positivo:'))
    for i in range(1, int(num)):
        if num % i == 0:
            soma.append(i)
    print(f'A soma dos divisores do número {num} é {sum(soma)}!')



























