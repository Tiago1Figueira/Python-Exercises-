"""
#1
vetor1 = [ ]
vet_impares = []
for i in range(0,51):
    vetor1.append(i)
    if i % 2 != 0 or  vetor1 % 2 !=0:
        vet_impares.append(i, vetor1)
# aqui a solução envolve o uso do 'import randon' para a escolha dos 10 números em 50 possibilidades.
"""

#2
vetor = [ ]
vetor_impar = [ ]
for i in range(1,5):
    num = float(input(f'Informe o {i}° número de 0 a 50:'))
    while num != int(num) or num < 0 or num > 50:
        print('Número inválido!')
        num = float(input(f'Informe o {i}° número de 0 a 50:'))
    vetor.append(num)
    for i in vetor:
        if int(i) % 2 != 0:
            vetor_impar.append(i)
    for indice, i in enumerate(vetor):
        print(indice, i)
# nao sei como fazer pra que o número imprima dois vetores por linha como pedido no enunciado.





