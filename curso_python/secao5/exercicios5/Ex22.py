while True:
    print('=' * 50,'CÁLCULO PARA A APOSENTADORIA', '='*50)
    idade = int(input('Informe a sua idade:'))
    tempo_servico = float(input('Informe o seu tempo de serviço:'))
    if idade >= 65 or tempo_servico >=30 or idade >=60 and tempo_servico >= 25 :
        print('Pode se aposentar!')
    else:
        print('Não pode se aposentar!')

print('=' * 50, 'CÁLCULO PARA A APOSENTADORIA', '=' * 50)
idade = int(input('Informe a sua idade:'))
tempo_servico = float(input('Informe o seu tempo de serviço:'))

"""

if idade >= 65:
    print('Pode se aposentar!')
if tempo_servico >= 30:
    print('Pode se aposentar!')
if idade >= 60 and tempo_servico >= 25:
    print('Pode se aposentar!')
else:
    print('Não pode se aposentar!')
"""