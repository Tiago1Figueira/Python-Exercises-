"""
#1
print('='*60, 'CÁLCULO DE OPERAÇÕES MATEMÁTICAS', '='*60)
print('ADIÇÃO -        OPÇÃO 1\nSUBTRAÇÃO -     OPÇÃO 2\nMULTIPLICAÇÃO - OPÇÃO 3\nDIVISÃO -       OPÇÃO 4\nSAÍDA -         OPÇÃO 5')
opc = int(input('Qual é a opção desejada? N°:'))
while opc >=1 and opc <=5:
    if opc == 1:
        num1 = float(input('Informe o primeiro número para o cálculo:'))
        num2 = float(input('Informe o segundo número para o cálculo:'))
        adicao = num1 + num2
        print(f'O valor da adição dos números {num1} e {num2} é {adicao}\n.')
    if opc == 2:
        num1 = float(input('Informe o primeiro número para o cálculo:'))
        num2 = float(input('Informe o segundo número para o cálculo:'))
        subtracao = num1 - num2
        print(f'O valor da subtração dos números {num1} e {num2} é {subtracao}\n.')
    if opc == 3:
        num1 = float(input('Informe o primeiro número para o cálculo:'))
        num2 = float(input('Informe o segundo número para o cálculo:'))
        multiplicacao = num1 * num2
        print(f'O valor da multiplicação dos números {num1} e {num2} é {multiplicacao}\n.')
    if opc == 4:
        num1 = float(input('Informe o primeiro número para o cálculo:'))
        num2 = float(input('Informe o segundo número para o cálculo:'))
        divisao = num1 / num2
        print(f'O valor da divisão dos números {num1} e {num2} é {divisao}\n.')
    if opc == 5:
        print('Você saiu!!')
        break
    print('=' * 60, 'CÁLCULO DE OPERAÇÕES MATEMÁTICAS', '=' * 60)
    print(
        'ADIÇÃO -        OPÇÃO 1\nSUBTRAÇÃO -     OPÇÃO 2\nMULTIPLICAÇÃO - OPÇÃO 3\nDIVISÃO -       OPÇÃO 4\nSAÍDA -         OPÇÃO 5')
    opc = int(input('Qual é a opção desejada? N°:'))

#2
#2
print('=' * 55, 'ESCOLHA UMA DAS OPERAÇÕES', '=' * 65 )
print('adição -        opção 1\nsubtração -     opção 2\nmultiplicação - opção 3\ndivisão -       opção 4\nsaída -         opção 5')
opc = int(input('Informe a opção: N°'))
while True:
    if opc == 1:
        num1 = float(input('Informe o primeiro número a ser usado na operação:'))
        num2 = float(input('Informe o segundo número a ser usado na operação:'))
        adicao = num1 + num2
        print(f'A soma dos números {num1} e {num2} é igual a {adicao}')
    if opc == 2:
        num1 = float(input('Informe o primeiro número a ser usado na operação:'))
        num2 = float(input('Informe o segundo número a ser usado na operação:'))
        subtracao = num1 - num2
        print(f'A subtração dos números {num1} e {num2} é igual a {subtracao}')
    if opc == 3:
        num1 = float(input('Informe o primeiro número a ser usado na operação:'))
        num2 = float(input('Informe o segundo número a ser usado na operação:'))
        multiplicacao = num1 * num2
        print(f'A multiplicação dos números {num1} e {num2} é igual a {multiplicacao}')
    if opc == 4:
        num1 = float(input('Informe o primeiro número a ser usado na operação:'))
        num2 = float(input('Informe o segundo número a ser usado na operação:'))
        divisao = num1 / num2
        print(f'A divisão dos números {num1} e {num2} é igual a {divisao}')
    if opc < 1 or opc > 5:
        print('Atenção: o número deve ser entre 1 e 5!!')
        print('=' * 55, 'ESCOLHA UMA DAS OPERAÇÕES', '=' * 65)
        print(
            'adição -        opção 1\nsubtração -     opção 2\nmultiplicação - opção 3\ndivisão -       opção 4\nsaída -         opção 5')
        opc = int(input('Informe a opção: N°'))
    if opc == 5:
        print('Você saiu!!')
        break
    print('=' * 55, 'ESCOLHA UMA DAS OPERAÇÕES', '=' * 65)
    print(
        'adição -        opção 1\nsubtração -     opção 2\nmultiplicação - opção 3\ndivisão -       opção 4\nsaída -         opção 5')
    opc = int(input('Informe a opção: N°'))
"""
#3




































