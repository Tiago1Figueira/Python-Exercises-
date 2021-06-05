"""
#1
vet = [ ]
for i in range(5):
    num = int(input(f'Digite o número {i+1}/5:'))
    vet.append(num)
print(vet)
for valor in vet:
    if valor < 0:
        vet.insert(vet.index(valor), 0)
        vet.pop(vet.index(valor))
print(vet)

#2
vet = []
for i in range(5):
    num = int(input(f'Informe o {i+1}/5 número:'))
    vet.append(num)
print(vet)
for i in vet:
    if i < 0:
        vet.insert(vet.index(i), 0)
        vet.pop(vet.index(i))
print(vet)
# houve cópia das linhas 18 a 21. Estudar e praticar para adquirir conhecimento.

#3
vetor = [ ]
while True:
    print('='*80)
    for i in range(1,11):
        num = float(input(f'Informe o {i}° número:'))
        vetor.append(num)
    for i in vetor:
        if i < 0:
            vetor.insert(vetor.index(i), 0)
            vetor.pop(vetor.index(i))
    print(vetor)
    vetor.clear()

"""
#4
vetor = [ ]
print('#'*100)
for i in range(1,11):
    num = float(input(f'Informe o {i}° número:'))
    vetor.append(num)
    for i in vetor:
        if i < 0:
            vetor.insert(vetor.index(i), 0)
            vetor.pop(vetor.index(i))
print(f'Os números digitados foram {vetor}. ')
vetor.clear()



























































