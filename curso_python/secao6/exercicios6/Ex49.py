"""
#1
meses = 0
salario1 = float(input("Digite o salário de Carlos:"))
salario2 = salario1 / 3
while salario2 < salario1:
    salario2 += (salario2 * 0.05)
    salario1 += (salario1 * 0.02)
    meses += 1
print(f"O salario de João demorará {meses} para ultrapassar o salário de Carlos")

#2
porc_caderneta = 2/100
por_rendafixa = 5/100
meses = 0
sal_carlos = int(input('Informe o salário do Carlos:'))
sal_joao = sal_carlos * 1/3

while sal_joao < sal_carlos: # Aqui salário do Carlos e do João é igual aos seus investimentos!!
    sal_carlos = sal_carlos + (sal_carlos * porc_caderneta)
    sal_joao = sal_joao + (sal_joao * por_rendafixa)
    meses += 1
print(f'O salário do João demorará {meses} meses para ser maior que o do Carlos!')

#3
taxa_carlos = 0.02
taxa_joao = 0.05
cont_meses = 0
carlos = float(input('Informe o salário do Carlos:'))
joao = carlos / 3
while joao < carlos:
    carlos += (carlos * taxa_carlos)
    joao += (joao * taxa_joao)
    cont_meses += 1
print(f'O montante do investimento de João será maior que o de Carlos em {cont_meses} meses!')

"""
#3
cont = 0
icarlos = 2/100
ijoao = 5/ 100
while True:
    print('='*80)
    carlos = float(input('Informe o salário:'))
    joao = carlos / 3

    while joao < carlos:
        carlos += (carlos * icarlos)
        joao += (joao * ijoao)
        cont += 1
    print(f'O número de meses que João precisa para igualar ou ultrapassar o salário de Carlos é {cont}!')



















