"""
Módulos collections default dict

#para se obter mais informaçoes sobre o 'defaultdict'
#checar: docs.python/3/library/collections.html#collections.defaultdict

#1- Recapitulando Dicionários
dict vem de dicionários.
dicionario = {'curso': 'Programação em Python essencial '}
print(dicionario)
#{'curso': 'Programação em Python essencial '}

print(dicionario['curso'])# aqui 'curso' é visto como uma chave e o resto é o valor.
#Programação em Python essencial

#2
O que fazer qdo uma chave nao encontra um valor respectivo, como a chave 'outro', e da KeyError?
print(dicionario['outro'])
KeyError: 'outro'

Podemos criar um default dict para essa situação.
Default dict: criando um dicionario com default dict,podemos informar um valor default podendo utilizar um lambda para isso.
Esse valor será utilizado sempre que não houver um valor definido.
Caso tentemos acessar uma chave que não existe, essa chave será criada e o valor default será atribuido.
obs.: lambdas são funçoes sem nome que podem ou não receber parâmetros de entrada e retornar valores.

"""

#fazendo o import

from collections import defaultdict
dicionario = defaultdict(lambda : 0)
dicionario['curso'] = 'Programação em Python Essencial'
print(dicionario)
#defaultdict(<function <lambda> at 0x7fb423a44c10>, {'curso': 'Programação em Python Essencial'})

print(dicionario['outro'])# o keyerror não acontece aqui.
print(dicionario)
#0
#defaultdict(<function <lambda> at 0x7faf04d20c10>, {'curso': 'Programação em Python Essencial', 'outro': 0})
