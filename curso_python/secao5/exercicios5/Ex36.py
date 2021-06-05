porc1 = 0.16
base1 = 700
porc2 = 0.14
base2 = 650
porc3 = 0.14
base3 = 600
porc4 = 0.14
base4 = 550
porc5 = 0.14
base5 = 500
porc6 = 0.14
base6 = 400

while True:
    print('=' * 50, 'CALCULE A COMISSÃO', '=' * 50)
    venda = float(input('Informe o valor da venda:'))
    if venda >= 100000:
        comissao = ( venda * porc1) + base1
        print(f'A comissão será de {comissao:.2f}')
    elif venda < 100000 and venda >= 80000:
        comissao = ( venda * porc2) + base2
        print(f'A comissão será de {comissao:.2f}')
    elif venda < 80000 and venda >= 60000:
        comissao = ( venda * porc3) + base3
        print(f'A comissão será de {comissao:.2f}')
    elif venda < 60000 and venda >= 40000:
        comissao = ( venda * porc4) + base4
        print(f'A comissão será de {comissao:.2f}')
    elif venda < 40000 and venda >= 20000:
        comissao = ( venda * porc5) + base5
        print(f'A comissão será de {comissao:.2f}')
    else:
        comissao = ( venda * porc6) + base6
        print(f'A comissão será de {comissao:.2f}')

