"""
#1
soma = 0
fatorial = 1
n = int(input('Informe um número:'))
while n <=0:
    n = int(input('Informe um número:'))
for i in range(1, n+1):
    fatorial = fatorial * i
    soma += fatorial
    E = 1 + 1 / fatorial # aqui n é fatorial!
print(f'O número {n} gera o número E={E}.')
# conferir com o professor se o código está correto.

#2
"""

