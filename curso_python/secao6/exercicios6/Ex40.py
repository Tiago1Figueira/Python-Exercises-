"""
#1
lista = []
num = int(input('Informe um número inteiro:'))
lista.append(num)
while True:
    num = int(input('Informe um número inteiro:'))
    if num >= 0:
        lista.append(num)
    else:
        break
print(f'Os números digitados foram {lista}')
print(f'O maior número digitado foi {max(lista)} e o menor {min(lista)}')
# checar com o professor por que o primeiro número da sequência está sendo excluído da lista de números.

#2
lista = []
num = int(input('Informe um número inteiro:'))
lista.append(num)
while True:
    num = int(input('Informe um número inteiro:'))
    if num >= 0:
        lista.append(num)
    else:
        print('Você digitou um número negativo! Programa terminado!')
        break
print(f"Dos números digitados {max(lista)} é o maior e {min(lista)} é o menor!")

#3
lista = [ ]
while True:
    print('='*80)
    num = int(input('Informe um número:'))
    lista.append(num)
    while True:
        num = int(input('Informe um número:'))
        if num >= 0:
            lista.append(num)
        else:
            print('Vocẽ saiu!')
            break
    print(f'Maior {max(lista)} Menor {min(lista)}!')
    lista.clear()


"""
#4
lista = [ ]
while True:
    num = float(input('Informe um número:'))
    if num < 0:
        print('Você saiu!')
        break
    else:
        lista.append(num)
print(f'Maior {max(lista)} Menor {min(lista)}!')










