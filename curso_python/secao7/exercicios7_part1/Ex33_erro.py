"""
#1
vet = []
for i in range(1,5):#15
    num = int(input(f'Informe o {i}° número:'))
    if num == 0:
        vet.pop( )
        vet.append(num)
print(vet)
# não encontrei uma forma de se excluir o '0' do vetor.
"""
#2
vetor = [ ]
while True:
    print('#'*100)
    for i in range(1,16):
        num = float(input(f'Informe o {i}° elemento do vetor:'))
        vetor.append(num)
    for i in vetor:
        if i == 0:
            vetor.pop(vetor.index(i))
    print(f'Vetor sem zeros é {vetor}')
    vetor.clear()
#o programa recebe zeros, mas não exclui a todos do vetor.

