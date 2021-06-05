"""
- Conjuntos ou sets {}: estão relacionados aos conjuntos da matemática.
- Sets não passuem valores duplicados ou ordenados.
- Elementos não são acessados via indice, ou seja, conjuntos não são indexados.
- Conjuntos: utilizamos para armazenar elementos sem se importar com a organização. Qdo não nos preocupamos com chaves,
valores e itens duplicados.
- Diferença entre conjuntos ou sets e mapas (dicionários)
   - mapas : chaves e valores
   - conjuntos/sets: valores
#0
help(usando o terminal)
#>>> s = {1,2,3}
#>>> dir(s)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__',
  '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__',
   '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference',
    'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
     'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

#1
# Definindo o 'set'/ conjuntos:
# forma 1
#números repetidos são ignorados e não geram erro! (conjuntos: valores - chaves:chaves e valores)
s = set({1,2,3,4,5,5,7,6,2,2,3})
print(s)
print(type(s))
{1, 2, 3, 4, 5, 6, 7}
<class 'set'>

#2
# forma 2 (mais comum)
s = {1,2,3,4,5,5}
print(s)
print(type(s))
{1, 2, 3, 4, 5}
<class 'set'>

#3
#Além de não termos valores duplicados, não temos ordem.
#podemos verificar se determinado elemento está contido no conjunto usando o 'if in '.

s = {1,2,3,4,5,5}
if 3 in s:
    print('O número faz parte do conjunto.')
else:
    print('O número não faz parte do conjunto.')
# O número faz parte do conjunto.


#4
# "listas" aceitam valores duplicados, logo 10 elementos.(não mexe na ordem numérica original)
lista = [99,2,56,4,23,67,87,9,2,56]
print(f'Lista {lista} com {len(lista)} elementos')
print(type(lista))
Lista [99, 2, 56, 4, 23, 67, 87, 9, 2, 56] com 10 elementos
<class 'list'>

#4.1
#tuplas aceitam valores duplicados, logo 10 elementos. (não mexe na ordem numérica original)
tupla = (99,2,56,4,23,67,87,9,2,56)
print(f'Tupla {tupla} com {len(tupla)} elementos')
print(type(tupla))
Tupla (99, 2, 56, 4, 23, 67, 87, 9, 2, 56) com 10 elementos
<class 'tuple'>

#4.2
#dicionários não aceitam chaves duplicadas, logo 8 elementos.(não mexe na ordem numérica original)
dicionario = {}.fromkeys([99,2,56,4,23,67,87,9,2,56], 'dict') #dicionário não aceitam chaves duplicadas,
#logo 2 e 56 não se repetem.
print(f'Dicionário {dicionario} com {len(dicionario)} elementos')
print(type(dicionario))
Dicionário {99: 'dict', 2: 'dict', 56: 'dict', 4: 'dict', 23: 'dict', 67: 'dict', 87: 'dict', 9: 'dict'} com 8 elementos
<class 'dict'>

#4.3
#conjuntos não aceitam valores duplicados, logo 8 elementos.( mexe na ordem numérica original reordenando
os números de maneira própria.
conjunto = {99,2,56,4,23,67,87,9,2,56} #conjuntos não aceitam valores duplicados, logo 2 e 56 não se repetem.
print(f'Conjunto {conjunto} com {len(conjunto)} elementos')
print(type(conjunto))
Conjunto {2, 99, 4, 67, 9, 87, 23, 56} com 8 elementos
<class 'set'>

Resumindo ponto 4:
Resumo:
lista = [99,2,56,4,23,67,87,9,2,56] #números aparecem repetidos e na ordem em que estavam antes no print!
print(f'Lista {lista} com {len(lista)} elementos')
print(type(lista))
Lista [99, 2, 56, 4, 23, 67, 87, 9, 2, 56] com 10 elementos
<class 'list'>

#números aparecem repetidos e na ordem em que estavam.
tupla = (99,2,56,4,23,67,87,9,2,56)
print(f'Tupla {tupla} com {len(tupla)} elementos')
print(type(tupla))
Tupla (99, 2, 56, 4, 23, 67, 87, 9, 2, 56) com 10 elementos
<class 'tuple'>

#dicionário não aceitam chaves duplicadas,logo 2 e 56 não se repetem, ficam na ordem em que estavam antes.
dicionario = {}.fromkeys([99,2,56,4,23,67,87,9,2,56],'dict')
print(f'Dicionário {dicionario} com {len(dicionario)} elementos')
print(type(dicionario))
Dicionário {99: 'dict', 2: 'dict', 56: 'dict', 4: 'dict', 23: 'dict', 67: 'dict', 87: 'dict', 9: 'dict'} com 8 elementos
<class 'dict'>

#sets/conjuntos não aceitam valores duplicados, logo 2 e 56 não se repetem.Números se movem.
conjunto = {99,2,56,4,23,67,87,9,2,56}
print(f'Conjunto {conjunto} com {len(conjunto)} elementos')
print(type(conjunto))
Conjunto {2, 99, 4, 67, 9, 87, 23, 56} com 8 elementos
<class 'set'>

#5
#Assim como todo conjunto no Python podemos colocar tipos de dados misturados em sets.
s = (1,'b',True, 3.22, 44)
print(s)
(1, 'b', True, 3.22, 44)

#5.1
# podemos iterar normalmento com o 'sets'.
s = (1,'b',True, 3.22, 44)
for valor in s:
    print(valor)
1
b
True
3.22
44

#6
#usos interessantes com os sets(conjuntos)
# Exemplo: Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes informam
# as suas cidades manualmente. Adicionamos os nomes de cada cidade no python, já que em uma lista podemos adicionar
#novos elementos e ter repetição.

cidades = ['Belo Horizonte', 'Sao Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'Sao Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))
['Belo Horizonte', 'Sao Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'Sao Paulo', 'Cuiaba']
7

#6.1
#agora precisamos saber qtas cidades distintas, únicas, nós temos:
#usa-se o 'set' já que esta coleção não repete itens e assim somente aparecerá as cidades necessárias.

cidades = ['Belo Horizonte', 'Sao Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'Sao Paulo', 'Cuiaba']
print(set(cidades))
print(len(set(cidades)))
{'Cuiaba', 'Belo Horizonte', 'Campo Grande', 'Sao Paulo'}
4

#7
#adicionando elementos em um conjunto.
conjuntos são mutáveis, diferentemente das tuplas, pois podemos modificar o dicionário.
s = {1,2,3}
s.add(4)
{1, 2, 3, 4}
#duplicidade de elementos no dicionário não gera erro ou duplica os número. É ignorado.
s.add(4)
print(s)
{1, 2, 3, 4}

#8
#remover elementos em um conjunto.
s = {1,2,3}
print(s)
{1,2,3}
# 3 não é índice, mas sim o número a ser removido.
s.remove(3)
print(s)
{1,2}

#8.1
s.discard(2)
print(s)
{1}

#9
#copiando um conjunto para o outro.
#forma 1 (deep copy)
s= {1,2,3}
print(s)
{1,2,3}
novo = s.copy()
print(novo)
{1, 2, 3}

#9.1
novo.add(4)
print(novo)
print(s)
{1, 2, 3, 4}
{1, 2, 3}

#9.2
#forma 2(shallow copy) aqui uma modificação nos elementos 'novo' modifica o dicionário copiado 's'.
s= {1,2,3}
print(s)
{1, 2, 3}

novo = s
novo.add(4)
print(novo)
{1, 2, 3, 4}

#10
#podemos remover todos os elementos de um conjunto.
s = {1,2,3}
print(s)
s.clear()
print(s)
{1, 2, 3}
set()

#11
#métodos matemáticos de conjuntos

estudantes_python = {'Marcos', 'Patrícia','Ellen', 'Pedro', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patrícia'}

#11.1
#Forma 1
Utilizando a union elementos duplicados não aparecem no print.

estudantes_python = {'Marcos', 'Patrícia','Ellen', 'Pedro', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patrícia'}
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)
#{'Gustavo', 'Guilherme', 'Ellen', 'Ana', 'Júlia', 'Fernando', 'Pedro', 'Marcos', 'Patrícia'}

#(elementos duplicados não aparecem no print)
estudantes_python = {'Marcos', 'Patrícia','Ellen', 'Pedro', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patrícia'}
unicos2 = estudantes_java.union(estudantes_python)
print(unicos2)
#{'Ellen', 'Gustavo', 'Júlia', 'Pedro', 'Marcos', 'Guilherme', 'Fernando', 'Patrícia', 'Ana'}

#11.2
#Forma 2 (utilizando o pipe) #(elementos duplicados não aparecem no print.)

unicos3 = estudantes_python | estudantes_java
print(unicos3)
#{'Ana', 'Pedro', 'Ellen', 'Patrícia', 'Júlia', 'Marcos', 'Fernando', 'Gustavo', 'Guilherme'}

#12
#gerar um conjunto de estudantes que estão em ambos os cursos.

#12.1
#Forma 1
(Utilizando intersection)
estudantes_python = {'Marcos', 'Patrícia','Ellen', 'Pedro', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patrícia'}
ambos1 = estudantes_java.intersection(estudantes_python)
print(ambos1)
#{'Júlia', 'Patrícia'}

#12.2
#Forma 2
(Intersection Utilizando o &)
estudantes_python = {'Marcos', 'Patrícia','Ellen', 'Pedro', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patrícia'}
ambos2 = estudantes_java & estudantes_python
print(ambos2)
#{'Patrícia', 'Júlia'}

#13
#gerar um conjunto de estudantes que não estão no outro.(oposto do intersection)

estudantes_python = {'Marcos', 'Patrícia','Ellen', 'Pedro', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patrícia'}
so_python = estudantes_python.difference(estudantes_java)
print(so_python)
#{'Marcos', 'Pedro', 'Ellen', 'Guilherme'} Estudantes que estão no python, mas não no java.

#13.1
estudantes_python = {'Marcos', 'Patrícia','Ellen', 'Pedro', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patrícia'}
so_java = estudantes_java.difference(estudantes_python)
print(so_java)
#{'Fernando', 'Gustavo', 'Ana'} Estudantes que estão no java, mas não no python.

#14
#soma*, valor_max*, valor_min*, tamanho
s = {1,2,3,4,5,6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))
#21
#6
#1
#6

"""
