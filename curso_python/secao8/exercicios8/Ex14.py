def calculo_kml(km,litros):

    kml = km / litros
    if kml < 8:
        return f'{kml:.2f} quilômetros por litro! Venda o carro!'
    if kml >= 8 and kml <= 14:
        return f'{kml:.2f} quilômetros por litro! Econômico!'
    if kml > 14:
        return f'{kml:.2f} quilômetros por litro!Super Econômico!'
while True:
    print("=" * 50,'CÁLCULO QUILÔMETROS POR LITRO',"=" * 50)
    a = float(input('Informe quantos quilômetros percorreu:'))
    b = float(input('Informe quantos litros consumiu:'))

    print(calculo_kml(a,b))
