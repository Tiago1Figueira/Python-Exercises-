"""
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
print(set(vetor1).union(vetor2))

#2
v1 = []
v2 = []
v3 = []
for i in range(1,4):#11
    num1 = int(input(f'Informe o {i}° número do vetor1:'))
    v1.append(num1)

for i in range(1,4):#11
    num2 = int(input(f'Informe o {i}° número do vetor2:'))
    v2.append(num2)
v3 = v1 + v2 - (num1 == num2)
# error = não consegui arrumar o v3!
"""
#3
vetor1 = [ ]
vetor2 = [ ]
vetor3 = [ ]
while True:
    print('#'*100)
    for i in range(1,4):
        num1 = float(input(f'Informe o {i}° elemento do vetor1:'))
        vetor1.append(num1)
    for i in range(1,4):
        num2 = float(input(f'Informe o {i}° elemento do vetor2:'))
        vetor2.append(num2)
    vetor3 = (set(vetor1).union(vetor2))

    print(f'Vetor1 {vetor1}\nVetor2 {vetor2}\nVetor3 {vetor3}')
    vetor1.clear()
    vetor2.clear()
    vetor3.clear()
# interessante seria saber como organizar os elementos em ordem crescente, descrecente,
# alfabética no set, pois o sort aqui nao funciona!
















