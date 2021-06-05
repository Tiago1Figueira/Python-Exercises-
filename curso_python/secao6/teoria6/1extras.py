"""
#1
sleep ex11
from time import sleep
num = int(input('Informe um número inteiro e positivo:'))
while num < 0:
    print('Atenção: o número deve ser inteiro e positivo! ')
    num = int(input('Informe um número inteiro e positivo:'))
for i in range(0, num + 1):
    sleep(0.2)
    print(i, end=' ')

#2
fatorial ex.29
import math
num = int(input('Digite um número inteiro\nn = '))
s = 0
for n in range(1, num + 1):
    s = s + n / (math.factorial(n * 2))
print('O resultado desta série é ', s)

#3
ex15
while True:
    num = float(input('\nInforme um número inteiro ímpar:'))
    while num % 2 == 0 or num < 0 or num != int(num):
        print('Número inválido!')
        num = float(input('\nInforme um número inteiro ímpar:'))
    for i in range(1, int(num + 1)):
        print(i, end=' ')
#só recebe numero int, mas é necessário colocar "float" na pergunta de recebimento para que o python receba o
#número float e dê a mensagem de 'número inválido'. Foi necessário, também , colocar um cast 'int' no loop for
#(ao se receber um numero float o python não consegue iterá-lo no loop for; somente int é interávelo no loop for. Ou
entao o número float entra no loop for, mas aí a limitação de ser somente numero int num != int(num) nao deixa
#o processamento continuar dando erro!)
#para que não aparecesse uma mensagem de erro, mas tão somente a mensagem de 'numero invalido'.

#4
ex16
num = int(input('Informe um número inteiro positivo e ímpar:'))
while num % 2 == 0 or num < 0:
    num = int(input('Informe um número inteiro positivo e ímpar:'))
for i in range(num, 0, -1):
        if i % 2 !=0:
            print(i, end= ' ')

" while num % 2 == 0 or num < 0:"
Aqui deve-se fixar a diferença entre or e and. Qdo se usa o 'or' o código aceita o processamento,pois entende
que o número recebido é diferente de par ou negativo.
" while num % 2 == 0 and num < 0:"
Se o and for usado aqui, o processamento ficará errado, pois o sistema entenderá que somente o número " par e
menor que 0 " e.g.(-2) deverá ser travado. Caso contrário, o sistema deixará o número par ser processado mesmo
o exercício pedindo números ímpares para ser processado.

#5
ex6
lista = [ ]
for i in range(1,11):
    numero = int(input(f'Informe o {i}° número inteiro:'))
    lista.append(i)
print(f'A média dos números informados é {sum(lista) / len(lista)}!')
# veja como a lista e a média foram feitas!

#6
#37
for i in range(1000,10_000):
    w = str(i)
    x = w[0:2]
    y = w[2:]
    z = int(x) + int(y)
    if z ** 2 == i:
        print(i)
#7
#38
for horas in range(0,4):
    for minutos in range(1,55):
        for segundos in range(1,60):
            print(horas,minutos,segundos)
#aqui um loop for alimenta o outro. O loop mais baixo (segundos) alimenta os acima dele(horas, minutos)

#8
#50
cont = 0
chico = 150
ze = 110
while ze < chico:
    chico += 2
    ze += 3
    cont += 1
print(f'Levará {cont} anos pra Zé ser maior que Chico!')

#9
#61
lista = [ ]
for i in range(1, 999 + 1):
    for j in range(1, 999 + 1):
        res = i * j
        res1 = str(res)
        res1 = res1[::-1]
        res1 = int(res1)
        if res1 == res:
            lista.append(res)
print(max(lista))
"""

