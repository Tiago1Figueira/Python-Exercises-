desconto = 0.12
while True:
    print('=' * 50, 'CALCULE VALOR PRODUTO COM DESCONTO:', '=' * 50)
    valor = float(input('Informe o valor do produto:'))
    valor_final = valor - (valor * desconto)
    print(f'O valor de produto já descontado é {valor_final:.2f}!')

