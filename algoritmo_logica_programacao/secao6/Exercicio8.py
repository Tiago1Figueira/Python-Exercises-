#entrada
num = int(input('Informe o número:'))
#processamento
if num > 0:
    if num % 2 ==0:
        print(f'O número {num} é positivo e par!')
    else:
        print(f'O número {num} é positivo e ímpar!')
else:
    if num % 2 ==0:
        print(f'O número {num} é negativo e par!')
    else:
        print(f'O número {num} é positivo e ímpar!')

