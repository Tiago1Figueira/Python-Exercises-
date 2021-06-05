"""
#1
def data(dia,mes,ano):
    meses = {1: 'Janeiro', 2: 'Feveiro', 3:'Março', 4: 'Abril', 5: 'Maio', 6:'Junho', 7:'Julho', 8:'Agosto',
             9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}
    return f' {dia} de {meses[mes]} de {ano}'

print(data(1,2,2000))

#2
def data(dia,mes,ano):
    meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho', 7:'Julho', 8:'Agosto', 9:'Setembro',
             10:'Outubro', 11:'Novembro', 12: 'Dezembro'}
    return f'{dia} de {meses[mes]} de {ano} '

print(data(1,2,2000))

#3
def data(dia,mes,ano):
    meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho',
             7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}
    return f'{dia} de {meses[mes]} de {ano}'

print(data(1,5,2000))

#4
def data(dia,mes,ano):
    meses = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September',
             10:'October', 11:'November', 12:'December'}
    return f'{dia} of {meses[mes]}  {ano}'

a = int(input('Informe um dia:'))
b = int(input('Informe um mês:'))
c = int(input('Informe um ano:'))

print(data(a,b,c))

#5
def data(dia,mes,ano):
    meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho',
             7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}
    return f'{dia} de {meses[b]} de {ano}'

while True:
    print('*'*100)
    a = int(input('Informe o dia desejado:'))
    b = int(input('Informe o mês desejado:'))
    c = int(input('Informe o ano desejado:'))
    print(data(a,b,c))

#6
def data(dia,mes,ano):
    meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho', 7:'Julho',
             8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}
    return f'{dia} de {meses[b]} de {ano}'

while True:
    a = int(input(f'Informe o dia:'))
    b = int(input(f'Informe o mês:'))
    c = int(input(f'Informe o ano:'))
    print(data(a,b,c))

"""
def data(dia, mes, ano):
    meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho',
             7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}
    return f'{dia} de {meses[mes]} de {ano}'

while True:
    print('*' * 100)
    dia = int(input('Informe o dia:'))
    mes = int(input('Informe o mês:'))
    ano = int(input('Informe o ano:'))

    print(data(dia,mes,ano))


























































