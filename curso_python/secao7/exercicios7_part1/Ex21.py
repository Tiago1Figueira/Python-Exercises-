"""
#1
a, b, c = [], [], []
for i in range(1,5):
    aux_a = int(input("A Valor: "))
    a.append(aux_a)
for i in range(1,5):
    aux_b = int(input("B Valor: "))
    b.append(aux_b)
    c.append(aux_a - aux_b)

print(f'A: {a}')
print(f'B: {b}')
print(f'C: {c}')

#2
vetor_a = []
vetor_b = []
vetor_c = []
for i in range(1,5):#11
    a = int(input(f'Informe o {i}° número do vetorA:'))
    vetor_a.append(a)
for i in range(1,5):#11
    b = int(input(f'Informe o {i}° número do vetorB:'))
    vetor_b.append(b)
for i in vetor_a:
    for i in vetor_b:
        c = (vetor_a[i] - vetor_b[i])
        vetor_c.append(c)
        for i in vetor_c:
            print(i)


#print(vetor_a,vetor_b,vetor_c)
#não consegui fazer o vetor c (c = a - b)
"""
#3
vetor_a = []
vetor_b = []
vetor_c = []
while True:
    print('='*80)
    print(f'Informe 10 números inteiros para o vetorA:')
    for i in range(10):
        a = float(input('N°'))
        while a != int(a) or a < 0:
            print('Número inválido!')
            a = float(input('N°'))
        vetor_a.append(a) # Teste! Aqui somente números inteiros e positivos!
    print(f'Informe 10 números para o vetorB:')
    for i in range(10):
        b = float(input('N°'))
        vetor_b.append(b) # Aqui qqer número!
    for i in range(10):
        c = (vetor_a[i] - vetor_b[i])# vetorA < vetorB dá número negativo!
        vetor_c.append(c)
    print(f'O vetor C será {vetor_c}')
    vetor_a.clear()
    vetor_b.clear()
    vetor_c.clear()
