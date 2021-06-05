while True:
    print('=' * 150)
    degrau = float(input('Informe a altura do degrau em cm:'))
    altura = float(input('Informe a altura que se quer chegar em cm:'))
    objetivo_degraus = altura / degrau
    print(f'O objetivo será alcançado depois de {objetivo_degraus} degraus.')

