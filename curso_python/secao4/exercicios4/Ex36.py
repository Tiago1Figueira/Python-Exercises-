pi = 3.141592
while True:
    print('=' * 50, 'CALCULE ÁREA DO CILINDRO CÍRCULAR:', '=' * 50)
    a = float(input('Informe a altura do cilindro em centímetros:'))
    r = float(input('Informe o raio do cilindro em centímetros:'))
    volume = pi * r**2 * a
    print(f'O volume do cilíndro circular é {volume:.2f} cm3!')
