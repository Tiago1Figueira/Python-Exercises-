#1
comissao1 = 0.05
imposto1 = 0.00
comissao2 = 0.10
imposto2 = 0.15
comissao3 = 0.15
imposto3 = 0.20
while True:
    print('='*150)
    custo_fabrica = float(input('Informe o valor do custo de fábrica:'))
    if custo_fabrica < 12000:
        comissao = custo_fabrica * comissao1
        imposto = custo_fabrica * imposto1
    elif custo_fabrica >= 12000 and custo_fabrica <= 25000:
        comissao = custo_fabrica * comissao2
        imposto = custo_fabrica * imposto2
    else:
        comissao = custo_fabrica * comissao3
        imposto = custo_fabrica * imposto3
    print(f'Custo de fábrica {custo_fabrica:.2f}\ncomissão do distribuidor {comissao:.2f}\nimpostos {imposto:.2f}')

