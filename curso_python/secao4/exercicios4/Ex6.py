# c = celsius
# f = fahrenheit
while True:
    print('=' * 50, 'CONVERSOR: CELCIUS PARA FAHRENHEIT', "=" * 50)
    c = float(input('Informe o valor da temperatura em Celsius:'))
    f = c * (9/5) + 32
    print(f'A temperatura {c} Celsius é igual a {f:.2f} fahrenheit.')

