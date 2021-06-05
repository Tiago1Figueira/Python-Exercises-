"""
#1
while True:
    print('=' * 150)
    numero = input('Informe um número inteiro entre 1000 e 9999:')
    if numero < str(1000) and numero > str(9999):
        print('Número inválido!')
    for valor in numero:
        print(f'{valor}')

#2
numero = input('Digite um número:')
for valor in numero:
    print(f'{valor}')

"""
#3
numero = input('Digite um número entre 1000 e 9999:')
print(numero[0])
print(numero[1])
print(numero[2])
print(numero[3])
