"""

#1
vetor = []
repetidos = []
for i in range(1, 5):#11
    num = int(input(f'Informe o {i}° número:'))
    vetor.append(num)
for i in vetor:
    if vetor.count(i) > 1 and i not in repetidos:
        print(f'O valor {i} repete na lista {vetor.count(i)} vezes.')

# pq o print está aparecendo 2 vezes qdo um número repetido aparece?
#volte a estudar esse comando!!
# copiado! Necessita explicação sobre and not in: se o número está em 'vetor' então não está em 'sem_repetição'. É isso?

#2 exercicio dificil!
vetor = []
repetidos = []
for i in range(1, 5):#11
    num = int(input(f'Informe o {i}° número:'))
    vetor.append(num)
for i in vetor:
    if vetor.count(i) > 1 and i not in repetidos:
print(f'O valor {i} repete na lista {vetor.count(i)} vezes.')
# pq o print está aparecendo 2 vezes qdo um número repetido aparece?

#3
vetor_total = [ ]
vetor = []
vetor_rep = []
for i in range(1,6):
    num = float(input(f'Informe o {i}° número:'))
    vetor_total.append(num)
for i in vetor_total:
    if i not in vetor:
        vetor.append(i)
    else:
        vetor_rep.append(i)
print(f'Os números repetidos são {vetor_rep}!')

#4
numeros_digitados = [ ]
numeros_nao_repetidos = [ ]
numeros_repetidos = [ ]
while True:
    print('='*80)
    for i in range(1,5): #10
        num = float(input(f'Informe o {i}° número:'))
        numeros_digitados.append(num)
    for i in numeros_digitados:
        if i not in numeros_nao_repetidos:
            numeros_nao_repetidos.append(i)
        else:
            numeros_repetidos.append(i)
    print(f'Números repetidos {numeros_repetidos}')
    numeros_digitados.clear()
    numeros_repetidos.clear()
    numeros_nao_repetidos.clear()

#5
vetor = [ ]
vetor_sem_repetidos = [ ]
vetor_com_repetidos = [ ]
while True:
    print('='*80)
    for i in range(1,10):
        num = float(input(f'Informe o {i}° número:'))
        while num != int(num):
            print('Número inválido!')
            num = float(input(f'Informe o {i}° número:'))
        vetor.append(num)
    for i in vetor:
        if i not in vetor_sem_repetidos:
            vetor_sem_repetidos.append(i)
        else:
            vetor_com_repetidos.append(i)
    print(vetor_com_repetidos)


"""
#6
valor = [ ]
valor_nao_repetido = [ ]
valor_repetido = [ ]
while True:
    print('#'*100)
    for i in range(1,11):
        num = float(input(f'Informe o {i}° número:'))
        while num != int(num) or num<= 0:
            print('Número inválido!')
            num = float(input(f'Informe o {i}° número:'))
        valor.append(num)
    for i in valor:
        if i not in valor_nao_repetido:
            valor_nao_repetido.append(i)
        else:
            valor_repetido.append(i)
    print(f'Os números repetidos, dos que foram digitados, são {valor_repetido}!')
    valor.clear()
    valor_repetido.clear()
    valor_nao_repetido.clear()





















































































