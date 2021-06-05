"""
#1
maior = -9999
cont = 0
qtd = int(input('Quantos números serão lidos? N°:'))
for i in range(1, qtd +1):
    num = int(input(f'Informe o {i}°número: N° '))
    if num > maior:
        maior = num
        cont = 1
    elif maior == num:
        cont += 1
print(f'O maior número é {maior} e ele apareceu {cont} vez(es)!')
# O resultado da contagem do número de vezes que o maior aparece está incorreto.
# Aqui o maior aparece na primeira vez no if, e se repete nas outras vezes no elif.

#2
maior = 0
cont = 0
qtd = int(input('Informe a quantidade de números a ser inserida:'))
for i in range(1, qtd +1):
    num = int(input(f'Informe o {i}° número:'))
    if num > maior:
        maior = num
        cont = 1
    elif maior == num:
    cont += 1
print(f'O maior número digitado é {maior} e ele apareceu {cont} vezes!')
# O resultado da contagem do número de vezes que o maior aparece está incorreto.
# Aqui o maior aparece na primeira vez no if, e se repete nas outras vezes no elif.

#3
maior = 0
cont = 0
repetidos = 0
qtd = int(input('Informe a quantidade de números a ser inserida:'))
for i in range(1, qtd +1):
    num = input(f'Informe o {i}° número:')
    while num in maior:
        repetidos = num
        cont += 1
    else:
        num > maior
        maior = num

print(f'O maior número digitado é {maior} e ele apareceu {cont} vezes!')
# O resultado da contagem do número de vezes que o maior aparece está incorreto.

#4
maior = -999
lista = []
lista1 = []
qtd = int(input('Quantos números serão lidos? N°:'))
for i in range(1, qtd +1):
    num = int(input(f'Informe o {i}°número: N° '))
    lista.append(num)
    lista1=lista.count(max(lista))
print(f'O maior número é {max(lista)} e ele apareceu {lista1} vezes!')
# O resultado da contagem do número de vezes que o maior aparece está incorreto.


#5
lista = []
while True:
    qtd = int(input('Informe quantos números irá digitar:'))
    for i in range(1, qtd + 1):
        num = float(input(f'Informe o {i}° número:'))
        while num < 0 or num != int(num):
            print('Número inválido!')
            num = float(input(f'Informe o {i}° número:'))
        lista.append(int(num))
        maior = max(lista)
        print(f'O maior número é {maior} e apareceu {(len(maior))}!')

"""
maior = 0
cont = 0
while True:
    print('='*100)
    qtd = int(input('Informe quantos números irá inserir:'))
    for i in range(1, qtd + 1):
        num = int(input(f'Informe o {i}° número:'))
        if num > maior:
            maior = num
            cont = 1
        elif num == maior:
            maior = num
            cont += 1
    print(f'O maior número é {maior} e ele apareceu {cont} vez(es)!')








