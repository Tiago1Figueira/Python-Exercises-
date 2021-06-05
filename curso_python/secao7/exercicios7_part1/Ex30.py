"""
#1
cont = 1
vetor1 = []
vetor2 = []

while cont <= 5:
    valores_vetor1 = int(input(f'Valor {cont}: '))
    valores_vetor2 = int(input(f'Valor {cont}: '))
    vetor1.append(valores_vetor1)
    vetor2.append(valores_vetor2)
    cont = cont + 1

print(vetor1)
print(vetor2)
print(set(vetor1).intersection(vetor2))

#2
v1 = []
v2 = []
v3 = []
print('=' * 50, 'VETOR 1', '=' * 50)
for i in range(1,4):#11
    num1 = int(input(f'Informe o {i}° número do vetor1:'))
    v1.append(num1)
print('=' * 50, 'VETOR 2', '=' * 50)
for i in range(1, 4):  # 11
    num2 = int(input(f'Informe o {i}° número do vetor2:'))
    v2.append(num2)
print('=' * 50, 'VETOR 3', '=' * 50)
if v1 != v2:
    v3 = v1 + v2
print(v3)
#nao consegui resolver o problema com o vetor 3.
"""
#3
vetor1 = [ ]
vetor2 = [ ]
vetor3 = [ ]
while True:
    print('#'*100)
    print(f'Informe 10 números para o vetor1:')
    for i in range(4):
        num1 = float(input('N°'))
        vetor1.append(num1)
    print(f'Informe 10 números para o vetor2:')
    for i in range(4):
        num2 = float(input('N°'))
        vetor2.append(num2)
    print(vetor1)
    print(vetor2)
    print(set(vetor1).intersection(vetor2))
    vetor1.clear()
    vetor2.clear()
    vetor3.clear()

















