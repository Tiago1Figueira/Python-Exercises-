def retorna_farenheit(c):
    f = c * (9/5) + 32
    return f'{c}° Celsius são iguais a {f}° Fahrenheit!'

c = float(input('Informe quantos graus Celsius serão convertidos para Fahrenheit:'))
print(retorna_farenheit(c))
