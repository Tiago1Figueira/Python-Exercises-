#entradas
indice = float(input('Informe um índice:'))
#processamento
if indice < 0.3:
    print('Níveis aceitável!')
elif indice >= 0.3 and indice < 0.4:
    print('Atenção: indústrias grupo 1 parem atividades!')
elif indice >= 0.4 and indice <0.5:
    print('Atenção: indústrias grupos 1 e 2 parem atividades!')
elif indice >= 0.5:
    print('Atencão: indústrias grupos 1, 2 e 3 parem atividades!')
