#variáveis
maior = 0
#entradas
num = float(input('Informe o número:'))
#processamento
while num !=0:
    if num > maior:
        maior = num
    num = float(input('Informe o número:'))
print(f'O maior número é {maior}')
