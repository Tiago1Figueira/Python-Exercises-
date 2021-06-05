while True:
    print('='*50,'ESCOLHA UMA OPERAÇÃO','='*50)
    print('Opções:\n1-Geométrica\n2-Ponderada\n3-Harmônica\n4-Aritmética\n5-Sair')
    opc = int(input('N°:'))
    if opc < 1 or opc > 5:
        print('Atenção: número inválido!')
        print('Opções:\n1-Geométrica\n2-Ponderada\n3-Harmônica\n4-Aritmética\n5-Sair')
        opc = int(input('N°:'))
    if opc == 1:
        x = int(input('Informe X:'))
        y = int(input('Informe Y:'))
        z = int(input('Informe Z:'))
        geometrica = (x*y*z) ** 1/3
        print(f'A média geométrica dos números {x}, {y}, {z} é igual a {geometrica:.2f}!')
    if opc == 2:
        x = int(input('Informe X:'))
        y = int(input('Informe Y:'))
        z = int(input('Informe Z:'))
        ponderada = (x+2 * y+3 * z) / 6
        print(f'A média ponderada dos números {x}, {y}, {z} é igual a {ponderada:.2f}!')
    if opc == 3:
        x = int(input('Informe X:'))
        y = int(input('Informe Y:'))
        z = int(input('Informe Z:'))
        harmonica =  1 / 1/x + 1/y + 1/z
        print(f'A média harmônica dos números {x}, {y}, {z} é igual a {harmonica:.2f}!')
    if opc == 4:
        x = int(input('Informe X:'))
        y = int(input('Informe Y:'))
        z = int(input('Informe Z:'))
        aritmetica = (x + y+ z) / 3
        print(f'A média aritmética dos números {x}, {y}, {z} é igual a {aritmetica:.2f}!')
    if opc ==5:
        print('Você saiu!')
        break


