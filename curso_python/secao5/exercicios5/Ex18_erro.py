#se eu coloco mais de um número inválido sucessivamente(menor que 1 ou maior q 5) o programa deixa de falar
#'número inválido' vez sim e vez não. Pq?
print('=' * 50, 'CÁLCULO DE OPERAÇÕES MATEMÁTICAS', '=' * 50)
print('Opções:\n1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\n5-Sair\n')
opt = int(input('Selecione um número: n°'))

while True:
    if opt < 1 or opt > 5:
        print('Número inválido!')
        print('Opções:\n1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\n5-Sair\n')
        opt = int(input('Selecione um número: n°'))

    if opt == 1:
        num1 = int(input('Informe o 1° valor da soma:'))
        num2 = int(input('Informe o 2° valor da soma:'))
        soma = num1 + num2
        print(f'A soma dos números {num1} e {num2} é igual a {soma}')

    if opt == 2:
        num1 = int(input('Informe o 1° valor da subtração:'))
        num2 = int(input('Informe o 2° valor da subtração:'))
        subtracao = num1 - num2
        print(f'A subtração dos números {num1} e {num2} é igual a {subtracao}')

    if opt == 3:
        num1 = int(input('Informe o 1° valor da multiplicação:'))
        num2 = int(input('Informe o 2° valor da multiplicação:'))
        multiplicacao = num1 * num2
        print(f'A multiplicação dos números {num1} e {num2} é igual a {multiplicacao}')

    if opt == 4:
        num1 = int(input('Informe o 1° valor da divisão:'))
        num2 = int(input('Informe o 2° valor da divisão:'))
        subtracao = num1 / num2
        print(f'A divisão dos números {num1} e {num2} é igual a {subtracao}')

    if opt == 5:
        print('Você saiu!')
        break

    print('=' * 50, 'CÁLCULO DE OPERAÇÕES MATEMÁTICAS', '=' * 50)
    print('Opções:\n1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\n5-Sair\n')
    opt = int(input('Selecione um número: n°'))


