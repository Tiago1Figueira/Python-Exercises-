"""
while True:
    print('=' * 150)
    valor = int(input('Informe um valor em segundos:'))
    hora = int(valor / 3600)
    rest_seg = valor % 3600
    minutos = int(rest_seg / 60)
    segundos = rest_seg % 60
    print(f'O número de {valor} segundos é igual a {hora}:{minutos}:{segundos}!')

"""
#2
while True:
    print('=' * 150)
    segundos = int(input('Informe a quantidade em segundos:'))
    horas = int(segundos / 3600)
    rest_segundos = segundos % 3600
    minutos = int(rest_segundos / 60)
    segundos1 = rest_segundos % 60
    print(f'{segundos} segundos são iguais a {horas}:{minutos}:{segundos1}!')





