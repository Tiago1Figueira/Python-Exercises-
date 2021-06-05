"""
#1

vetor_a = []
vetor_b = []
a = int(input('Informe um número menor que 10000: '))
b = int(input('Informe outro número menor que 10000: '))
if a < 10000 and b < 10000:
    a = str(a)
    b = str(b)
    for valor_a in a:
	vetor_a.append(int(valor_a))
    vetor_a.sort()
    for valor_b in b:
	vetor_b.append(int(valor_b))
    print(f'A soma de {vetor_a} + {vetor_b} é {sum(vetor_a) + sum(vetor_b)}')
else:
    print('Valores informados incorretamente. ')
    
"""
#2
vetor1 = [ ]
vetor2 = [ ]
while True:
    print('%'*100)
    a = int(input(f'Informe um número menor que 10.000:'))
    while a > 10_000:
        print(f'Número inválido!')
        a = int(input(f'Informe um número menor que 10.000:'))
    b = int(input(f'Informe outro número menor que 10.000:'))
    while b > 10_000:
        print(f'Número inválido!')
        b = int(input(f'Informe outro número menor que 10.000:'))
    a = str(a)
    b = str(b)
    for i in a:
        vetor1.append(int(i))
        vetor1.sort()
    for i in b:
        vetor2.append(int(i))
        vetor2.sort()
    print('Resultado:')
    print(f'A soma de {vetor1} + {vetor2} é igual a {sum(vetor1) + sum(vetor2)}!')
    vetor1.clear()
    vetor2.clear()
# não consigo aplicar a restrição aos números não inteiros durante o recebimento dos números digitados.
