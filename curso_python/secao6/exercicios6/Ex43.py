"""
#1
soma = 0
media = 0
cont = 0
lista = []
idade = int(input('Informe a sua idade:'))
while idade != 0:
    idade = int(input('Informe a sua idade:'))
    soma += idade
    cont += 1
    media = soma / cont
    lista.append(idade)
print(f'Média das idades desse grupo é {media:.2f} e as idades informadas são {lista}')
# a primeira idade informada não está sendo usada no cálculo. Por quê?

#2
media = 0
soma = 0
cont = 0
idade = int(input('Informe a sua idade:'))
soma += idade
cont += 1
while idade > 0:
    idade = int(input('Informe a sua idade:'))
    soma += idade
    cont += 1
    if idade == 0:
        print('Programa finalizado!')
        break
    media = soma / cont
print(f'A idade média desse grupo é {media:.2f}!')

"""
#3
idades = [ ]
while True:
    num = float(input('Informe sua idade:'))
    while num != int(num):
        print('Idade inválida!')
        num = float(input('Informe sua idade:'))
    if num <= 0:
        print('Você saiu!')
        break
    else:
        idades.append(num)
print(f'A idade média desse grupo é {sum(idades)/ len(idades)}!')




















