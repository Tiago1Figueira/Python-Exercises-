"""
#1
lista = []
for i in range(1,7):
    num = int(input(f'Informe o {i}° número inteiro:'))
    lista.append(num)
for valores in lista:
    print(valores)
print(lista)

"""
#2
lista = [ ]
while True:
    print('='*80)
    for i in range(1,7):
        num = float(input(f'Informe o {i}° número:'))
        while num != int(num):
            print('Número inválido!')
            num = float(input(f'Informe o {i}° número:'))
        lista.append(num)
    print(f'O valor da soma dos números digitados é {sum(lista)}!')

















