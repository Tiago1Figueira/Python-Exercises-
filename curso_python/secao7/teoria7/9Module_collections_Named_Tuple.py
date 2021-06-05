"""
Module collections - Named tuple
Recapitulando
tupla = (1,2,3)
print(tupla[2])

Named tuple
Named tuple: são tipos diferenciados de tuplas nas quais especificamos o nome dela e também parâmetros.

"""
#Importando
#1
from collections import namedtuple
#precisamos definir o nome e os parâmetros.

#forma 1 (declaração named tuple)
cachorro = namedtuple('cachorro', 'idade raça nome')

# forma 2 (declaração named tuple)
cachorro = namedtuple('cachorro', 'idade,raça,nome')

#forma 3(declaração named tuple)
cachorro = namedtuple('cachorro',['idade', 'raça', 'nome'])

#2
ray = cachorro(idade=2, raça="chou", nome="ray")
print(ray)
#2
#chou
#ray

#3
#acessando os dados

#forma 1
ray = cachorro(idade=2, raça="chou", nome="ray")
print(ray[0])
print(ray[1])
print(ray[2])
#2
#chou
#ray


#forma 2
ray = cachorro(idade=2, raça="chou", nome="ray")
print(ray.idade)
print(ray.raça)
print(ray.nome)
#2
#chou
#ray

#3
print(ray.index('chou'))# como na tupla o comando index mostra o índice do elemento chou.
print(ray.count('chou')) # como na tupla o comando count mostra quantos elementos 'chou' existem na tupla.
#1
#1
