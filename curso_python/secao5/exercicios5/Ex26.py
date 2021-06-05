while True:
    print('=' * 50, 'CALCULE O CONSUMO DO VEÍCULO', '=' *50)
    quilometros = float(input('Informe quantos quilômetros foram percorridos:'))
    litros = float(input('Informe quantos litros foram consumido no percurso:'))
    kml = quilometros / litros
    print(f'O consumo foi igual a {kml:.2f} quilômetros por litro!')
    if kml < 8:
        print('Venda o carro!')
    elif kml >= 8 or kml > 14:
        print('Carro econômico!')
    elif kml >= 14:
        print('Carro super econômico!')


