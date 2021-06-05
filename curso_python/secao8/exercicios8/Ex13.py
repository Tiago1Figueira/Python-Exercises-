#1
def operacoes_matematicas(operacao,num1,num2):
    if operacao == '+':
        soma = num1 + num2
        return f'{soma}'
    if operacao == '-':
        subtracao = num1 - num2
        return f'{subtracao}'
    if operacao == '*':
        multiplicacao = num1 * num2
        return f'{multiplicacao}'
    if operacao == '/':
        divisao = num1 / num2
        return f'{divisao}'
    return f'Símbolo inválido! Opções: "+", "-","*","/" !'

while True:
    operacao = input(f'Operações: +, -, *, /\nEscolheu:')
    a = int(input('1° número:'))
    b = int(input('2° número:'))
    print(operacoes_matematicas(operacao,a,b))

