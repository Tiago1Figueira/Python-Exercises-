def maior_numero(a,b):
    if a > b:
        return f'O número {a} é maior que {b}!'
    if b > a:
        return f'O número {b} é maior que {a}!'
    return f'Os dois números são iguais!'

a = float(input('Informe o 1º número:'))
b = float(input('Informe o 2º número:'))

print(maior_numero(a,b))
