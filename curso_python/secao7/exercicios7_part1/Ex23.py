"""
#1
vetor1 = []
vetor2 = []
vetor3 = []
soma = 0
print('=' * 60, 'VETOR1', '=' * 60)
for x in range(1, 6):
    num1 = float(input(f'Informe o {x}° número:'))
    vetor1.append(num1)
print('=' * 60, 'VETOR2', '=' * 60)
for y in range(1, 6):
    num2 = float(input(f'Informe o {y}° número:'))
    vetor2.append(num2)
for i in range(1,6):
    soma += vetor1 * vetor2
print('=' * 60, 'RESULTADOS', '=' * 60)
print(f'vetor1{vetor1}')
print(f'vetor2{vetor2}')
print(f'produto escalar[{soma}]')
# não consegui achar o cálculo do vetor 3 ou produto escalar!!

#2
vetor1 = [ ]
vetor2 = [ ]
pe = 0
print('Informe 5 números para o 1° vetor:')
for i in range(5):
    num1 = float(input('N°' ))
    vetor1.append(num1)
print('Informe 5 números para o 2° vetor:')
for i in range(5):
    num2 = float(input(f'N°'))
    vetor2.append(num2)
for i in range(5):
    pe = pe + vetor1[i] * vetor2[i]
print(f'Vetor1 {vetor1}\nVetor2 {vetor2}\nPe {pe}')

"""
#3
vetor1 = [ ]
vetor2 = [ ]
pe = 0
while True:
    print('#'*100)
    print('Informe 5 números para o 1° vetor:')
    for i in range(5):
        num = int(input('N°'))
        vetor1.append(num)
    print('Informe 5 números para o 2° vetor:')
    for i in range(5):
        num = int(input('N°'))
        vetor2.append(num)
    for i in range(5):
        pe = pe + vetor1[i] * vetor2[i]
    print(f'Vetor 1 {vetor1}\nVetor 2 {vetor2}\nProduto Escalar {pe}')
    vetor1.clear()
    vetor2.clear()


















