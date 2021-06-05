"""
#1
numero_lido = int(input('Digite um numero de 100 a 999: '))
if 100 <= numero_lido <= 999:
    numero_gerado = str(numero_lido)[::-1]
    print(numero_gerado)
else:
    print("Numero invalido")

#2 (professor)
numero_lido = input('Digite um numero de 100 a 999: ')

if int(numero_lido) >= 100 and int(numero_lido) <= 999:
    print(numero_lido[::-1])
else:
    print('Numero invalido')

#3
numeroInverso = input("Digite um número entre 100 e 999: ")
print(f"Número invertido de {numeroInverso} é: {numeroInverso[::-1]}")

#4
while True:
    print('=' * 150)
    num = input('Informe um número inteiro e positivo entre 100 e 999:')
    if num >= str(100) and num <= str(999):
        print(f'O número inverso é {num[::-1]}!')
    else:
        print('Número inválido!')
"""
#5
print('='*150)
num = input('Informe um número entre 100 e 999:')
print(f'numero  {num[::-1]}')





