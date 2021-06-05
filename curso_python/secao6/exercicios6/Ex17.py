"""
#1
soma = 0
num = int(input('Informe um número inteiro positivo: '))
while num <=0:
    num = int(input('Informe um número inteiro positivo: '))
for i in range(0, num + 1):
    soma += i
print(f'A soma de todos os números de 0 a {num} é {soma} !')

#2
soma = 0
num = int(input('Informe um número inteiro e positivo:'))
while num < 0:
    print('Atenção: digite número inteiro e positivo!')
    num = int(input('Informe um número inteiro e positivo:'))
for i in range(0, num + 1):
    soma += i
    print(soma, end=' ')

#3
soma = 0
while True:
    num = float(input('Informe um número inteiro e positivo:'))
    while num < 0 or num != int(num):
        print('Número inválido!')
        num = float(input('Informe um número inteiro e positivo:'))
    for i in range(0, int(num) + 1):
        soma = soma + i
    print(soma)

"""
#4
lista = []
while True:
    num = float(input('Informe um número inteiro e positivo:'))
    while num <= 0 or num != int(num):
        print('Número inválido!')
        num = float(input('Informe um número inteiro e positivo:'))
    for i in range(1, int(num) + 1):
        lista.append(i)
    print(sum(lista))
    lista.clear()














