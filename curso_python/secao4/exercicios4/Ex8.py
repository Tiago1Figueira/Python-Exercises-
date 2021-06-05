# k = Kelvin
# c = Celsius
while True:
    print('=' * 50, 'CONVERSOR: KELVIN PARA CELSIUS', '=' * 50)
    k = float(input('Informe a temperatura em Kelvin:'))
    c = k - 273.15

    print(f'A temperatura {k}° Kelvin é igual a {c:.2f}° Celsius.  ')

