while True:
    print('=' * 150)
    idade = int(input('Informe a idade atual:'))
    ano = int(input('Informe o ano atual:'))
    nascimento = ano - int(idade)
    print(f'Data de nascimento = {nascimento}!')
