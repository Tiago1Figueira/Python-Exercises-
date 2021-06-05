"""
#1
soma = 0
soma1 = 0
soma_total = (soma1)**2
diferenca = soma_total - soma
n = 100
for i in range(0, n+1):
    soma += (i**2)
    soma1 += i
    soma_total = (soma1)**2
    diferenca = soma_total - soma

print(f'O valor da diferença entre a soma dos quadrados dos {n} números naturais e o quadrado da soma é '
      f'{soma_total} - {soma} = {diferenca}!')

#2
soma = 0
soma_1 = 0
soma_2 = 0
n1 = 1
n2 = 100
for i in range(n1, n2 + 1):
    soma += i**2
    soma_1 += i
    soma_2 = (soma_1)**2
    diferenca = soma_2 - soma

print(f'A diferença entre a soma dos quadrados dos {n2} primeiros números e o quadrado da soma é '
      f'{soma_2} - {soma} = {diferenca}!!')

"""
#3
soma = 0
soma_quadrado = 0
quadrado_soma = 0
n1 = 1
n2 = 11
for i in range(n1, n2):
    soma_quadrado += i**2
    soma += i
    quadrado_soma = (soma)**2
diferenca = quadrado_soma - soma_quadrado
print(f'A diferença é {diferenca}')



