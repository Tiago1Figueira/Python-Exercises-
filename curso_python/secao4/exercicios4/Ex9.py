# k = Kelvin
# c = Celsius
while True:
    print('=' * 50, 'CONVERSOR: CELSIUS PARA KELVIN ', '=' * 50)
    c = float(input('Informe a temperatura em Celsius:'))
    k = c + 273.15
    print(f'A temperatura {c}° Celsius é igual a {k:.2f}° Kelvin.  ')

