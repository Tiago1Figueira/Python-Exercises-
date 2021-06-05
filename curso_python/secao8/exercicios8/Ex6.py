def calculo_segundos(horas,minutos,segundos):
    qtos_segundos = horas*3600 + minutos*60 + segundos
    return f' {horas} hora(s) {minutos} minuto(s) e {segundos} segundo(s) são iguais a {qtos_segundos} segundos!'

a = int(input('Informe quantas horas:'))
b = int(input('Informe quantas minutos:'))
c = int(input('Informe quantas segundos:'))

print(calculo_segundos(a,b,c))

