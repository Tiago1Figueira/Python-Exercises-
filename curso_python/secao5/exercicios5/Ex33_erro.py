while True:
    print('='*50, 'CALCULO DE PREÇO', '=' *50)
    preco = float(input('Informe o preço do produto:'))
    if preco < 50:
        preco_aumentado = preco + (preco * 0.05)
    elif preco > 50 or preco < 100:
        preco_aumentado = preco + (preco * 0.10)
    else:
        preco_aumentado = preco + (preco * 0.15)

    if preco_aumentado < 80:
        print(f'O preço {preco_aumentado:.2f} é barato!')
    elif 80 <= preco_aumentado >= 120:
        print(f'O preço {preco_aumentado:.2f} é normal!')
    elif 120 < preco_aumentado >= 200:
        print(f'O preço {preco_aumentado:.2f} é caro!')
    else:
        print(f'O preço {preco_aumentado:.2f} é muito caro!')
# o código não está encaixando o preço aumentado na banda correta. Ex. 123 depois do aumento vira 135.30
#e é considerado normal,qdo seria caro!
