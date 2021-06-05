#g = ângulo
# r = radianos
pi = 3.14
while True:
    print('=' * 50, 'CONVERSOR: GRAUS EM RADIANOS!', '=' * 50)
    g = float(input('Informe o valor do ângulo que deseja converter:'))
    r = g * pi / 180
    print(f'{g} graus são {r:.2f} radianos!!')
