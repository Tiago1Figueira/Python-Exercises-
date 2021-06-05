"""
#>>> tupla = (1,2,3)
#>>> dir(tupla)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
'__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
 '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
#>>>
Tuplas (parênteses) parecidas com as listas [colchetes].
Há 2 tipos básicos:
1- Tuplas são representadas por parênteses, mas as vezes não os têm.
2- Tuplas são imutáeis, ou seja, qdo criadas de um jeito não mudam; não podem aumentar ou diminuir.
Operações com tuplas geram outras tuplas.

Tuplas têm parenteses, mas as vezes, não os possuem.

tupla1 = (1,2,3,4,5,6)# com parênteses
print(tupla1)
print(type(tupla1))
(1, 2, 3, 4, 5, 6)
<class 'tuple'>

tupla2 = 1,2,3,4,5,6 # sem parênteses
print(tupla2)
print(type(tupla2))
(1, 2, 3, 4, 5, 6)
<class 'tuple'>

tupla3 = (4) # isso não é uma tupla! E considerada classificação 'inteiro'.
print(tupla3)
print(type(tupla3))
4
<class 'int'>

tupla4 = (4,) # isso é tupla!
print(tupla4)
print(type(tupla4))
(4,)
<class 'tuple'>

tupla5 = 4, # isso é tupla! Tuplas são definidas por vírgulas!
print(tupla5)
print(type(tupla5))
(4,)
<class 'tuple'>

Resumindo:
(4) não é tupla.
(4,) é tupla.
4, é tupla.

#1
tuplas = tuple(range(11))
print(tuplas)
print(type(tuplas))
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
<class 'tuple'>


#2 Desempacotamento de tupla
# Adicionar ou remover elementos de tuplas não existem, já que isso alteraria os seus elementos.
# gera erro se colocarmos um número diferente de elementos para desempacotarmos.
tupla = ('Geek University', 'Python Essencial')
escola, curso = tupla
print(escola)
print(curso)
Geek University
Python Essencial

#3 SOMA*, VALOR MÁXIMO*, VALOR MÍNIMO* E TAMANHO (Todos os valores devem ser números inteiros ou reais)
tupla = (1,2,3,4,5,6)
print(max(tupla))
6
print(min(tupla))
1
print(len(tupla))
6
print(sum(tupla))
21

#4
# Concatenação de tuplas(união)
# tuplas são imutáveis, mas podemos uni-las.
tupla1 = (1,2,3)
print(tupla1)
(1,2,3)
tupla2 = (4,5,6)
print(tupla2)
(4,5,6)
print(tupla1 + tupla2)
(1,2,3,4,5,6)

#4.1
tupla1 = (1,2,3)
tupla2 = (4,5,6)
tupla3 = tupla1 + tupla2
print(tupla1)
(1,2,3)
print(tupla2)
(4,5,6)
print(tupla3)
(1,2,3,4,5,6)

#4.2
# Tuplas são imutáveis e apesar disso, podemos sobrescrever tuplas criando outras sem alterações.
tupla1 = (1,2,3)
tupla2 = (4,5,6)
print(tupla1)
(1, 2, 3)
print(tupla2)
(4, 5, 6)
tupla3 = tupla1 + tupla2
print(tupla3)
(1, 2, 3, 4, 5, 6)
tupla1 = tupla1 + tupla2
(1, 2, 3, 4, 5, 6)

#5
Verificar se tal elemento está na tupla( True or False).
tupla = (1,2,3)
print(9 in tupla)
False

#6
Iterando (fazendo repetições) com um tupla.
tupla = (1,2,3)
for n in tupla:
    print(n)
    1
    2
    3
tupla = (1,2,3)
for indice, valor in enumerate(tupla):
    print(indice, valor)


#7
# Contando elementos dentro de uma tupla.
tupla = ('a','b','c','d','e','a','b')
print(tupla.count('e'))
1
print(tupla.count('a'))
2
escola = tuple('Geek University')
print(escola)
('G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y')
print(escola.count('e'))
3

#8
Dicas para a utilização de tuplas
#utilizamos tuplas sempre que não precisarmos modificar uma coleção de elementos.Exemplo:
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
print(meses[5])
junho

#9
O acesso a elementos de uma tupla é semelhante ao de uma lista.
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
print(meses)
('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
print(meses[5])
junho

#10
#itinerar(fazer repetição) com o comando 'while'.
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1
janeiro
fevereiro
março
abril
maio
junho
julho
agosto
setembro
outubro
novembro
dezembro

#11
#verificar na tupla em qual índice um elemento está.
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
print(meses.index('junho'))
5
print(meses.index('julho'))
6

#12
# Slicing wiht tuplas
tupla (inicio:fim:passo)
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
print(meses[::])
('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

#13
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
print(meses[::])
('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

#13.1
print(meses[5:])
('junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

#13.2
print(meses[5:9])
('junho', 'julho', 'agosto', 'setembro')
print(meses[:3])
('janeiro', 'fevereiro', 'março')

#14 Pq utilizar tuplas ao invés de listas ?
1 - Tuplas são mais rápidas do que listas.
2- Tuplas dão segurança estrutural ao código.

#15 Copiando uma tupla para a outra.
tupla = (1,2,3)
print(tupla)

nova = tupla
print(nova)
print(tupla)

outra = (4,5,6)
nova = nova + outra
print(outra)
print(nova)
(1, 2, 3)
(1, 2, 3)
(1, 2, 3)
(4, 5, 6)
(1, 2, 3, 4, 5, 6)

#15
tupla = 4, é uma tupla
tupla = (4,) é uma tupla
tupla = (4) # apesar do parênteses não é tupla, já que elas são caracterizadas pelas vírgulas. É número inteiro.
VS.
lista = [4] # é uma lista
lista = [4,] # é uma lista
lista = 1, # aqui temos classificação tupla e não lista.

"""
















