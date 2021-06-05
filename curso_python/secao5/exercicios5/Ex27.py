while True:
    print('='* 50, "CATEGORIA DO NADADOR", '=' * 50)
    idade = int(input('Informe a idade do nadador:'))
    if idade < 5:
        print('Muito Jovem!')
    if idade >=5 and idade <=7:
        print(f'Categoria Infantil A!')
    if idade >=8 and idade <=10:
        print('Categoria Infantil B!')
    if idade >=11 and idade <= 13:
        print('Categoria Juvenil A!')
    if idade>=14 and idade <=17:
        print('Categoria Juvenil B!')
    if idade>=18:
        print('Categoria Sênior!')
