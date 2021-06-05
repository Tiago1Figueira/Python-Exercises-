"""
#1
num = int(input('Informe um número maior que 1:'))
while num <=1:
    num = int(input('Informe um número maior que 1:'))
if num == 2:
    print(f'O número {num} é primo!')
if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or \
        num % 11 == 0 or num % 13 == 0 or num % 17 == 0 or num % 19 == 0 or num % 23 == 0:
    print(f'O número {num} não é primo!')

else:
    print(f'O número {num } é primo!')
# Não consigo colocar o número 2 no código identificado como número primo somente, pois aparece com não primo tambem.
# Fora o problema acima, o código está correto?

"""
num = int(input('Digite um número: '))
divisores = []

while num <= 1:
    print('Você deve informar um número maior do que 1.')
    num = int(input('Digite um número: '))
for i in range(1, num + 1):
    if num % i == 0:
        divisores.append(i)
if len(divisores) == 2 and divisores.__contains__(1) and divisores.__contains__(num):
    print(f'O número {num} é um número primo.')
else:
    print(f'O número {num} não é um número primo.')