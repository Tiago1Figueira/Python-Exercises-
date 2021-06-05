#1
vetor = [ ]
vetor1 = [ ]
crescente = [ ]
decrescente = [ ]
while True:
    print('#' * 100)
    for i in range(1,11):
        num = float(input(f'Informe o {i}° número real:'))
        vetor.append(num)
        if i <=6:
            a = vetor[i]
            crescente.append(a)
            crescente.sort()
        else:
            a = vetor[i]
            decrescente.append(a)
            decrescente.sort()
            decrescente.reverse()
        vetor = crescente + decrescente
    print(vetor)
    vetor.clear()
    crescente.clear()
    decrescente.clear()
#está dando problema no print! refazê-lo!!