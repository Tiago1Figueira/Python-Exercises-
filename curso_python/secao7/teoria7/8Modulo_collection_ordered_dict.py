"""
Modulo Collection : OrderedDict
Terminal/python/dir({})/help({}) para obter ajudar sobre comandos com dicionários.
Em um dicionário a ordem de inserção dos elementos não é garantida.

#1
#Em um dicionário não há garantia de que a sequência digitada será a sequência no 'print'.
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }
for chave, valor in dicionario.items():
    print(f'chave = {chave} e valor = {valor}')

chave = a e valor = 1
chave = b e valor = 2
chave = c e valor = 3
chave = d e valor = 4
chave = e e valor = 5

#2
# orderedDict é um comando que nos garante a ordem de inserção dos elementos no dicionario.
#fazendo o import
from collections import OrderedDict
dicionario = OrderedDict ({'a': 1, 'b': 2, 'c':3, 'd':4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave = {chave} valor = {valor}')

chave = a e valor = 1
chave = b e valor = 2
chave = c e valor = 3
chave = d e valor = 4
chave = e e valor = 5

"""
