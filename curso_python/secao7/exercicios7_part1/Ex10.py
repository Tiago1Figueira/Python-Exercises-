"""
#1
notas = []
cont = 0
valores = 0
media = ' '
for i in range(1,5):#16
    num = float(input(f'Informe o {i}° nota:'))
    notas.append(num)
    notas.sort( )
    cont += 1
    valores += num
    #media = valores / cont
    media = sum(notas) / len(notas)

print(f'As notas são {notas} e a média geral das notas é {media:.2f}!')

"""
#2
notas = [ ]
for i in range(1,16):
    num = float(input(f'Informe o {i}° número:'))
    while num < 0 or num > 10:
        print('Nota inválida!')
        num = float(input(f'Informe o {i}° número:'))
    notas.append(num)
print(f'Média {sum(notas) / len(notas)}!')














