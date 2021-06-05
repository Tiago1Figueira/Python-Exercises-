#código está com erro e não gera resultado! Modificar o código! Entende melhor o fatorial!
def soma_algarismos_fatorial(num):
    if num < 0 or num != int(num):
        return'O número deve ser inteiro e positivo!'
    fatorial = 1
    soma = 0
    for i in range(1, num + 1):
        fatorial *= i
        for i in fatorial:
            soma += fatorial

while True:
    a = int(input('Informe um número positivo e inteiro:'))
    print(soma_algarismos_fatorial(a))

