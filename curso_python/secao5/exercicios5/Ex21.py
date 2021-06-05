print('=' * 50, 'ESCOLHA A OPERAÇÃO MATEMÁTICA', '=' *50)
print('Opções:\n1- Soma de 2 números\n2- Diferença entre 2 números\n3- Produto entre dois números\n4- Divisão entre 2 números\n5- Sair')
opc = int(input('Opção n°'))
while opc < 1 or opc >5:
    print('Atenção: opção inválida!')
    print('Opções:\n1- Soma de 2 números\n2- Diferença entre 2 números\n3- Produto entre dois números\n4- Divisão entre 2 números\n5- Sair')
    opc = int(input('Opção n°'))
while True:
    if opc == 1:
        num1 = int(input('Informe o 1° número:'))
        num2 = int(input('Informe o 2° número:'))
        soma = num1 + num2
        print(f'A soma dos números {num1} e {num2} é igual a {soma}! ')

    if opc == 2:
        num1 = int(input('Informe o 1° número:'))
        num2 = int(input('Informe o 2° número:'))
        while num2 > num1:
            print('Atenção: 1° número deve ser maior que o segundo!!' )
            num1 = int(input('Informe o 1° número:'))
            num2 = int(input('Informe o 2° número:'))
        subtracao= num1 - num2
        print(f'A subtração dos números {num1} e {num2} é igual a {subtracao}! ')

    if opc == 3:
        num1 = int(input('Informe o 1° número:'))
        num2 = int(input('Informe o 2° número:'))
        multiplicacao = num1 * num2
        print(f'A multiplicação dos números {num1} e {num2} é igual a {multiplicacao}! ')

    if opc == 4:
        num1 = int(input('Informe o numerador da divisão:'))
        num2 = int(input('Informe o denominador da divisão:'))
        while num2 == 0:
            print('Atenção: o denominador não pode ser 0 !!' )
            num1 = int(input('Informe o numerador da divisão:'))
            num2 = int(input('Informe o denominador da divisão:'))
        divisao = num1 / num2
        print(f'A divisão dos números {num1} e {num2} é igual a {divisao}! ')
    if opc == 5:
        print('Você saiu!')
        break

    print('=' * 50, 'ESCOLHA A OPERAÇÃO MATEMÁTICA', '=' *50)
    print('Opções:\n1- Soma de 2 números\n2- Diferença entre 2 números\n3- Produto entre dois números\n4- Divisão entre 2 números\n5- Sair')
    opc = int(input('Opção n°'))
    while opc < 1 or opc >5:
        print('Atenção: opção inválida!')
        print('Opções:\n1- Soma de 2 números\n2- Diferença entre 2 números\n3- Produto entre dois números\n4- Divisão entre 2 números\n5- Sair')
        opc = int(input('Opção n°'))
