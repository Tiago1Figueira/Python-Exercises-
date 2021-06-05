"""
#1
soma = 0
soma_pares = 0
lista = []
cont = 0
num = float(input('Informe um número:'))
lista.append(num)
cont += 1
soma += num
while True:
    num = float(input('Informe um número:'))
    if num != 0:
        soma += num
        cont += 1
        media = soma / cont
        lista.append(num)
        if num % 2 == 0:
            soma_pares += num
    else:
        break
print(f'Seguem os dados pedidos:\n1- Soma dos números é: {soma}\n2- Quantidade de números é: {cont}\n'
      f'3- Média dos números é: {media:.2f}\n4- Maior número é: {max(lista)}\n5- Menor Número é: {min(lista)}\n'
      f'6- Soma números pares é: {soma_pares}.')

# Professor, arrumei o problema relacionado ao 0, que consta no relato acima, usando o "while True" e "if/else".  Contudo,
# ainda um problema persiste: estou repetindo o comando ' soma, cont, media e lista.append ' nas linhas 6 a 8, para que o
#primeiro número digitado faça parte dos cálculo. Essa é a melhor forma de colocar o primeiro número digitado no loop?

#2
soma = 0
qtd = 0
lista = []
par = 0
cont_par = 0
num = float(input("Informe um número:" ))
lista.append(num)
soma += num
qtd += 1
while True:
    if num !=0:
        num = float(input("Informe um número:"))
        lista.append(num)
        soma += num
        qtd += 1
        media = soma / qtd
        if num % 2 == 0:
            cont_par += 1
            par += num
    else:
        break
print(f'A soma dos números é {soma}!')
print(f'A quantidade de números digitados é de {qtd} números!')
print(f'A média dos números foi {media:.2f}!')
print(f'O maior número digitado foi {max(lista)} e o menor foi {min(lista)}!')
print(f'A média dos números pares digitados é {par/ cont_par} ')
"""
#3
lista = [ ]
pares = [ ]
while True:
    num = float(input('Informe um número:'))
    if num == 0:
        print('Você saiu!')
        break
    elif num % 2 == 0:
        pares.append(num)
    lista.append(num)

print(f'1-Soma dos números {sum(lista)}!\n2-Total número digitados {len(lista)}!\n'
f'3-Média dos números {sum(lista)/ len(lista)}!\n4-Maior número {max(lista)}!\n5-Menor Número {min(lista)}!\n'
f'6-Média números pares {sum(pares) / len(pares)}!')


















