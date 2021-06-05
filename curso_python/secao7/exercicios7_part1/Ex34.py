"""
#1
vetor = []
while len(vetor) < 10:
    valor = int(input(f"Digite um número {len(vetor)+1}/10: "))
    if valor in vetor:
        print(f'O valor {valor} já existe no vetor')
    else:
        vetor.append(valor)
print(vetor)

#2
vetor = []
for i in range(10):
    valor = int(input(f"Digite um número {i+1}/10: "))
    while valor in vetor:
        print(f'O valor {valor} já existe no vetor')
        valor = int(input(f"Digite um número {i + 1}/10: "))
    else:
        vetor.append(valor)
print(vetor)

#3
vet = []
for i in range(1,7): #11
    num = int(input(f'Informe o {i}° número:'))
    while num in vet:
        print((f'Atenção: o vetor já possui número {num}!'))
        num = int(input(f'Informe o {i}° número:'))
    else:
        vet.append(num)
print(vet)

#4
vet = [ ]
for i in range(1,5):#11
    num = int(input(f'Informe o {i} número:'))
    while num in vet:
        print(f'O número {num} já foi digitado!')
        num = int(input(f'Informe o {i}° número:'))
    else:
        vet.append(num)
print(vet)

#5
vetor = [ ]
while True:
    print('#'*100)
    for i in range(1,11):
        num = float(input(f'Informe o {i}° número:'))
        while num in vetor:
            print(f'O número {num} já existe no vetor!')
            num = float(input(f'Informe o {i}° número:'))
        else:
            vetor.append(i)
    print(vetor)

"""
#6
vetor = [ ]
while True:
    print('#'*100)
    for i in range(1,11):
        num = float(input(f'Informe o {i}° número:'))
        while num in vetor:
            print(f'O número {num} já existe no vetor:')
            num = float(input(f'Informe o {i}° número:'))
        else:
            vetor.append(num)
    print(vetor)















