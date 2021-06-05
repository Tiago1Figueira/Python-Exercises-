"""
#1
hora_i = int(input('Insira a hora de início: '))
minuto_i = int(input('Insira os minutos de início: '))
segundo_i = int(input('Insira os segundos de início: '))
duracao = int(input('Insira a duração do experimento: '))

hora_seg = hora_i * 3600
minutos_seg = minuto_i * 60

total_segundos = hora_seg + minutos_seg + segundo_i + duracao
hora_f = int(total_segundos / 3600)
rest_seg = total_segundos % 3600
minuto_f = int(rest_seg / 60)
rest_seg = rest_seg % 60
print(f'O experimento terminou às {hora_f}:{minuto_f}:{rest_seg}')

#2
horas_i = int(input('Informe a hora:'))
minutos_i = int(input('Informe os minutos:'))
segundos_i = int(input('Informe os segundos:'))
duracao = int(input('Informe a duração do experimento em segundos:'))
horas_seg = horas_i * 3600
minutos_seg = minutos_i * 60
segundos_seg = segundos_i
total_seg = horas_seg + minutos_seg + segundos_seg + duracao

horas_f = int(total_seg / 3600)
rest_seg = total_seg % 3600
minutos_f = int(rest_seg / 60)
segundos_f = rest_seg % 60
print(f'O horário de término do experimento foi as {horas_f}:{minutos_f}:{segundos_f}!')

"""
#3
hora = int(input('Informe a hora do início do evento:'))
minutos = int(input('Informe os minutos do início do evento:'))
segundos = int(input('Informe os segundos do início do evento:'))
duracao = int(input('Informe a duração do evento:'))

hora_i = hora * 3600
minutos_i = minutos * 60
segundos_i = segundos
total = hora_i + minutos_i + segundos_i + duracao
hora_f = int(total / 3600)
rest_seg = total % 3600
minutos_f = int(rest_seg / 60)
segundos_f = rest_seg % 60
print(f'O horário final do experimento começado as {hora}:{minutos}:{segundos} é {hora_f}:{minutos_f}:{segundos_f}!')






























