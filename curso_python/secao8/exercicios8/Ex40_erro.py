# o número de pares não está batendo com o que foi inserido no vetor.
lista = [ ]
def pares_na_funcao(num):
    if num % 2 == 0:
        lista.append(num)
    return f'O vetor possui {len(lista)} número par!'
while True:
    qtd = int(input('Informe quantos números o vetor terá:'))
    for i in range(1, qtd + 1):
        a = int(input(f'Informe o {i}° número:'))
    print(pares_na_funcao(a))


