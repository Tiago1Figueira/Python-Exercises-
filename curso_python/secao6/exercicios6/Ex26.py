"""
#1
divisivel_11 = 0
divisivel_13 = 0
divisivel_17 = 0
num = int(input('Informe um número:'))
for i in range(num, num + 17):
    if i > num:
        if i % 11 == 0:
            divisivel_11 = i
        if i % 13 == 0:
            divisivel_13 = i
        if i % 17 == 0:
            divisivel_17 = i
print(f'Após o número {num} os números divisíveis por 11, 13 e 17 são respectivamente '
      f'{divisivel_11}, {divisivel_13} e {divisivel_17}.')
# erro: quando se coloca o número 34 o valor de primeiro múltiplo de 17 após esse número aparece como 0.
# o que devo fazer para acertar o código? 

#2
divisivel_11 = 0
divisivel_13 = 0
divisivel_17 = 0
num = int(input('Informe um número:'))
for i in range(num, num + 20):
    if i > num:
        if i % 11 == 0:
            divisivel_11 = i
        if i % 13 == 0:
            divisivel_13 = i
        if i % 17 == 0:
            divisivel_17 = i
print(f'O divisores de 11, 13 e 17 após o número {num} são {divisivel_11}, {divisivel_13}, {divisivel_17}!')

"""
#3
divisor_11 = ' '
divisor_13 = ' '
divisor_17 = ' '
while True:
    num = float(input('Informe um número:'))
    while num < 0 or num != int(num):
        print('Número inválido!')
        num = float(input('Informe um número:'))
    for i in range(int(num), int(num) + 18):
        if i > num:
            if i % 11 == 0:
                divisor_11 = i
            elif i % 13 == 0:
                divisor_13 = i
            elif i % 17 == 0:
                divisor_17 = i
    print(f'Os primeiros divisores por 11, 13 e 17 após o número {num} são {divisor_11}, {divisor_13} e {divisor_17}!')
















