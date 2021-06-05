"""
#1
vetor1 = []
vetor2 = []
vetor3 = []
print('=' * 55, 'VETOR1', '=' * 55)
for i in range(1,11):
    num1 = int(input(f'Informe o {i}° número do vetor1:'))
    vetor1.append(num1)
    if num1 % 2 == 0:
        vetor3.append(num1)
        vetor3.sort( )

print('=' * 55, 'VETOR2', '=' * 55)
for i in range(1,11):
    num2 = int(input(f'Informe o {i}° número do vetor2:'))
    vetor2.append(num2)
    if num2 % 2 != 0:
        vetor3.append(num2)
        vetor3.sort( )

print('=' * 55, 'RESULTADOS', '=' * 55)
print(f'vetor1 {vetor1}')
print(f'vetor2 {vetor2}')
print(f'vetor3 {vetor3}')
"""
#2
vetor1 = [ ]
vetor2 = [ ]
vetor3 = [ ]
while True:
    print('='*80)
    for i in range(1,5):
        num1 = float(input(f'Informe o {i}° número do Vetor1:'))
        vetor1.append(num1)
    for i in range(1,5):
        num2 = float(input(f'Informe o {i}° número do Vetor2:'))
        vetor2.append(num2)
    for i in vetor1:
        if i % 2 == 0:
            vetor3.append(i)
    for i in vetor2:
        if i % 2 != 0:
            vetor3.append(i)
            vetor3.sort()

    print(f'Vetor1 {vetor1}\nVetor2 {vetor2}\nVetor3 {vetor3}!')
    vetor1.clear()
    vetor3.clear()
    vetor2.clear()
# não sei limitar o número de posições em até 5 vindas de cada vetor(vetor 1 e vetor2) Isso é só curiosidade, não é enunciado.
























