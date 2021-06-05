bonus = 0
while True:
    print('=' * 150)
    sal = int(input('Informe o salário atual:'))
    temposer = int(input('Informe o tempo de serviço:'))
    if temposer < 1:
        bonus = 0
    elif temposer >= 1 and temposer <= 3:
        bonus = 100
    elif temposer >= 4 and temposer <= 6:
        bonus = 200
    elif temposer >= 7 and temposer <= 10:
        bonus = 300
    else:
        bonus = 500
    if sal > 2000 and temposer < 1:
        print('Sem bônus ou reajuste!')
    elif sal <= 500:
        sal = sal + (sal * 0.25) + bonus
    elif sal <= 1000:
        sal = sal + (sal * 0.20) + bonus
    elif sal <= 1500:
        sal = sal + (sal * 0.15) + bonus
    elif sal <= 2000:
        sal = sal + (sal * 0.10) + bonus
    else:
        sal = sal + (sal * 0.00) + bonus
    print(f'O seu salário ajustado é {sal}!')


