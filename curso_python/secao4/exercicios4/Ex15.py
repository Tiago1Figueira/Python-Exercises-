#g = ângulo
# r = radianos
pi = 3.14
while True:
    print('=' * 50, 'CONVERSOR: RADIANOS EM GRAUS!', '=' * 50)
    r = float(input('Informe o valor dos radianos que deseja converter:'))
    g = r * 180 / pi
    print(f'{r} radianos são {g:.2f} graus!!')
