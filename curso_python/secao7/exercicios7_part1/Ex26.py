numero = [ ]
while True:
    print('#'*100)
    for i in range(1,11):
        num = float(input(f'Informe o {i}° número para calcular o desvio padrão:'))
        while num <= 0:
            print('Número inválido!')
            num = float(input(f'Informe o {i}° número para calcular o desvio padrão:'))
        numero.append(num)
    media = sum(numero) / len(numero)
    desvio_padrao = 0
    desvio_padrao += ( ((media - i) ** 2 ) / len(numero)) ** 1/2
    print(f'O valor do desvio padrão é {desvio_padrao}!')
# não tenho certeza se está certo!!


