"""
#1
vetor = [ ]
sem_repeticao = [ ]
for i in range(1, 6):#21
    num = int(input(f'Informe o {i}° número:'))
    vetor.append(num)
    if num in vetor and num not in sem_repeticao:#copiado
        sem_repeticao.append(num)
print(vetor)
print(sem_repeticao)
# copiado! Necessita explicação sobre and not in: se o número está em 'vetor' então não está em 'sem_repetição'. É isso?

#2
numeros_digitados = [ ]
numeros_nao_repetidos = [ ]
numeros_repetidos = [ ]
for i in range(1,5):
    num = float(input(f'Informe o {i}° número:'))
    numeros_digitados.append(num)
    if num in numeros_digitados not in numeros_nao_repetidos:
        numeros_nao_repetidos.append(num)
    else:
        numeros_repetidos.append(num)
print(f'Números repetidos {numeros_repetidos}')

#3
lis = []
for i in range(5):
    n = int(input(f'Digite {i}° número inteiro:'))
    lis.append(n)
for number in set(lis):
    print(number)

#4
lista = [ ]
for i in range(1,5):#20
    num = float(input(f'Informe o {i}° número:'))
    while num != int(num):
        print('Número inválido!')
        num = float(input(f'Informe o {i}° número:'))
    lista.append(num)
for i in lista:
    lista = set(lista)
print(lista)


"""
#5




























































