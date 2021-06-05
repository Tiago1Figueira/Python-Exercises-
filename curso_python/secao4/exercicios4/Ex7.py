# c = celsius
# f = fahrenheit
while True:
    print('=' * 50, 'CONVERSOR: FAHRENHEIT PARA CELSIUS', '=' * 50)
    f = float(input('Informe a temperatura em Fahrenheit:'))
    c = 5 * (f - 32) / 9

    print(f'A temperatura {f}° Fahrenheit é igual a {c}° Celsius.  ')

