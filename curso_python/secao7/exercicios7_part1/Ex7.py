"""
#1
vetor = []
for i in range(1,11):
    num = float(input(f'Informe o {i}° número:'))
    vetor.append(num)
print(vetor)
print(max(vetor))
print(vetor.index(max(vetor)))
"""
#2
vetor = [ ]
while True:
    print('='*80)
    for i in range(1,11):
        num = float(input(f'Informe o {i}° número:'))
        vetor.append(num)
    print(f'Números digitados: {vetor}\nMaior elemento: {max(vetor)}\nPosição Maior elemento: {vetor.index(max(vetor))}')
    vetor.clear()

