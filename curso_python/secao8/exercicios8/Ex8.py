def calculo_hipotenusa(a,b):
    h = (a**2 + b**2)**0.5
    return f'O valor da hipotenusa é {h:.2f}'

cateto_a = float(input('Informe o valor do cateto A:'))
cateto_b = float(input('Informe o valor do cateto B:'))

print(calculo_hipotenusa(cateto_a,cateto_b))



