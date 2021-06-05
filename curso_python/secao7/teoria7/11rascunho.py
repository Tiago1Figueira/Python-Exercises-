# LISTAS

#1
lista1 = [ 1,2,3,44,67,999,0]
print(lista1.count(1))
1

#2
lista5 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
print(lista5.count('e'))
3

#3
lista1 = [ 1,2,3,44,67,999,0]
print(lista1)
lista1.append(42)# um elemento!
print(lista1)
[0, 1, 2, 3, 44, 67, 999]
[0, 1, 2, 3, 44, 67, 999, 42]

#3.1
lista = []
lista.append(42)
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
print(lista)
[42, 42, 42, 33, 33]

#4
lista1 = [ 1,2,3,44,67,999,0]
print(lista1)
lista1.append(42)# um elemento!
print(lista1)
[0, 1, 2, 3, 44, 67, 999]
[0, 1, 2, 3, 44, 67, 999, 42]

#5
[0, 1, 2, 3, 44, 67, 999]
#lista1.append([2,3,5])
print(lista1)
[0, 1, 2, 3, 44, 67, 999, 42, [2, 3, 5]]

#6
lista1 = [ 1,2,3,44,67,999,0]
lista1.extend([122, 34, 56])
print(lista1)
[0, 1, 2, 3, 44, 67, 999, 42, [2, 3, 5], 122, 34, 56]

#7
lista1 = [ 1,2,3,44,67,999,0]
lista1.extend(['Geek'])
print(lista1)
[0, 1, 2, 3, 44, 67, 999, 42, [2, 3, 5], 122, 34, 56, 'Geek']

#8
lista1.extend('geek')
print(lista1)
[0, 1, 2, 3, 44, 67, 999, 42, [2, 3, 5], 122, 34, 56, 'Geek', 'g', 'e', 'e', 'k']

#9
lista1 = [ 1,2,3,44,67,999,0]
lista1.insert(2, 'novo valor')
print(lista1)
[0, 1, 'novo valor', 2, 3, 44, 67, 999, 42, [2, 3, 5], 122, 34, 56, 'Geek', 'g', 'e', 'e', 'k']

#10
vetor = [1,-1,2,3]
for i in vetor:
    if i < 0:
        vetor.insert(vetor.index(i), '0')
        vetor.pop(vetor.index(i))
print(vetor)
[1,0,2,3]

#11
lista1 = [ 1,2,3,44,67,999,0]
lista2 = ['g','U', 'J', 'M', 'y', 'I']
lista6 = lista1 + lista2
print(lista6)
[1, 2, 3, 44, 67, 999, 0, 'g', 'U', 'J', 'M', 'y', 'I']

#12
lista1 = [ 1,2,3,44,67,999,0]
lista2 = ['g','U', 'J', 'M', 'y', 'I']
lista1.extend(lista2)
print(lista1)
[1, 2, 3, 44, 67, 999, 0, 'g', 'U', 'J', 'M', 'y', 'I']

#13
lista1 = [ 1,2,3,44,67,999,0]
lista2 = ['g','U', 'J', 'M', 'y', 'I']
lista1.extend(lista2)
print(lista1)
[1, 2, 3, 44, 67, 999, 0, 'g', 'U', 'J', 'M', 'y', 'I']

#14
lista1 = [ 1,2,3,44,67,999,0]
lista2 = ['g','U', 'J', 'M', 'y', 'I']
print(lista1)
print(lista2)
print('='*70)
print(lista1[::-1])
print(lista2[::-1])
[1, 2, 3, 44, 67, 999, 0]
['g', 'U', 'J', 'M', 'y', 'I']
#======================================================================
[0, 999, 67, 44, 3, 2, 1]
['I', 'y', 'M', 'J', 'U', 'g']

#15
lista1 = [ 1,2,3,44,67,999,0]
lista2 = ['g','U', 'J', 'M', 'y', 'I']
print(len(lista1))
7
print(len(lista2))
6

#16
lista2 = ['g','U', 'J', 'M', 'y', 'I']
lista6 = lista2.copy()
print(lista6)
['g', 'U', 'J', 'M', 'y', 'I']

#17
lista1 = [ 1,2,3,44,67,999,0]
print(lista1)
lista1.pop()
print(lista1)
[1, 2, 3, 44, 67, 999, 0]
[1, 2, 3, 44, 67, 999]

#18
lista1 = [ 1,2,3,44,67,999,0]
print(lista1)
lista1.pop(2)
print(lista1)
[1, 2, 3, 44, 67, 999]
[1, 2, 44, 67, 999]

#19
# trabalhar com pop
vetor = [1,-1,2,3]
for i in vetor:
    if i < 0:
        vetor.insert(vetor.index(i), '0')
        vetor.pop(vetor.index(i))
print(vetor)
[1,0,2,3]

#20
lista1 = [ 1,2,3,44,67,999,0]
lista1
lista1.clear()
print(lista1)
[]

#21
lista_nova = (1,2,3)
print(lista_nova)
lista_nova = lista_nova * 3
print(lista_nova)
(1, 2, 3)
(1, 2, 3, 1, 2, 3, 1, 2, 3)

#22
curso = 'Programação em Python essencial!'
print(curso)
curso = curso.split()
print(curso)
# Programação em Python essencial!
['Programação', 'em', 'Python', 'essencial!']

#23
curso = 'Programação,em,python,essencial'
print(curso)
curso = curso.split(',')
print(curso)
#Programação,em,python,essencial
['Programação', 'em', 'python', 'essencial']

#24
curso = ' '.join(curso)
print(curso)
['Programação', 'em', 'python', 'essencial']
#Programação em python essencial

#25
lista5 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista6 = '-'.join(lista5)
print(lista6)
#G-e-e-k- -U-n-i-v-e-r-s-i-t-y

#26
lista2 = ['g','U', 'J', 'M', 'y', 'I']
for elemento in lista2:
    print(elemento)
#    g
#    U
#    J
#    M
#    y
#    I

#27
# Utilizando o 'for' imprimir os elementos da lista solicitada
soma = 0
lista1 = [ 1,2,3,44,67,999,0]
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

#28
soma = ' '
lista2 = ['g','U', 'J', 'M', 'y', 'I']
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print(soma)
#g
#U
#J
#M
#y
#I
# gUJMyI

#29
#           0       1         2          3
cores = ['azul', 'amarelo', 'verde', 'branco']
print(cores[0])#azul
print(cores[1])#amarelo
print(cores[2])#verde
print(cores[3])#branco

#30
#          -4      -3        -2        -1
cores = ['azul', 'amarelo', 'verde', 'branco']
print(cores[-1])#branco
print(cores[-2])#verde
print(cores[-3])#amarelo
print(cores[-4])#azul

#31
#            0       1         2          3
cores = ['azul', 'amarelo', 'verde', 'branco']
for cor in cores:
    print(cor)
#azul
#amarelo
#verde
#branco

#32
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1
#azul
#amarelo
#verde
#branco

#33
#          0       1         2          3
cores = ['azul', 'amarelo', 'verde', 'branco']
for indice, cor in enumerate(cores):
    print(indice, cor)
#    0 azul
#    1 amarelo
#    2 verde
#    3 branco

#34
cores = ['azul', 'amarelo', 'verde', 'branco']
cores = list(enumerate(cores))
print(cores)
[(0, 'azul'), (1, 'amarelo'), (2, 'verde'), (3, 'branco')]

#35
lista = [ 22,3,2,9,0,6]
for indice, i in enumerate(lista):
    print(indice, i)
#0 22
#1 3
#2 2
#3 9
#4 0
#5 6

#36
numeros = [3,4,5,6,7,8,10,5]
print(numeros.index(6)) # em qual índice da lista está o elemento 6?
print(numeros.index(10)) # em qual índice da lista está o elemento 10?
print(numeros.index(5))# caso haja dois números repetidos o primeiro índice dos dois ou mais será o que aparecerá.
print(numeros.index(5,3))# busca o próximo índice do número 5 a partir do índice 3(3 que é primeiro elemento 5).
print(numeros.index(8,0,7))# busca o número 8 entre os índices 0 e 7.
1
6
2
7
5

#37
# trabalhar com index
vetor = [1,-1,2,3]
for i in vetor:
    if i < 0:
        vetor.insert(vetor.index(i), '0')
        vetor.pop(vetor.index(i))
print(vetor)
[1,0,2,3]

#38
#index
print(lista.index(30)) #imprimi o elemento na posição 30 da lista.

#39
#Trabalhando com slice de 'lista' no parâmetro início.
lista = [1,2,3,4]
print(lista[1:]) # iniciando no índice 1 e indo até o último elemento.
print(lista[::]) # imprimi todos os elementos da lista.
print(lista[1]) # imprimi o elemento localizado no índice 1, ou seja, 2.
print(lista[0]) # imprimi o elemento localizado no índice 0, ou seja, 1.
print(lista[-1:]) # imprimi o elemento localizado no índice -1, ou seja, 4
print(lista[-3:]) # imprimi os elementos localizados de -1 a -3.[ 2,3,4]
print(lista[-4:])
[2, 3, 4]
[1, 2, 3, 4]
2
1
[4]
[2, 3, 4]
[1, 2, 3, 4]

#40
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista[:2])# aqui o print começa no 0 (:) e vai até o segundo índice(2-1).
print(lista[:4])# aqui o print começa no 0 (e vai até o 4th índice(4-1).
print(lista[:6])# aqui o print começa no 0 e vai até o 6th índice.(6-1)
print((lista[1:3]))#
[1, 2]
[1, 2, 3, 4]
[1, 2, 3, 4, 5, 6]
[2, 3]

#41
curso = 'programacao em python essencial'
print(curso[::-1])
#laicnesse nohtyp me oacamargorp

#42
nomes = ['geek', 'university']
nomes.reverse()
print(nomes)
['university', 'geek']

#43
lista = [1,2,3,4,5,6]
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))
21
6
1
6

#44
#deep copy = não afetou a primeira lista.
lista = [1,2,3,4]
print(lista)
[1, 2, 3, 4]

nova = lista.copy()
print(nova)
nova.append(4)
print(lista)
print(nova)
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4, 4]

#45
lista = [1,2,3]
print(lista)

nova = lista # aqui diz que uma lista afeta a outra ou shallow copy!
print(nova)
nova.append(4)
print(lista)
print(nova)
[1, 2, 3]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4]

#  TUPLAS
#Resumindo: são imutáveis. Não alteram o seu valor.
#(4) não é tupla.
#(4,) é tupla.
#4, é tupla.

#1
tupla1 = (1,2,3,4,5,6)# com parênteses
print(tupla1)
print(type(tupla1))
(1, 2, 3, 4, 5, 6)
#<class 'tuple'>

#2
tupla2 = 1,2,3,4,5,6 # sem parênteses
print(tupla2)
print(type(tupla2))
(1, 2, 3, 4, 5, 6)
#<class 'tuple'>

#3
tupla = ('Geek University', 'Python Essencial')
escola, curso = tupla
print(escola)
print(curso)
# Geek University
# Python Essencial

#4
tupla = (1,2,3,4,5,6)
print(max(tupla))
6
print(min(tupla))
1
print(len(tupla))
6
print(sum(tupla))
21

#5
tupla1 = (1,2,3)
print(tupla1)
(1,2,3)
tupla2 = (4,5,6)
print(tupla2)
(4,5,6)
print(tupla1 + tupla2)
(1,2,3,4,5,6)

#6
tupla1 = (1,2,3)
tupla2 = (4,5,6)
tupla3 = tupla1 + tupla2
print(tupla1)
(1,2,3)
print(tupla2)
(4,5,6)
print(tupla3)
(1,2,3,4,5,6)

#7
tupla = (1,2,3)
for n in tupla:
    print(n)
    1
    2
    3

#8
tupla = (1,2,3)
for indice, valor in enumerate(tupla):
    print(indice, valor)
#0 1
#1 2
#2 3

#9
tupla1 = (1,2,3)
print(tupla1)
(1,2,3)
tupla2 = (4,5,6)
print(tupla2)
(4,5,6)
print(tupla1 + tupla2)
(1,2,3,4,5,6)

#10
tupla1 = (1,2,3)
tupla2 = (4,5,6)
tupla3 = tupla1 + tupla2
print(tupla1)
(1,2,3)
print(tupla2)
(4,5,6)
print(tupla3)
(1,2,3,4,5,6)

#11
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

#12
tupla = (1,2,3)
for n in tupla:
    print(n)
    1
    2
    3

#13
tupla = (1,2,3)
for indice, valor in enumerate(tupla):
    print(indice, valor)
# 0 1
# 1 2
# 2 3

#14
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

#15
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
print(meses[5])
#junho

#16
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1
#janeiro
#fevereiro
#março
#abril
#maio
#junho
#julho
#agosto
#setembro
#outubro
#novembro
#dezembro

#17
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
print(meses.index('junho'))
5
print(meses.index('julho'))
6

#18
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
print(meses[::])
('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

#19
#19.1
print(meses[5:])
('junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

#19.2
print(meses[5:9])
('junho', 'julho', 'agosto', 'setembro')

print(meses[:3])
('janeiro', 'fevereiro', 'março')

#20
tupla = (1,2,3)
print(tupla)
(1, 2, 3)

nova = tupla
print(nova)
print(tupla)
(1, 2, 3)
(1, 2, 3)

outra = (4,5,6)
nova = nova + outra
print(outra)
print(nova)
(4, 5, 6)
(1, 2, 3, 4, 5, 6)


# DICIONÁRIOS
#Chaves {} e valores são separados por ':'.


#1
paises = {'br':'Brasil','usa':'Estados Unidos', 'py':'Paraguai'}
print(paises)
print(type(paises))
{'br': 'Brasil', 'usa': 'Estados Unidos', 'py': 'Paraguai'}
#<class 'dict'>

#2
#Acesse elementos
paises = {'br':'Brasil','usa':'Estados Unidos', 'py':'Paraguai'}
print(paises['br'])
print(paises['py'])
#Brasil
#Paraguai

#2.1
#mais comum
paises = {'br':'Brasil','usa':'Estados Unidos', 'py':'Paraguai'}
print(paises.get('br'))
print(paises.get('py'))
#Brasil
#Paraguai

#3
paises = {'br':'Brasil','usa':'Estados Unidos', 'py':'Paraguai'}
pais = paises.get('py')
if pais:
    print('Encontrei o país.')
else:
    print('Não encontrei o país.')
# Encontrei o país.

#4
paises = {'br':'Brasil','usa':'Estados Unidos', 'py':'Paraguai'}
print('br' in paises)
True
print('ru' in paises)
False
print('Estados Unidos' in paises)
False

#5
#tupla são boas para serem usadas como chaves.
localidades = {
    (3544, 5656): ' Escritório em Japão:',
    (4244, 9056): ' Escritório em NYC:',
    (4444, 2356): ' Escritório em São Paulo:',
}
print(localidades)
print(type(localidades))
{(3544, 5656): ' Escritório em Japão:', (4244, 9056): ' Escritório em NYC:', (4444, 2356): ' Escritório em São Paulo:'}
#<class 'dict'>

#6
#adicionar elementos
receita = {'jan':'245', 'fev':'345', 'mar': '123'}
print(receita)
print(type(receita))
{'jan': '245', 'fev': '345', 'mar': '123'}
#<class 'dict'>

#7
# forma1 (mais comum)
receita = {'jan':'245', 'fev':'345', 'mar': '123'}
receita['abr'] = 3789
print(receita)
{'jan': '245', 'fev': '345', 'mar': '123', 'abr': 3789}

#forma 2
receita = {'jan':'245', 'fev':'345', 'mar': '123'}
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)
{'jan': '245', 'fev': '345', 'mar': '123', 'abr': 3789}
{'jan': '245', 'fev': '345', 'mar': '123', 'abr': 3789, 'mai': 500}

#8
receita = {'jan':'245', 'fev':'345', 'mar': '123'}
print(receita)

#forma 1 (mais comum)
receita['mai'] = 550
print(receita)
{'jan': '245', 'fev': '345', 'mar': '123', 'abr': 3789, 'mai': 500}

#forma 2
receita.update({'mai': 600})
print(receita)
{'jan': '245', 'fev': '345', 'mar': '123', 'abr': 3789, 'mai': 500}


#9
#atualizar ou adicionar elementos
receita = {'jan':'245', 'fev':'345', 'mar': '123'}
print(receita)

#forma 1 (mais comum)
receita['mai'] = 550
print(receita)
{'jan': '245', 'fev': '345', 'mar': '123', 'abr': 3789, 'mai': 500}

#forma 2
receita.update({'mai': 600})
print(receita)
{'jan': '245', 'fev': '345', 'mar': '123', 'abr': 3789, 'mai': 500}

#10
#forma 1 ( É a mais comum!)
#Informa-se a chave e não o valor. Ao se remover uma chave o seu valor é sempre retornado.

receita = {'jan':'245', 'fev':'345', 'mar': '123'}
print(receita)
ret = receita.pop('mar')
print(ret)
print(receita)
#{'jan': '245', 'fev': '345', 'mar': '123'}
#123
#{'jan': '245', 'fev': '345'}

#forma 2
#neste caso o valor removido nao e retornado.
receita = {'jan': '245', 'fev': '345'}
del receita['fev']
print(receita)
{'jan': '245'}


#11 exemplo de adiçao de elementos(aqui produtos)
carrinho = []
produto1 = {'nome':'playstation 4','quantidade':'1','valor':'2300'}
produto2 = {'nome':'god of war 4','quantidade':'1','valor':'150'}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
[{'nome': 'playstation 4', 'quantidade': '1', 'valor': '2300'}, {'nome': 'god of war 4', 'quantidade': '1', 'valor': '150'}]

#12
# limpar o dicionário.(zerar o dicionário)
#d.clear()
#print(d)

d= dict(a=1,b=2,c=3)
print(d)
print(type(d))
{'a': 1, 'b': 2, 'c': 3}
#<class 'dict'>

#13
#copiando um dicionário para outro

#Forma 1(deep copy)
d= dict(a=1,b=2,c=3)
novo = d.copy()
novo['d']=4
print(d)
print(novo)
{'a': 1, 'b': 2, 'c': 3}
{'a': 1, 'b': 2, 'c': 3, 'd': 4}

#14
# forma 2 (shallow copy) (Há alteração no dicionário original)
d= dict(a=1,b=2,c=3)
print(d)
print(type(d))
{'a': 1, 'b': 2, 'c': 3}
#<class 'dict'>

novo = d
novo['d'] = 4
print(d)
print(novo)
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
{'a': 1, 'b': 2, 'c': 3, 'd': 4}

#15
#forma não usual de criação de dicionário
outro = {}.fromkeys('a','b')
print(outro)
print(type(outro))
{'a': 'b'}
#<class 'dict'>

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))
{'nome': 'desconhecido', 'pontos': 'desconhecido', 'email': 'desconhecido', 'profile': 'desconhecido'}
#<class 'dict'>

#16
veja = {}.fromkeys('teste','valor')
print(veja)
print(type(veja))
{'t': 'valor', 'e': 'valor', 's': 'valor'}# um valor por letra. só não ha repetição de chaves como nas letras 't' e 'e'.
#<class 'dict'>

veja = {}.fromkeys(range(1,11),'novo')
print(veja)
{1: 'novo', 2: 'novo', 3: 'novo', 4: 'novo', 5: 'novo', 6: 'novo', 7: 'novo', 8: 'novo', 9: 'novo', 10: 'novo'}

# MAPAS
#1
receita = {'jan':'100', 'fev':'250', 'mar':'400'}
print(receita)
{'jan': '100', 'fev': '250', 'mar': '400'}

#2
#imprimindo chaves
receita = {'jan':'100', 'fev':'250', 'mar':'400'}
for chave in receita:
    print(chave)
#jan
#fev
#mar

#3
#imprimindo valores
receita = {'jan':'100', 'fev':'250', 'mar':'400'}
for chave in receita:
    print(receita[chave])
100
250
400

#4
#acessando os valores
receita = {'jan':'100', 'fev':'250', 'mar':'400'}
for chave in receita:
    print(f'Recebi em {chave} valor de R$ {receita[chave]}!')
#Recebi em jan valor de R$ 100!
#Recebi em fev valor de R$ 250!
#Recebi em mar valor de R$ 400!
# usa-se {receita[chave]} para se obter os valores referentes as chaves. As chaves são usadas aqui para se obter os valores

#5
#acessando os valores
receita = {'jan':'100', 'fev':'250', 'mar':'400'}
print(receita.keys())
for chave in receita.keys():
    print(receita[chave])
#dict_keys(['jan', 'fev', 'mar'])
100
250
400

#6
#acessando valores
receita = {'jan':'100', 'fev':'250', 'mar':'400'}
print(receita)
{'jan':'100', 'fev':'250', 'mar':'400'}

#7
receita = {'jan':'100', 'fev':'250', 'mar':'400'}
print(receita.values())
for valor in receita.values():
    print(valor)
#dict_values(['100', '250', '400'])
#100
#250
#400

#8
#desempacotando valores
receita = {'jan':'100', 'fev':'250', 'mar':'400'}
print(receita)
print(receita.items())

#{'jan': '100', 'fev': '250', 'mar': '400'}
#dict_items([('jan', '100'), ('fev', '250'), ('mar', '400')])

#9
#desempacotando valores
for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

#chave = jan e valor = 100
#chave = fev e valor = 250
#chave = mar e valor = 400

#10
#Dicionários : soma, valor_maximo, valor_minimo, tamanho
receita = {'jan':100, 'fev':250, 'mar':400}
print(receita)
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
print(sum(receita.values()))
{'jan': 100, 'fev': 250, 'mar': 400}
400
100
3
750


# CONJUNTOS OU SETS


# 1
#forma 1
#números repetidos são ignorados e não geram erro! (conjuntos: valores - chaves:chaves e valores)
s = set({1,2,3,4,5,5,7,6,2,2,3})
print(s)
print(type(s))
{1, 2, 3, 4, 5, 6, 7}
#<class 'set'>

#2
# forma 2 (mais comum)
s = {1,2,3,4,5,5}
print(s)
print(type(s))
{1, 2, 3, 4, 5}
#<class 'set'>

#3
s = {1,2,3,4,5,5}
if 3 in s:
    print('O número faz parte do conjunto.')
else:
    print('O número não faz parte do conjunto.')
# O número faz parte do conjunto.

#4
lista = [99,2,56,4,23,67,87,9,2,56]
print(f'Lista {lista} com {len(lista)} elementos')
print(type(lista))
#Lista [99, 2, 56, 4, 23, 67, 87, 9, 2, 56] com 10 elementos
#<class 'list'>

#5
#conjuntos não aceitam valores duplicados, logo 8 elementos.( mexe na ordem numérica original reordenando os números de maneira própria.
conjunto = {99,2,56,4,23,67,87,9,2,56} #conjuntos não aceitam valores duplicados, logo 2 e 56 não se repetem.
print(f'Conjunto {conjunto} com {len(conjunto)} elementos')
print(type(conjunto))
#Conjunto {2, 99, 4, 67, 9, 87, 23, 56} com 8 elementos
#<class 'set'>

#6
#sets/conjuntos não aceitam valores duplicados, logo 2 e 56 não se repetem.Números se movem.
conjunto = {99,2,56,4,23,67,87,9,2,56}
print(f'Conjunto {conjunto} com {len(conjunto)} elementos')
print(type(conjunto))
#Conjunto {2, 99, 4, 67, 9, 87, 23, 56} com 8 elementos
#<class 'set'>

#7
s = (1,'b',True, 3.22, 44)
for valor in s:
    print(valor)
1
#b
True
3.22
44

#8
cidades = ['Belo Horizonte', 'Sao Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'Sao Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))
['Belo Horizonte', 'Sao Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'Sao Paulo', 'Cuiaba']
7

#9
#agora precisamos saber qtas cidades distintas, únicas, nós temos:
#usa-se o 'set' já que esta coleção não repete itens e assim somente aparecerá as cidades necessárias.

cidades = ['Belo Horizonte', 'Sao Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'Sao Paulo', 'Cuiaba']
print(set(cidades))
print(len(set(cidades)))
{'Cuiaba', 'Belo Horizonte', 'Campo Grande', 'Sao Paulo'}
4

#10
#adicionando elementos em um conjunto.
#conjuntos são mutáveis, diferentemente das tuplas, pois podemos modificar o dicionário.
s = {1,2,3}
s.add(4)
{1, 2, 3, 4}
#duplicidade de elementos no dicionário não gera erro ou duplica os número. É ignorado.
s.add(4)
print(s)
{1, 2, 3, 4}

#11
#remover elementos em um conjunto.
s = {1,2,3}
print(s)
{1,2,3}
# 3 não é índice, mas sim o número a ser removido.
s.remove(3)
print(s)
{1,2}

#12
s.discard(2)
print(s)
{1}

#13
#copiando um conjunto para o outro.
#forma 1 (deep copy)
s= {1,2,3}
print(s)
{1,2,3}
novo = s.copy()
print(novo)
{1, 2, 3}

#14
novo.add(4)
print(novo)
print(s)
{1, 2, 3, 4}
{1, 2, 3}

#15
#forma 2(shallow copy) aqui uma modificação nos elementos 'novo' modifica o dicionário copiado 's'.
s= {1,2,3}
print(s)
{1, 2, 3}

novo = s
novo.add(4)
print(novo)
{1, 2, 3, 4}

#16
#podemos remover todos os elementos de um conjunto.
s = {1,2,3}
print(s)
s.clear()
print(s)
{1, 2, 3}
set()


#17
#Utilizando a union elementos duplicados não aparecem no print.

#Forma 1
estudantes_python = {'Marcos', 'Patrícia','Ellen', 'Pedro', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patrícia'}
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)
#{'Gustavo', 'Guilherme', 'Ellen', 'Ana', 'Júlia', 'Fernando', 'Pedro', 'Marcos', 'Patrícia'}

#18
estudantes_python = {'Marcos', 'Patrícia','Ellen', 'Pedro', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patrícia'}
unicos2 = estudantes_java.union(estudantes_python)
print(unicos2)
#{'Ellen', 'Gustavo', 'Júlia', 'Pedro', 'Marcos', 'Guilherme', 'Fernando', 'Patrícia', 'Ana'}

#19
#Forma 2 (utilizando o pipe) #(elementos duplicados não aparecem no print.)
unicos3 = estudantes_python | estudantes_java
print(unicos3)
#{'Ana', 'Pedro', 'Ellen', 'Patrícia', 'Júlia', 'Marcos', 'Fernando', 'Gustavo', 'Guilherme'}

#20
#gerar um conjunto de estudantes que estão em ambos os cursos.

#20.1
#Forma 1
#(Utilizando intersection)
estudantes_python = {'Marcos', 'Patrícia','Ellen', 'Pedro', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patrícia'}
ambos1 = estudantes_java.intersection(estudantes_python)
print(ambos1)
#{'Júlia', 'Patrícia'}

#20.2
#Forma 2
#(Intersection Utilizando o &)
estudantes_python = {'Marcos', 'Patrícia','Ellen', 'Pedro', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patrícia'}
ambos2 = estudantes_java & estudantes_python
print(ambos2)
#{'Patrícia', 'Júlia'}

#21
#gerar um conjunto de estudantes que não estão no outro.(oposto do intersection)

estudantes_python = {'Marcos', 'Patrícia','Ellen', 'Pedro', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patrícia'}
so_python = estudantes_python.difference(estudantes_java)
print(so_python)
#{'Marcos', 'Pedro', 'Ellen', 'Guilherme'} Estudantes que estão no python, mas não no java.

#21.1
estudantes_python = {'Marcos', 'Patrícia','Ellen', 'Pedro', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patrícia'}
so_java = estudantes_java.difference(estudantes_python)
print(so_java)
#{'Fernando', 'Gustavo', 'Ana'} Estudantes que estão no java, mas não no python.


#22
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

#COLLECTIONS COUNTER

#1
#realizando o import
from collections import Counter
lista = [1,1,1,1,2,2,2,3,3,3,1,1,2,4,4,4,5,5,5,5,6,35,45,32] #podemos utilizar qqer iterável. Aqui, utilizamos um 'lista'.
res = Counter(lista) #utilizamos o counter aqui.
print(res)
print(type(res))
#Counter({1: 6, 2: 4, 5: 4, 3: 3, 4: 3, 6: 1, 35: 1, 45: 1, 32: 1})
#<class 'collections.Counter'>

#2
from collections import Counter
print(Counter('Geek University'))
#Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

#3
# texto =    recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um
#dicionário, contendo como chaves os elementos da 'lista' dada como parâmetro e como valor a quantidade de elementos
#que esse valor aparece."""

#palavras = texto.split()
#print(palavras)
['recebe', 'um', 'iterável', 'como', 'parâmetro', 'e', 'cria', 'um', 'objeto', 'do',
 'tipo', 'Collections', 'Counter', 'que', 'é', 'parecido', 'com', 'um', 'dicionário,',
 'contendo', 'como', 'chaves', 'os', 'elementos', 'da', "'lista'", 'dada', 'como',
 'parâmetro', 'e', 'como', 'valor', 'a', 'quantidade', 'de',
 'elementos', 'que', 'esse', 'valor', 'aparece.']

#3.1
# o comando ' counter ' coloca números nos elementos
# Aqui há uma reunião dos 2 comandos.
#from collections import Counter

#res = Counter(palavras)
#print(res)
#Counter({'como': 4, 'um': 3, 'parâmetro': 2, 'e': 2, 'que': 2, 'elementos': 2,
 #        'valor': 2, 'recebe': 1, 'iterável': 1, 'cria': 1, 'objeto': 1, 'do':
  #           1, 'tipo': 1, 'Collections': 1, 'Counter': 1, 'é': 1, 'parecido':
   #          1, 'com': 1, 'dicionário,': 1, 'contendo': 1, 'chaves': 1, 'os':
    #         1, 'da': 1, "'lista'": 1, 'dada': 1, 'a': 1, 'quantidade': 1, 'de':
     #        1, 'esse': 1, 'aparece.': 1})

#3.2
#Encontrando as 5 palavras que mais aparecem no texto.
#print(res.most_common(6))
#[('como', 4), ('um', 3), ('Collections', 2), ('-', 2), ('parâmetro', 2), ('e', 2)]

#4
#realizando o import
from collections import Counter
lista = [1,1,1,1,2,2,2,3,3,3,1,1,2,4,4,4,5,5,5,5,6,35,45, 45,32]#podemos utilizar qqer iterável. Aqui, utilizamos um 'lista'.
res = Counter(lista) #utilizamos o counter aqui.
print(type(res)) #<class 'collections.Counter'>
print(res)
#Counter({1: 6, 2: 4, 5: 4, 3: 3, 4: 3, 6: 1, 35: 1, 45: 1, 32: 1})

#4.1
from collections import Counter#1
lista1 = ['a','b','c','d',1,1,'1e','e',1,45,45,'tago']
res = Counter(lista1)#2
print(res)#3
print(type(res))#4
Counter({1: 3, 45: 2, 'a': 1, 'b': 1, 'c': 1, 'd': 1, '1e': 1, 'e': 1, 'tago': 1})
#<class 'collections.Counter'>

#4.2
from collections import Counter#1
lista2 = ['geek' 'university']
ret = Counter(lista2)#2
print(ret)#3
Counter({'geekuniversity': 1})

#4.3
from collections import Counter
lista3 = [1,2,3,3,3,3,3,3,4,5,5,5,6,6,6,9,11,111,23,24,56,66,78,100]
ret = Counter(lista3)
print(ret)
Counter({3: 6, 5: 3, 6: 3, 1: 1, 2: 1, 4: 1, 9: 1, 11: 1, 111: 1, 23: 1, 24: 1, 56: 1, 66: 1, 78: 1, 100: 1})

#4.4
from collections import Counter
print(Counter('Geek University'))
#Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})
#aqui as letras são contadas reparadamente.

#4.4.1
from collections import Counter
lista4 = ['Geek University']
res = Counter(lista4)
print(res)
#Counter({'Geek University': 1})
#aqui, dentro de uma lista, a frase é contada como se fosse uma e não um conjunto de letras.

#5
#o comando 'split' separa todas as palavras que estão no texto.
# o comando ' counter ' coloca números nos elementos
# Aqui há uma reunião dos 2 comandos.

from collections import Counter
#texto = """  recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um
#dicionário, contendo como chaves os elementos da 'lista' dada como parâmetro e como valor a quantidade de elementos
#que esse valor aparece."""

#palavras = texto.split()
#print(palavras)

#res = Counter(palavras)
print(res)

print(res.most_common(6))

['recebe', 'um', 'iterável', 'como', 'parâmetro', 'e', 'cria', 'um', 'objeto', 'do',
 'tipo', 'Collections', 'Counter', 'que', 'é', 'parecido', 'com', 'um', 'dicionário,',
 'contendo', 'como', 'chaves', 'os', 'elementos', 'da', "'lista'", 'dada', 'como',
 'parâmetro', 'e', 'como', 'valor', 'a', 'quantidade', 'de',
 'elementos', 'que', 'esse', 'valor', 'aparece.']

Counter({'como': 4, 'um': 3, 'parâmetro': 2, 'e': 2, 'que': 2, 'elementos': 2,
         'valor': 2, 'recebe': 1, 'iterável': 1, 'cria': 1, 'objeto': 1, 'do':
             1, 'tipo': 1, 'Collections': 1, 'Counter': 1, 'é': 1, 'parecido':
             1, 'com': 1, 'dicionário,': 1, 'contendo': 1, 'chaves': 1, 'os':
             1, 'da': 1, "'lista'": 1, 'dada': 1, 'a': 1, 'quantidade': 1, 'de':
             1, 'esse': 1, 'aparece.': 1})

[('como', 4), ('um', 3), ('Collections', 2), ('-', 2), ('parâmetro', 2), ('e', 2)]




#COLLECTIONS DEFAULT DICT

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

#COLLECTIONS ORDERED DICT

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }
for chave, valor in dicionario.items():
    print(f'chave = {chave} e valor = {valor}')

#chave = a e valor = 1
#chave = b e valor = 2
#chave = c e valor = 3
#chave = d e valor = 4
#chave = e e valor = 5

#2
# orderedDict é um comando que nos garante a ordem de inserção dos elementos no dicionario.
#fazendo o import
from collections import OrderedDict
dicionario = OrderedDict ({'a': 1, 'b': 2, 'c':3, 'd':4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave = {chave} valor = {valor}')

#chave = a e valor = 1
#chave = b e valor = 2
#chave = c e valor = 3
#chave = d e valor = 4
#chave = e e valor = 5

#COLLECTIONS NAMED TUPLE

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

#COLLECTIONS DEQUE
#Deques servem para adicionar, remover elementos em uma lista, a esquerda ou a direita.

#1
# criando deques
#Importar
from collections import deque
deq = deque('Geek')
print(deq)
# deque(['G', 'e', 'e', 'k'])

#2
#adicionando elementos no deq a direita
deq.append('y')
print(deq)
#deque(['G', 'e', 'e', 'k'])
#deque(['G', 'e', 'e', 'k', 'y'])

#3
#adicionando elementos na lista deq a esquerda
deq.appendleft('k')
print(deq)
#deque(['G', 'e', 'e', 'k'])
#deque(['G', 'e', 'e', 'k', 'y'])
#deque(['k', 'G', 'e', 'e', 'k', 'y'])

#4
#Removendo elementos de uma lista
#remove e retorna o último elemento de uma lista.
print(deq.pop())
print(deq)
#deque(['k', 'G', 'e', 'e', 'k', 'y'])
#y
#deque(['k', 'G', 'e', 'e', 'k'])

#5
#remove e retorna o primeiro elemento de uma lista.
print(deq.popleft())
print(deq)
#deque(['k', 'G', 'e', 'e', 'k'])
#k
#deque(['G', 'e', 'e', 'k'])































































































































































































































