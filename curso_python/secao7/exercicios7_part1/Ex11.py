"""
#1
lista = []
negativos = []
positivos = []
for i in range(1,11):
    num = int(input(f'Informe o {i}° número:'))
    lista.append(num)
    if num < 0:
        negativos.append(num)
    if num > 0:
        positivos.append(num)
print(sum(positivos))
print(negativos)
"""
#2
negativos = [ ]
positivos = [ ]
while True:
    print('='*80)
    for i in range(1,11):
        num = float(input(f'Informe o {i}° número:'))
        if num < 0:
            negativos.append(num)
        else:
            positivos.append(num)
    print(f'Quantidade números negativos {negativos}\nSoma números positivos {sum(positivos)}')
    negativos.clear()
    positivos.clear()
