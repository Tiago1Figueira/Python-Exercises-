"""
#1
v = []
v1 = [ ]
v2 = [  ]
for i in range(1, 11):
    num = int(input(f'Informe o {i}° número:'))
    v.append(num)
    if i % 2 != 0: #ímpar
        v1.append(num)
    if i % 2 == 0: #par
        v2.append(num)
print(f'Vetor1 {v1} e vetor2 {v2}.')
"""
#2
v = [ ]
v1 = [ ]
v2 = [ ]
while True:
    print('#'*100)
    for i in range(1,11):
        num = float(input(f'Informe o {i}° número:'))
        while num <= 0 or num != int(num):
            print('Número inválido!')
            num = float(input(f'Informe o {i}° número:'))
        v.append(num)
    for i in v:
        if i % 2 != 0:
            v1.append(i)
        else:
            v2.append(i)

    print('RESULTADO FINAL:')
    print(f'Números ímpares {v1}\nNúmeros pares {v2}')
    v.clear()
    v1.clear()
    v2.clear()

