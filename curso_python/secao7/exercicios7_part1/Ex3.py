"""
#1
vetor1 = []
vetor_quadrado = []
for i in range(1, 11):
    num = float(input(f'Informe o {i}° número real:'))
    vetor1.append(num)
print(vetor1)
for i in vetor1:
    quadrado = i **2
    vetor_quadrado.append(quadrado)
print(vetor_quadrado)
"""
#2
vetor = [ ]
vetor_quadrado = [ ]
while True:
    print('='*80)
    for i in range(1,5):
        num = float(input(f'Informe o {i}° número:'))
        vetor.append(num)
    for i in vetor:
        quadrado = i ** 2
        vetor_quadrado.append(quadrado)
    print(f'Números digitados {vetor}!\nNúmeros ao quadrado {vetor_quadrado}!')
    vetor.clear()
    vetor_quadrado.clear()


















