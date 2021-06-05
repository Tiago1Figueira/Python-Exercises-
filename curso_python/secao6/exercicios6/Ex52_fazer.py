"""
# exercicio muito dificil!
#1
moeda001 = 0
moeda005 = 0
moeda010 = 0
moeda025 = 0
moeda050 = 0
moeda1 = 0
nota2 = 0
nota5 = 0
nota10 = 0
nota20 = 0
nota50 = 0
nota100 = 0
saque = int(input('Informe o valor do saque:'))
print('Aguardando saque ....')
while True:
    if saque > 100:
        saque -= 100
        nota100 += 1
    if saque < 100 and saque > 50:
        saque -= 50
        nota50 += 1
    if saque < 50 and saque > 20:
        saque -= 20
        nota20 += 1
    if saque < 20 and saque > 10:
        saque -= 10
        nota10 += 1
    if saque < 10 and saque > 5:
        saque -= 5
        nota5 += 1
    if saque < 5 and saque > 2:
        saque -= 2
        nota2 += 1
    if saque < 2 and saque > moeda1:
        saque -= 1
        moeda1 += 1
print(f' ')

"""

#2
notas = [1, 2, 5, 10, 20, 50, 100]
valor_saque = int(input('Insira o valor que deseja sacar: '))
notas_saque = []

notas.sort(reverse=True)
print(notas)

for i in range(len(notas)):
    while valor_saque - notas[i] >= 0:
        valor_saque -= notas[i]
        notas_saque.append(notas[i])

print(notas_saque)

