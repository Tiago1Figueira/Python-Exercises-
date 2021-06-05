"""
#1
vetorx = [ ]
vetory = [ ]
soma = [ ]
multiplicacao = [ ]
subtracao = [ ]
interseccao = [ ]
uniao = [ ]
while True:
    print('#' * 100)
    print('Informe 5 números para o vetorX')
    for i in range(5):
        num = float(input('N°:'))
        while num <=0 or num != int(num):
            print('Número inválido!')
            num = float(input('N°:'))
        vetorx.append(num)
    print('Informe 5 números para o vetorY')
    for i in range(5):
        num = float(input(f'N°:'))
        while num <=0 or num != int(num):
            print('Número inválido!')
            num = float(input('N°:'))
        vetory.append(num)
    for i in range(5):
        #soma
        somaxy = vetorx[i] + vetory[i]
        soma.append(somaxy)
        #multiplicacao
        multiplicacaoxy = vetorx[i] * vetory[i]
        multiplicacao.append(multiplicacaoxy)
        #diferenca
        subtracaoxy = vetorx[i] - vetory[i]
        subtracao.append(subtracaoxy)
        #interseccao
        (set(vetorx).intersection(vetory))
        #uniao
        (set(vetorx).union(vetory))

    print('Resultados:')
    print(f'Vetorx {vetorx}\nVetory {vetory}')
    print(f'1-Soma das posições dos vetores X e Y: {soma}\n'
          f'2-Multiplicação das posições dos vetores:{multiplicacao}\n'
          f'3-Subtração entre as posições dos vetores X e Y: {subtracao}\n'
          f'4-Intersecção entre os vetores X e Y:{(set(vetorx).intersection(vetory))}\n'
          f'5-União das posições dos vetores X e Y:{(set(vetorx).union(vetory))}')
    vetorx.clear()
    vetory.clear()
    soma.clear()
    multiplicacao.clear()
    subtracao.clear()
    interseccao.clear()
    uniao.clear()

#2
vetorx = [ ]
vetory = [ ]
soma = [ ]
multiplicacao = [ ]
subtracao = [ ]
while True:
    print('#'*100)
    print('Informe 5 números para o vetor1:')
    for i in range(5):
        num = float(input('N°'))
        while num <= 0 or num != int(num):
            print('Número inválido!')
            num = float(input('N°'))
        vetorx.append(num)
    print('Informe 5 números para o vetor2:')
    for i in range(5):
        num = float(input('N°'))
        while num <= 0 or num != int(num):
            print('Número inválido!')
            num = float(input('N°'))
        vetory.append(num)
    for i in range(5):
        somaxy = vetorx[i] + vetory[i]
        soma.append(somaxy)
        subtracaoxy = vetorx[i] - vetory[i]
        subtracao.append(subtracaoxy)
        multiplicacaoxy = vetorx[i] * vetory[i]
        multiplicacao.append(multiplicacaoxy)
    print(f'Vetor X {vetorx}')
    print(f'Vetor Y {vetory}')
    print(f'Soma dos elementos de X e Y {soma}')
    print(f'Subtração dos elementos de X e Y {subtracao}')
    print(f'Multiplicação dos elementos de X e Y {multiplicacao}')
    print(f'Diferença entre vetores(elementos de X que não existam em Y){set(vetorx).difference(vetory)}')
    print(f'Intersecção entre vetores {set(vetorx).intersection(vetory)}')
    print(f'União entre vetores {set(vetorx).union(vetory)}')
    vetorx.clear()
    vetory.clear()
    soma.clear()
    subtracao.clear()
    multiplicacao.clear()


#3
vetorx = [ ]
vetory = [ ]
soma = [ ]
multiplicacao = [ ]
diferenca = [ ]
subtracao = [ ]
while True:
    print('%'*100)
    print('Informe 5 números inteiros para o vetor X:')
    for i in range(5):
        num = float(input('N°:'))
        while num <=0 or num != int(num):
            print('Número Inválido!')
            num = float(input('N°:'))
        vetorx.append(num)
    print('Informe 5 números inteiros para o vetor Y:')
    for i in range(5):
        num = float(input('N°:'))
        while num <= 0 or num != int(num):
            print('Número inválido!')
            num = float(input('N°:'))
        vetory.append(num)
    for i in range(5):
        somaxy = vetorx[i] + vetory[i]
        soma.append(somaxy)
        multiplicacaoxy = vetorx[i] * vetory[i]
        multiplicacao.append(multiplicacaoxy)
        subtracaoxy = vetorx[i] - vetory[i]
        subtracao.append(subtracaoxy)
        diferenca = (set(vetorx).difference(vetory))

    print(f'Vetor X: {vetorx}')
    print(f'Vetor Y: {vetory}')
    print(f'Soma dos elementos vetores X e Y: {soma}')
    print(f'Multiplicação dos elementos vetores X e Y: {multiplicacao}')
    print(f'Subtração dos elementos vetores X e Y: {subtracao}')
    print(f'Diferença dos elementos vetores X e Y: {diferenca}')
    print(f'União dos elementos vetores X e Y: {(set(vetorx).union(vetory))}')
    print(f'Intersecção elementos vetores X e Y: {(set(vetorx).intersection(vetory))}')
    vetorx.clear()
    vetory.clear()
    soma.clear()
    multiplicacao.clear()
    subtracao.clear()

"""
#4
vetorx = [ ]
vetory = [ ]
soma = [ ]
multiplicacao = [ ]
subtracao = [ ]
while True:
    print('#'*100)
    print('Informe 5 números inteiros para o vetor X:')
    for i in range(5):
        num = float(input(f'N°:'))
        while num <= 0 or num != int(num):
            print('Número inválido!')
            num = float(input(f'N°:'))
        vetorx.append(num)
    print('Informe 5 números inteiros para o vetor Y:')
    for i in range(5):
        num = float(input(f'N°:'))
        while num <= 0 or num != int(num):
            print('Número inválido!')
            num = float(input(f'N°:'))
        vetory.append(num)
    for i in range(5):
        somaxy = vetorx[i] + vetory[i]
        soma.append(somaxy)
        multiplicacaoxy = vetorx[i] * vetory[i]
        multiplicacao.append(multiplicacaoxy)
        subtracaoxy = vetorx[i] - vetory[i]
        subtracao.append(subtracaoxy)
    print(f'Vetor X:{vetorx}')
    print(f'Vetor Y:{vetory}')
    print(f'Soma das posições de X e Y:{soma}')
    print(f'Multiplicação das posições de X e Y:{multiplicacao}')
    print(f'Subtração das posições de X e Y:{subtracao}')
    print(f'Diferença entre posições de X e Y:{(set(vetorx).difference(vetory))}')
    print(f'Intersecção entre os vetores X e Y:{(set(vetorx).intersection(vetory))}')
    print(f'União entre os vetores X e Y:{(set(vetorx).union(vetory))}')
    vetorx.clear()
    vetory.clear()
    soma.clear()
    multiplicacao.clear()
    subtracao.clear()





































