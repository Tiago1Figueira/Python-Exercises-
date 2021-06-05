"""
#1
soma1 = 0
soma2 = 0
soma3 = 0
lista = []
hab = int(input('Digite o número de habitantes: '))
for c in range(1, hab + 1):
    print('\nOPÇÕES''\n[1] Residencial''\n[2] Comercial''\n[3] industrial')
    tip_cons = int(input(f'Para o habitante número {c}, qual o tipo de consumidor ele é?: '))
    if tip_cons == 1:
        kwh1 = float(input('Qual o consumo deste habitante: '))
        soma1 = soma1 + kwh1
        lista.append(kwh1)
    if tip_cons == 2:
        kwh2 = float(input('Qual o consumo deste habitante: '))
        soma2 = soma2 + kwh2
        lista.append(kwh2)
    if tip_cons == 3:
        kwh3 = float(input('Qual o consumo deste habitante: '))
        soma3 = soma3 + kwh3
        lista.append(kwh3)
print(f'O menor consumo entre todos os habitante: {min(lista):.2f}')
print(f'O maior consumo entre todos os habitantes: {max(lista):.2f}')
print(f'A média do consumo de todos os habitantes: {(soma1 + soma2 + soma3) / 3:.2f}')
print(f'A soma do consumo das Residências: {soma1:.2f}')
print(f'A soma do consumo dos Comércios: {soma2:.2f}')
print(f'A soma do consumo das industrias: {soma3:.2f}')

#2
print('=' * 60, 'CÁLCULO DO CONSUMO DA POPULAÇÃO', '=' * 60)
soma1 = soma2 = soma3 = 0
lista = []
populacao = int(input("INFORME A POPULAÇÃO DA CIDADE:"))
for i in range(1, populacao + 1):
    print(f'CÓDIGO DO {i}°HABITANTE :\n1-RESIDENCIAL:\n2-COMERCIAL:\n3-INDUSTRIAL:')
    codigo_habitante = int(input(f'INFORME CÓDIGO DO {i}° HABITANTE : 1, 2 OU 3 ? N°'))
    if codigo_habitante == 1:
        consumo_habitante1 = float(input((f'INFORME O CONSUMO DO {i}° HABITANTE - Valor:')))
        print('=' * 152)
        soma1 = soma1 + consumo_habitante1
        lista.append(consumo_habitante1)
    if codigo_habitante == 2:
        consumo_habitante2 = float(input((f'INFORME O CONSUMO DO {i}° HABITANTE - Valor:')))
        print('=' * 152)
        soma2 = soma2 + consumo_habitante2
        lista.append(consumo_habitante2)
    if codigo_habitante == 3:
        consumo_habitante3 = float(input((f'INFORME O CONSUMO DO {i}° HABITANTE - Valor:')))
        print('=' * 152)
        soma3 = soma3 + consumo_habitante3
        lista.append(consumo_habitante3)
        soma_total = soma1 + soma2 + soma3

print(f'Valores de consumo:\nMaior valor {max(lista)}\nMenor Valor {min(lista)}\nMédia dos Valores {soma_total/populacao}\n')
print(f'Total de consumo por categoria:\nResidencial {soma1}\nComercial {soma2}\nIndustrial {soma3}\n')
print('=' * 152)

#3
soma1 = 0
soma2 = 0
soma3 = 0
lista = []
hab = int(input('Informe o número de habitantes:'))
for i in range(1, hab + 1):
    print('CÓDIGO DO HABITANTE:\n1- RESIDENCIAL\n2- COMERCIAL\n3- INDUSTRIAL')
    cod = int(input(f'Informe o código do {i}° habitante: n°'))
    while cod < 1 or cod > 3:
        print('CÓDIGO DO HABITANTE:\n1- RESIDENCIAL\n2- COMERCIAL\n3- INDUSTRIAL')
        cod = int(input(f'Informe o código do {i}° habitante: n°'))
    if cod ==1:
        consumo1 = float(input(f'Informe o seu consumo de energia do {i}° habitante:'))
        print('=' * 70)
        soma1 += consumo1
        lista.append(consumo1)
    if cod ==2:
        consumo2 = float(input(f'Informe o seu consumo de energia do {i}° habitante:'))
        print('=' * 70)
        soma2 += consumo2
        lista.append(consumo2)
    if cod ==3:
        consumo3 = float(input(f'Informe o seu consumo de energia do {i}° habitante:'))
        print('=' * 152)
        soma3 += consumo3
        lista.append(consumo3)
print('=' * 55, 'RESULTADOS GERAIS DO CONSUMO', '=' * 55)
print(f'Seguem os dados dos valores de consumo:\n1- Maior Valor:{max(lista)}\n2- Menor Valor:{min(lista)}\n'
          f'3- Média:{soma1 + soma2 + soma3/ hab}')
print('=' * 55, 'RESULTADOS GERAIS DO CONSUMO', '=' * 55)
print(f'Classificação do consumo por código:\n1- Residêncial-valor:{soma1}\n2- Comercial-valor:{soma2}'
          f'\n3- Industrial-valor:{soma3}')
"""
#4








































