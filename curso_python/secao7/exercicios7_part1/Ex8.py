"""
#1
lista = []
for i in range(1,7):
    num = int(input(f'Informe o {i}° número:'))
    lista.append(num)
# 2 formas de se fazer a reversão dos dados!
print(lista)
print(lista[::-1])

lista.reverse()
print(lista)
"""
#2
#ex8
vetor = [ ]
for i in range(1,7):
    num = float(input(f'Informe o {i}° número:'))
    while num != int(num):
        print('Número inválido!')
        num = float(input(f'Informe o {i}° número:'))
    vetor.append(num)
print(vetor[::-1]) #0 aqui o print é usado na reversão da posição dos números.

vetor.reverse()  #1 aqui o print não é usado, mas somente depois disso na linha abaixo!
print(vetor)
vetor.clear()


