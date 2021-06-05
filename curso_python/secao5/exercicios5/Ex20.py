"""
#1
def calculo_triangulo(a,b,c):

    if a == 0 or b == 0 or c == 0:
        return 'Todos os lados devem ser maiores que 0!'
    if a >= b + c:
        return f'A figura plana não é um triângulo!'
    if b >= a + c:
        return f'A figura plana não é um triângulo!'
    if c >= a + b:
        return f'A figura plana não é um triângulo!'
    if a != b and a != c and b != c:
        return f'Triângulo Escaleno!'
    if a == b and a == c and b == c:
        return f'Triângulo Equilátero!'
    return f'Triângulo Isósceles!'
while True:
    a = float(input('Informe o valor lado 1:'))
    b = float(input('Informe o valor lado 2:'))
    c = float(input('Informe o valor lado 3:'))
    print(calculo_triangulo(a,b,c))

"""
#2
while True:
    print('=' * 50, 'DESCUBRA O TIPO DE TRIÂNGULO:', '=' * 50)
    a = int(input('Informe lado A do triângulo:'))
    b = int(input('Informe lado B do triângulo:'))
    c = int(input('Informe lado C do triângulo:'))
    if a == 0 or b == 0 or c == 0:
        print('Todos os lados devem ser maiores que 0!')
    elif a >= b + c:
        print('A figura plana não é um triângulo!')
    elif b >= a + c:
        print('A figura plana não é um triângulo!')
    elif c >= b + a:
        print('A figura plana não é um triângulo!')
    elif a != b and a != c and c != b:
        print('Triângulo Escaleno!')
    elif a == b and a == c and c == b:
        print('Triângulo Equilátero!')
    else:
        print('Triângulo Isósceles!')
