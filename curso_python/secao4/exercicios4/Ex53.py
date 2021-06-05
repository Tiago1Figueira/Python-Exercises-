# t = custo_da_tela, c = comprimento_terreno, l = largura_terreno
while True:
    print('='*150)
    t = float(input('Informe o valor da tela por m²:'))
    c = float(input('Informe o comprimento do terreno em metros:'))
    l = float(input('Informe a largura do terreno em metros:'))
    while l > c:
        print('Atenção: o comprimento deve ser maior do que a largura:')
        l = float(input('Informe a largura do terreno:'))
    area_terreno = c * l * t
    print(f'O valor para cercar o terreno por completo é {area_terreno:.2f} reais!')
