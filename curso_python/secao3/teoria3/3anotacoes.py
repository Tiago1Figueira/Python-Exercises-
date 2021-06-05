"""
#PEP8 - PYTHON_ENHANCEMENT_PROPOSAL(guia de estilos ou padrão do código python)
propostas de melhoria do python - zen o python! usando o comando 'import this'!

#1
dir vs help
dir('geek') obtem as funções que podem ser usadas para essa string. ex.: dir('geek), uma delas e o lower.
Logo, 'Geek'.lower(). O que ele faz? Aí entra o help. help('Geek'.lower).
Explicação: converte para lowercase(minúscula).

#2
'GEEK'.lower()
'geek'

#3
'geek'.upper()
'GEEK'

#4
'geek'.title()
'Geek'

#5
'ANGELINA JOLIE'.lower().title()
'Angelina Jolie'

#RECEBENDO DADOS
input() = tudo o que vem do input é do tipo string. (Tudo o que está entre aspas é string!)
print('A %s tem %s anos'% (nome,idade) )         #forma antiga do python!
print('A {0} tem {1} anos.'.format(nome,idade)   #forma moderna do python!
print(f'A {nome} tem {idade} anos.')             #forma mais moderna do python!

"""


