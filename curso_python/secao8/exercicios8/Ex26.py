def somatoria(num):
    soma = 0
    for i in range(1, num + 1):
        soma += i
    return f'A somatória dos números de 1 até {num} é {soma}! '

a = int(input('Informe um número:'))

print(somatoria(a))


