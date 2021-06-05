"""
#1
lista = []
for i in range(1,11):
    num = float(input(f'Informe o {i}° número:'))
    lista.append(num)
print(f'O maior valor da lista é {max(lista)} e o menor valor é {min(lista)}! ')
"""
#2
vetor = [ ]
while True:
    print('='*80)
    for i in range(1,11):
        num = float(input(f'Informe o {i}° número:'))
        while num != int(num):
            print('Número inválido!')
            num = float(input(f'Informe o {i}° número:'))
        vetor.append(num)
    print(f'Maior número {max(vetor)}\nMenor número {min(vetor)}!')


