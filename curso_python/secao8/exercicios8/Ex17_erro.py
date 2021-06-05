"""
#0
def soma(*args):
    return sum(args)

print(soma(2,4))

#1
def soma(*args):
    for numero in args:
        if numero < 0:
            return 'Os números devem ser positivos e inteiros!'

        for numero in args:
            return sum(args)

a = int(input('Informe o 1° número:'))
b = int(input('Informe o 2° número:'))

print(soma(a,b))


#2
def soma_digitos(num1,num2):
    soma = 0
    for algarismos in num1:
        soma += algarismos
        return f'O valor da soma dos dígitos do número 1 é {soma}!'
    for algarismos in num2:
        soma += algarismos
        return f'O valor da soma dos dígitos do número 2 é {soma}!'

a = input('Informe o primeiro número com dois dígitos:')
b = input('Informe o segundo número com dois dígitos:')

print(soma_digitos(a,b))

#3
def soma_entre(num1,num2):
    numeros = num1, num2
    for numero in numeros:
        if numero < 0 or numero != int(numero):
          return 'Os números devem ser inteiros e positivos.'
    soma = 0
    for valor in range(num1 + 1, num2):
        soma = soma + valor
    return f'A soma dos números entre {num1} e {num2} é {soma}.'

while True:
    a = float(input('Informe o 1° número:'))
    b = float(input('Informe o 2° número:'))

    print(soma_entre(a,b))

#4
def soma_numeros(num1,num2):
    numeros = num1, num2
    for numero in numeros:
        if numero < 0 or numero != int(numero):
            return 'Os números devem ser positivos e inteiros!'
    soma = 0
    for numero in range(num1 + 1, num2):
        soma += numero
    return f'O valor da soma entre os números {num1} e {num2} é {soma}!'
while True:
    a = float(input('Informe o 1° número:'))
    b = float(input('Informe o 2° número:'))

    print(soma_numeros(a,b))

"""
#5 A soma entre o primeiro e segundo números está dando!
def soma_entre(num1,num2):
    if num1 < 0 or num2 < 0 or num1 != int(num1) or num2 != int(num2):
        return 'Os números devem ser positivos e inteiros!'
    soma = 0
    for numero in range(num1 +1 , num2):
        soma = soma + numero
        return f'A soma dos números entre {num1} e {num2} é {soma}!'
while True:
    a = int(input('Informe o 1° número:'))
    b = int(input('Informe o 2° número:'))
    print(soma_entre(a,b))

