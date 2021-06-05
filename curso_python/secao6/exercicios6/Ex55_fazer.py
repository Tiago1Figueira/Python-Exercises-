"""
#1
soma = 0
num = int(input('Informe um número maior que 1:'))
while num <=1:
    num = int(input('Informe um número maior que 1:N° '))
for i in range(1, num + 1):
    if i % 2 == 1 or i % 3 == 1 or i % 5 == 1 or i % 7 == 1 or \
        i % 11 == 1 or i % 13 == 1 or i % 17 == 1 or i % 19 == 1 or i % 23 == 1:
        soma += i
        print(i, end=' ')
print(f'A soma dos números primos até o número {num} é {soma}!')

# professor, não consigo resolver esse exercício. você poderia me dar uma luz?
"""

