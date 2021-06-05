"""
#1
def elevado(*args):
    resultado = 0
    for numero in args:
        print(numero)
        resultado = args[0] ** args[1]
    return {resultado}

print(elevado(2, 8)) #256

#2
def elevado(x,z):
    return f'O valor de {x} elevado a {z} é {x ** z} '

x = float(input('Informe um número:'))
z = float(input('Informe o expoente para o cálculo:'))

print(elevado(x,z))

"""




