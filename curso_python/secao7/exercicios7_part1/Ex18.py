"""
#1
vet = []
multiplos = []
contador = 0
for i in range(10):
    numero = int(input(f'Digite o número {i+10}/10:'))
    vet.append(numero)
numero = int(input('Entre os números digitados, mostre os múltiplos de: '))
for valor in vet:
    if valor % numero == 0:
        contador = contador + 1
        multiplos.append(valor)
if contador == 0:
    print(f'\nNão existem múltiplos do {numero}´)
else:
    print(f'\nExistem {contador} múltiplos do {numero}\nSão os seguintes:')
    for valor in multiplos:
        print(valor)
"""
#2
vetor = [ ]
multiplo_4 = [ ]
for i in range(1,11):
    num = float(input(f'Informe o {i}° número:'))
    vetor.append(num)
while True:
    print('=' * 80)
    num2 = float(input(f'Informe outro número e saiba se ele é divisível dos números digitados:'))
    for i in vetor:
        if i % num2 == 0:
            multiplo_4.append(i)
    print(f'Há {len(multiplo_4)} múltiplo(s) do {num2} nos números digitados, ou seja, {multiplo_4}.')
    multiplo_4.clear()
#há outra forma de se fazer a parte apos o 'while True' desse exercício?






















