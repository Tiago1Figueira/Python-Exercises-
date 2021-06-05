# as vezes não se escreve data válida ou não aparece qquer informação sobre validade ou invalidade.
"""
dia = int(input('Informe o dia'))

while dia < 1 or dia > 31:

    print('Dia inválido')

    dia = int(input('Informe o dia'))

mes = int(input('Informe o mês'))

while mes < 1 or mes > 12:

    print('Mês inválido')

    mes = int(input('Informe o mês'))

ano = int(input('Informe o ano'))

while ano < 1 or ano > 9999:

    print('Ano inválido')

    ano = int(input('Informe o ano'))

bisexto = False

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :

    bisexto = True

if dia == 31 and mes != 1 and mes != 3 and mes != 5 and mes != 7 and mes != 8 and mes != 10 and mes != 12:

    print('A data não é valida')

elif mes == 2 and dia == 30:

    print('A data não é valida')

elif mes == 2 and dia == 29 and bisexto == False:

    print('A data não é valida')

else:

    print('A data é válida')
"""

def validade_data(dia,mes,ano):
    meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho', 7:'Julho', 8:'Agosto', 9:'Setembro',
        10:'Outubro', 11:'Novembro', 12:'Dezembro'}
    bissexto = False
    if 1 > dia or dia > 31:
        print('Dia inválido!')
    elif 1 > mes or mes > 12:
        print('Mês inválido!')
    elif 1 > ano or ano >=9999:
        print(('Ano inválido!'))

    elif ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
        bissexto = True
    #exceções que geram datas inválidas
    elif dia == 31 and mes != 1 and mes != 3 and mes != 5 and mes != 7 and mes != 8 and mes != 10 and mes != 12:
        print('1O dia é inválido!')
    elif mes == 2 and dia >= 30:
        print('2O dia é inválido!')
    elif mes == 2 and dia == 29 and bissexto == False:
        print('3O dia é inválido!')
    else:
        print('A data é válida!')
    return f'{dia} de {meses[mes]} de {ano}'
while True:
    print('=' * 50, 'CALCULO DA DATA:', '=' * 50)
    dia = int(input('Informe o dia:'))
    mes = int(input('Informe o mês:'))
    ano = int(input('Informe o ano:'))

    print(validade_data(dia,mes,ano))
