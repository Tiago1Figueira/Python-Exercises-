#variáveis
maior = -999
menor = 999
media = 0
soma = 0
#entrada/processamento
for num in range(1,11):
    num = int(input('Informe um número:'))
    if num > 0:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        soma = soma + num
    else:
        num = int(input('Informe um número:'))
media = soma / 10
#saída
print(f'O maior número é {maior}.')
print(f'O menor número é {menor}.')
print(f'A média dos números é {media}')




