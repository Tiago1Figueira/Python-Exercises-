"""
lista = []
def vetor_maior(*args):
    lista.append(*args)
    return f'O maior número do vetor é {max(*args)}!'
opc = int(input('Informe quantos números você deseja digitar:'))
for numero in range(1, opc + 1):
    a = int(input(f'Informe o {numero}° número:'))
print(vetor_maior(a))
"""

