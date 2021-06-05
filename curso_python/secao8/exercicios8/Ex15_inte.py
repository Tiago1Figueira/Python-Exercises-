"""
#1
def tipo_de_triangulo(lado1,lado2,lado3):
    lados = lado1, lado2, lado3
    for lado in lados:
        if lado <=0:
            return f'Todos os lados devem ser maiores que 0!'
        if lado1 >= lado2 + lado3:
            return 'As medidas dos lados não correspondem a um triângulo!'
        if lado2 >= lado1 + lado3:
            return 'As medidas dos lados não correspondem a um triângulo!'
        if lado3 >= lado1 + lado2:
            return 'As medidas dos lados não correspondem a um triângulo!'
        if lado1 == lado2 == lado3:
            return 'Triângulo Equilátero!'
        if lado1 != lado2 and lado1 != lado3 and lado3 != lado2:
            return 'Triângulo Escaleno!'
        return 'Triângulo Isósceles!'

while True:
    a= float(input('Informe o lado 1:'))
    b= float(input('Informe o lado 2:'))
    c= float(input('Informe o lado 3:'))
    print(tipo_de_triangulo(a,b,c))

#2
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

#3
def tipo_de_triangulo(a,b,c):
    if a == 0 or b == 0 or c == 0:
        return 'Todos os lados devem ser maiores que 0!'
    elif a >= b + c:
        return 'A figura plana não é um triângulo!'
    elif b >= a + c:
        return 'A figura plana não é um triângulo!'
    elif c >= a + b:
        return 'A figura plana não é um triângulo!'
    elif a == b and a == c and b == c:
        return 'Triângulo Equilátero!'
    elif a != b and a != c and b != c:
        return 'Triângulo Escaleno!'
    return 'Triângulo Isósceles!'

while True:
    a = float(input('Informe o lado A:'))
    b = float(input('Informe o lado B:'))
    c = float(input('Informe o lado C:'))

    print(tipo_de_triangulo(a,b,c))
"""
#4
def formacao_triangulos(a,b,c):
    if a == 0 or b == 0 or c == 0:
        return 'Atenção: os valores de a,b e c devem ser maiores que 0!'
    elif a >= b + c:
        return 'As medidas não formam um triângulo!'
    elif b >= a + c:
        return 'As medidas não formam um triângulo!'
    elif c >= b + a:
        return 'As medidas não formam um triângulo!'
    elif  a == b == c:
        return 'Triângulo Equilátero!'
    elif a != b  and b != c and c != a:
        return 'Triângulo Escaleno!'
    else:
        return 'Triângulo Isósceles!'
while True:
    print('='*50,'TIPOS DE TRIÂNGULO','='*50)
    a = float(input('Informe o valor do lado A:'))
    b = float(input('Informe o valor do lado B:'))
    c = float(input('Informe o valor do lado C:'))

    print(formacao_triangulos(a,b,c))
















