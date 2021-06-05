"""
#1
linha = 1
numero = 1
valor = 1
qtd_linhas = int(input('Entre com um valor inteiro positivo: '))
print('\n')
while linha <= qtd_linhas:
    while numero <= linha:
        if numero == 1:
            print(f'N = {str(linha).zfill(2)} | ', end='')
        print(str(valor).zfill(2), end='')
        print(' ', end='')
        numero += 1
        valor += 1
    print('\n', end='')
    numero = 1
    linha += 1
"""




















