#depois de selecionar a opção 5 a frase 'Informe o valor do produto:' aparece e eu não sei tirá-la depois
#dessa opção. O que eu posso fazer?
print('=' * 50, 'CÁLCULO PREÇO FINAL DO PRODUTO', '=' *50)
print('Estado de destino:\n1- Minas Gerais\n2- São Paulo\n3- Mato Grosso\n4- Rio de Janeiro\n5- Sair')
opc = int(input('Opção n°:'))
while opc < 1 or opc > 5:
    print('Atenção: Estado Inválido!\n')
    print('Estado de destino:\n1- Minas Gerais\n2- São Paulo\n3- Mato Grosso\n4- Rio de Janeiro\n5- Sair')
    opc = int(input('Opção n°:'))
valor_produto = float(input('Informe o valor do produto:'))

while True:
    if opc == 1:
        valor_final = valor_produto + (valor_produto * 7/100)
        print(f'O valor final do produto é {valor_final}!\n')
    if opc == 2:
        valor_final = valor_produto + (valor_produto * 12 / 100)
        print(f'O valor final do produto é {valor_final}!\n')
    if opc == 3:
        valor_final = valor_produto + (valor_produto * 8 / 100)
        print(f'O valor final do produto é {valor_final}!\n')
    if opc == 4:
        valor_final = valor_produto + (valor_produto * 15 / 100)
        print(f'O valor final do produto é {valor_final}!\n')
    if opc == 5:
        print('Você saiu!!')
        break
    print('=' * 50, 'CÁLCULO PREÇO FINAL DO PRODUTO', '=' *50)
    print('Estado de destino:\n1- Minas Gerais\n2- São Paulo\n3- Mato Grosso\n4- Rio de Janeiro\n5- Sair')
    opc = int(input('Opção n°:'))
    while opc < 1 or opc > 5:
        print('Atenção: Estado Inválido!\n')
        print('Estado de destino:\n1- Minas Gerais\n2- São Paulo\n3- Mato Grosso\n4- Rio de Janeiro\n5- Sair')
        opc = int(input('Opção n°:'))
    valor_produto = float(input('Informe o valor do produto:'))

