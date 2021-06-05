"""
#verificar se o exercicio está correto no futuro.
#1
lista = []
r1 = ' '
r2 = ' '
while True:
    r1 = float(input('Informe a resistência 1:'))
    if r1 <= 0:
        print('Você finalizou')
        break
    r2 = float(input('Informe a resistência 2:'))
    if r2 <= 0:
        print('Você finalizou')
        break
    r = r1 * r2 / r1 + r2
    lista.append(r)
    print(lista)
    lista.clear()
"""
#2
while True:
    r1 = float(input('Informe a resistência 1:'))
    if r1 <=0:
        print('Número inválido! Você saiu!')
        break
    r2 = float(input('Informe a resistência 2:'))
    if r2 <= 0:
        print('Número inválido! Você saiu!')
        break
    r = r1 * r2 / r1 + r2
    print(r)




















