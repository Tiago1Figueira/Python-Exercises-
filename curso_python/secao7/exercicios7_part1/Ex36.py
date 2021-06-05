"""
#1
vetor = []
for i in range(1,5):#11
    num = float(input(f'Informe o {i}° número:'))
    vetor.append(num)
    vetor.sort()
print(vetor)

"""
#2
vetor = [ ]
while True:
    print('#' * 100)
    for i in range(1,10):
        num = float(input(f'Informe o {i}° número real:'))
        while num != float(num):
            print('Número inválido!')
            num = float(input(f'Informe o {i}° número real:'))
        vetor.append(num)
        vetor.sort()
    print(f'Os números reais digitados e ordenados são {vetor}')
    vetor.clear()
# como faço pra que o programa somente aceite número não inteiros?




