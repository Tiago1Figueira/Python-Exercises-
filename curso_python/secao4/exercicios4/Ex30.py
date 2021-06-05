cotacao = 5.4
while True:
    print('=' * 50, "CONVERSOR REAL - DÓLAR")
    real = float(input('Informe a quantia em real para obter quantia em dólares:'))
    dolar = real / cotacao
    print(f'A cotação de ${real} reais para dólares é ${dolar:.2f} dólares!')

