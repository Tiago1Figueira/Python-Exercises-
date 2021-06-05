lista = [ ]
while True:
    print("=" * 50,'CALCULE A SOMA DOS QUADRADOS DE 3 NÚMEROS', "=" * 50)
    for i in range(1,4):
        num = float(input(f'Informe o {i}° número:'))
        lista.append( (num)**2)

    print(f'O valor da soma dos números é {sum(lista)}!')
    lista.clear()
