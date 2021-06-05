"""
#1
cont_numeros_lidos = 0
cont_pares = 0
print('N° 1000 finaliza programa!!')
num = int(input('Informe um número:'))
while num != 1000:
    num = int(input('Informe um número:'))
    cont_numeros_lidos += 1
    if num % 2 == 0:
        cont_pares += 1
print(f'O quantia de números lidos foi de {cont_numeros_lidos} vezes e o número de pares foi de {cont_pares}.')

#2
cont = 0
cont_pares = 0
num = int(input('Informe um número:'))
cont += 1
if num % 2 == 0:
    cont_pares += 1
while True:
    num = int(input('Informe um número:'))
    if num != 1000:
        cont += 1
        if num % 2 == 0:
            cont_pares += 1
    else:
        break
print(f'A quantia de números inseridos foi {cont} e a quantia de números pares foi {cont_pares}!')

#3
cont_total = 0
cont_pares = 0
while True:
    print('='*80)
    print('Digite 1000 para finalizar!')
    num = int(input('Informe um número:'))
    cont_total += 1
    if num != 1000:
        if num % 2 == 0:
            cont_pares += 1
    print(f'{cont_total} números foram digitados, dos quais {cont_pares} são pares!')
    else:
        break
#4
cont_total = 0
cont_pares = 0
while True:
    print('='*80)
    print('Digite 1000 para finalizar!')
    num = int(input('Informe um número:'))
    cont_total += 1
    if num != 1000:
        if num % 2 == 0:
            cont_pares += 1
    else:
        break
print(f'{cont_total} números foram digitados, dos quais {cont_pares} são pares!')
"""

#5
cont = 0
pares = []
while True:
    print('='*80)
    print('n° 1000 finaliza o programa!')
    num = float(input('Informe um número:'))
    cont += 1
    while num != int(num):
        print('Número inválido!')
        num = float(input('Informe um número:'))
    if int(num) != 1000:
        if num % 2 == 0:
            pares.append(num)
    else:
        break
print(f'{cont} números foram digitados e {len(pares)} é/são pares!')


















