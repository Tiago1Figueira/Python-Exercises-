"""
print('Este programa recebe os elementos de uma matriz 4x4 e retorna a posição do maior elemento.')

matriz = [[int(input(f'Elemento {i}{j}: ')) for j in range(4)] for i in range(4)]

maior = max(max(linha) for linha in matriz)

posicao = [str(matriz.index(linha)) + str(linha.index(n)) for linha in matriz for n in linha if n == maior]

print(f"Linha/Coluna do maior elemento: {'/'.join(posicao[0])}")
"""