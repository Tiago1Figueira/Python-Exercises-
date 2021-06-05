"""
Listas( e.g.: lista = [] ou lista.append(num) )
Funcionam como vetores e matrizes, só que são DINÂMICAS e recebem QUALQUER dado.
- DINÂMICAS: não possuem valor fixo; podem colocar qquer quantia de dados. E.g.: listas.append(num) podem ser quantos
números puder colocar com entrada.
- QUALQUER dado é qualquer dado.Aqui uma palavra ou uma letra são uma 'string'. Ex. lista = ['a'] ou lista = ['olha']
Exemplos:
- Mutáveis: iniciam com alguns elementos, mas podem agregar mais elementos ou diminuir em quantidade.
# usando o terminal abaixo e dado um 'dir( )' podemos obter todas as funçoes que podem ser usadas com o dado 'lista5'
#>>> dir(lista5)no terminal
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__',
 '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__',
 '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index',
 'insert', 'pop', 'remove', 'reverse', 'sort']


lista1 = [ 1,2,3,44,67,999,0]

lista2 = ['g','U', 'J', 'M', 'y', 'I']

lista3 = []

#1
lista4 = list(range(11))
lista4
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#2
lista5 = list('Geek University')
lista5
['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

#2.1
lista5 = list('Geek University')
print(lista5[::-1])
['y', 't', 'i', 's', 'r', 'e', 'v', 'i', 'n', 'U', ' ', 'k', 'e', 'e', 'G']


#3
#podemos facilmente checar se determinado valor está na lista: 3
num = 3
if num in lista4:
    print(f'Encontrei o número {num}!')
else:
    print(f'Não existe o numemro {num} na lista4!')

#4
#lista5 = list('Geek University')
if 'e' in lista5:
    print('Encontrei a letra e !')
else:
    print('Não encontrei a letra e!')

#5
#usando comando 'sort' podemos ver como ele se comporta no exemplo:

lista1 = [ 1,2,3,44,67,999,0]
lista1.sort()
print(lista1)
[0, 1, 2, 3, 44, 67, 999]

#6
lista5 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista5.sort()
print(lista5)
[' ', 'G', 'U', 'e', 'e', 'e', 'i', 'i', 'k', 'n', 'r', 's', 't', 'v', 'y']

#7
#usando o comando ' count  ' podemos contar o número de ocorrência de um valor em uma lista:
lista1 = [ 1,2,3,44,67,999,0]
print(lista1.count(1))
1

#8
lista5 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
print(lista5.count('e'))
3

#8.1
'len' de length é usado para saber qtos elementos a compoem.
lista1 = [ 1,2,3,44,67,999,0]
lista2 = ['g','U', 'J', 'M', 'y', 'I']
print(len(lista1))
7
print(len(lista2))
6

#9
# usando o comando ' ' podemos adicionar elementos em um lista.
# obs.: não podemos adicionar mais de um elemento por vez, mas tão somente um.
# no lista.append() e no lista.extend() os dados adicionados vão para o fim da lista.

lista1 = [ 1,2,3,44,67,999,0]
print(lista1)
lista1.append(42)# um elemento!
print(lista1)
[0, 1, 2, 3, 44, 67, 999]
[0, 1, 2, 3, 44, 67, 999, 42]

#lista1.append(32, 34, 56) dá erro, pois há mais de um elemento!
#mas é possível uma lista dentro de outra lista como abaixo:

#10
# coloca os números como uma lista dentro de outra.(sublista) ou números individuais.
lista1 = [ 1,2,3,44,67,999,0]
print(lista1)
lista1.append(42)# um elemento!
print(lista1)
[0, 1, 2, 3, 44, 67, 999]
[0, 1, 2, 3, 44, 67, 999, 42]

lista1 = [ 1,2,3,44,67,999,0]
#lista1.append([2,3,5])
print(lista1)
[0, 1, 2, 3, 44, 67, 999, 42, [2, 3, 5]]

#11
 if [2,3,5] in lista1:
    print('Encontrei a lista!')
else:
    print('Não encontrei a lista!')
# resultado: Encontrei a lista!

#12
#São acrescentados blocos de dados.
#Coloca os números individualmente como adicionais.
lista1 = [ 1,2,3,44,67,999,0]
lista1.extend([122, 34, 56])
print(lista1)
[0, 1, 2, 3, 44, 67, 999, 42, [2, 3, 5], 122, 34, 56]

#13
#como se fosse uma lista com as barras!
lista1 = [ 1,2,3,44,67,999,0]
lista1.extend(['Geek'])
print(lista1)
[0, 1, 2, 3, 44, 67, 999, 42, [2, 3, 5], 122, 34, 56, 'Geek']

#14
#como se fosse uma string normal.
lista1.extend('geek')
print(lista1)
[0, 1, 2, 3, 44, 67, 999, 42, [2, 3, 5], 122, 34, 56, 'Geek', 'g', 'e', 'e', 'k']

#15
#aqui, inserimos um valor na posição 2
lista1 = [ 1,2,3,44,67,999,0]
lista1.insert(2, 'novo valor')
print(lista1)
[0, 1, 'novo valor', 2, 3, 44, 67, 999, 42, [2, 3, 5], 122, 34, 56, 'Geek', 'g', 'e', 'e', 'k']

#15.1
# trabalhar com insert
vetor = [1,-1,2,3]
for i in vetor:
    if i < 0:
        vetor.insert(vetor.index(i), '0')
        vetor.pop(vetor.index(i))
print(vetor)
[1,0,2,3]

#16
#aqui cria-se uma nova lista!
lista1 = [ 1,2,3,44,67,999,0]
lista2 = ['g','U', 'J', 'M', 'y', 'I']
lista6 = lista1 + lista2
print(lista6)
[1, 2, 3, 44, 67, 999, 0, 'g', 'U', 'J', 'M', 'y', 'I']

#17
#faz a mesma coisa que no exemplo acima, mas aqui se adiciona algo a lista existente; não se cria uma lista nova.
lista1 = [ 1,2,3,44,67,999,0]
lista2 = ['g','U', 'J', 'M', 'y', 'I']
lista1.extend(lista2)
print(lista1)
[1, 2, 3, 44, 67, 999, 0, 'g', 'U', 'J', 'M', 'y', 'I']

#18
#já modificada acima com a lista2, recebe a lista2 novamente.
lista1 = [ 1,2,3,44,67,999,0]
lista2 = ['g','U', 'J', 'M', 'y', 'I']
lista1.extend(lista2)
print(lista1)
[1, 2, 3, 44, 67, 999, 0, 'g', 'U', 'J', 'M', 'y', 'I']

lista1 = [1, 2, 3, 44, 67, 999, 0, 'g', 'U', 'J', 'M', 'y', 'I']
lista2 = ['g','U', 'J', 'M', 'y', 'I']
lista1 = lista1 + lista2 aqui a lista1,
print(lista1)
[1, 2, 3, 44, 67, 999, 0, 'g', 'U', 'J', 'M', 'y', 'I', 'g', 'U', 'J', 'M', 'y', 'I']

#19 print(lista1) aqui os números das listas têm suas posições invertidas.
lista1 = [ 1,2,3,44,67,999,0]
lista2 = ['g','U', 'J', 'M', 'y', 'I']
print(lista1)
print(lista2)
('=' * 50)
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)
[1, 2, 3, 44, 67, 999, 0]
['g', 'U', 'J', 'M', 'y', 'I']
#======================================================================
[0, 999, 67, 44, 3, 2, 1]
['I', 'y', 'M', 'J', 'U', 'g']

#20 Aqui,com esse comando tb podemos inverter a lista.
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

#21 'len' de length é usado para saber qtos elementos a compoem.
lista1 = [ 1,2,3,44,67,999,0]
lista2 = ['g','U', 'J', 'M', 'y', 'I']
print(len(lista1))
7
print(len(lista2))
6

#22 aqui podemos copiar uma lista já existente.
lista2 = ['g','U', 'J', 'M', 'y', 'I']
lista6 = lista2.copy()
print(lista6)
['g', 'U', 'J', 'M', 'y', 'I']

# 23 o comando pop deleta a último elemento da lista.
lista1 = [ 1,2,3,44,67,999,0]
print(lista1)
lista1.pop()
print(lista1)
[1, 2, 3, 44, 67, 999, 0]
[1, 2, 3, 44, 67, 999]

#24 o comando pop também pode deletar um elemento específico, no caso, o da posição 2.
lista1 = [ 1,2,3,44,67,999,0]
print(lista1)
lista1.pop(2)
print(lista1)
[1, 2, 3, 44, 67, 999]
[1, 2, 44, 67, 999]

#24.1
# trabalhar com pop
vetor = [1,-1,2,3]
for i in vetor:
    if i < 0:
        vetor.insert(vetor.index(i), '0')
        vetor.pop(vetor.index(i))
print(vetor)
[1,0,2,3]

#25 comando 'clear' limpa toda a lista.
lista1 = [ 1,2,3,44,67,999,0]
lista1
lista1.clear()
print(lista1)
[]

#26 podemos repetir elementos em uma lista com uma multiplicação.
lista_nova = (1,2,3)
print(lista_nova)
lista_nova = lista_nova * 3
print(lista_nova)
(1, 2, 3)
(1, 2, 3, 1, 2, 3, 1, 2, 3)

#27 comando split divide uma string em partes de acordo com os espaços que ela contêm!
curso = 'Programação em Python essencial!'
print(curso)
curso = curso.split()
print(curso)
Programação em Python essencial!
['Programação', 'em', 'Python', 'essencial!']

#28 comando split pode ser específico e dividir a string em partes particulares.
curso = 'Programação,em,python,essencial'
print(curso)
curso = curso.split(',')
print(curso)
Programação,em,python,essencial
['Programação', 'em', 'python', 'essencial']

#29 comando split pode ser específico e dividir a string em partes particulares ou numa lista.
curso = 'Programação,em,python,essencial'
print(curso)
curso = curso.split(',')
print(curso)
#Programação,em,python,essencial
#['Programação', 'em', 'python', 'essencial']

#30
#Comando join usado para unir uma lista em string.Aqui usa-se a lista5,
#coloca-se espaços e a une-se em uma string.Use espaço para unir os elementos.
print(curso)
curso = ' '.join(curso)
print(curso)
['Programação', 'em', 'python', 'essencial']
Programação em python essencial

#31
lista5 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista6 = '-'.join(lista5)
print(lista6)
G-e-e-k- -U-n-i-v-e-r-s-i-t-y

#32 qqer dado é possível em um lista. O tipo é lista.
lista6 = [1, 2.35, True, 'Geek', 'd', [1,2,3], 34534534534534534]
print(lista6)
print(type(lista6))
[1, 2.35, True, 'Geek', 'd', [1,2,3], 34534534534534534]

lista1 = [ 1,2,3,44,67,999,0]

lista2 = ['g','U', 'J', 'M', 'y', 'I']

lista3 = []

lista5 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
#33
#Utilizando o for imprimir os elementos da lista solicitada.
lista2 = ['g','U', 'J', 'M', 'y', 'I']
for elemento in lista2:
    print(elemento)
    g
    U
    J
    M
    y
    I

#34
# Utilizando o 'for' imprimir os elementos da lista solicitada
soma = 0
lista1 = [ 1,2,3,44,67,999,0]
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

#35
# Utilizando o 'for' imprimir os elementos da lista solicitada
soma = ' '
lista2 = ['g','U', 'J', 'M', 'y', 'I']
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print(soma)
g
U
J
M
y
I
 gUJMyI

#36
#Usando o while
carrinho = []
produto = ' '
while produto != 'sair':
    print('Adicione um produto a lista ou digite sair para sair!')
    produto = input( )
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)
Adicione um produto a lista ou digite sair para sair!
playstation 4
Adicione um produto a lista ou digite sair para sair!
video game
Adicione um produto a lista ou digite sair para sair!
sair

playstation 4
video game

#37
numeros = [1,2,3,4,5]
print(numeros)
#or
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1,num2,num3,num4,num5]
print(numeros)

#38
#           0       1         2          3
cores = ['azul', 'amarelo', 'verde', 'branco']
print(cores[0])#azul
print(cores[1])#amarelo
print(cores[2])#verde
print(cores[3])#branco

#39
Aqui, podemos imprimir um elemento dando a posição dela no print.
#         0       1         2          3
cores = ['azul', 'amarelo', 'verde', 'branco']
print(cores[0])#azul
print(cores[1])#amarelo
print(cores[2])#verde
print(cores[3])#branco

#40
Aqui, podemos imprimir os elementos na forma inversa usando o negativo na posição deles no print.
#            0       1         2          3
cores = ['azul', 'amarelo', 'verde', 'branco']
print(cores[-1])#branco
print(cores[-2])#verde
print(cores[-3])#amarelo
print(cores[-4])#azul

#41
#            0       1         2          3
cores = ['azul', 'amarelo', 'verde', 'branco']
for cor in cores:
    print(cor)
#azul
#amarelo
#verde
#branco

#42
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1
azul
amarelo
verde
branco

#43
#usamos o for para também informar o índice juntamente com os elementos
#          0       1         2          3
cores = ['azul', 'amarelo', 'verde', 'branco']
for indice, cor in enumerate(cores):
    print(indice, cor)
    0 azul
    1 amarelo
    2 verde
    3 branco

#44
cores = ['azul', 'amarelo', 'verde', 'branco']
cores = list(enumerate(cores))
print(cores)
[(0, 'azul'), (1, 'amarelo'), (2, 'verde'), (3, 'branco')]

#44.1
#enumerate: imprime todos os elementos colocando índices, usando o 'for'.
lista = [ 22,3,2,9,0,6]
for indice, i in enumerate(lista):
    print(indice, i)
0 22
1 3
2 2
3 9
4 0
5 6

#45
#Aqui é pra mostrar que a lista aceita valores repetidos.
lista = []
lista.append(42)
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
print(lista)
[42, 42, 42, 33, 33]

#46
Encontrar o índice de um elemento na lista. (numeros.index( ))
numeros = [3,4,5,6,7,8,10,5]
print(numeros.index(6)) # em qual índice da lista está o elemento 6?
print(numeros.index(10)) # em qual índice da lista está o elemento 10?
print(numeros.index(5))# caso haja dois números repetidos o primeiro índice dos dois ou mais será o que aparecerá.
print(numeros.index(5,3))# busca o próximo índice do número 5 a partir do índice 3(3 que é primeiro elemento 5).
print(numeros.index(8,0,7))# busca o número 8 entre os índices 0 e 7.
3
6
2
7
5

#46.1
# trabalhar com index
vetor = [1,-1,2,3]
for i in vetor:
    if i < 0:
        vetor.insert(vetor.index(i), '0')
        vetor.pop(vetor.index(i))
print(vetor)

#46.2
#index
# print(lista.index(30)) #imprimi o elemento na posição 30 da lista.

#47
REVISAO SOBRE SLICING.
# lista(inicio:fim:passo)
#range(inicio:fim:passo)
#Trabalhando com slice de 'lista' no parâmetro início.
lista = [1,2,3,4]
print(lista[1:]) # iniciando no índice 1 e indo até o último elemento.
print(lista[::]) # imprimi todos os elementos da lista.
print(lista[1]) # imprimi o elemento localizado no índice 1, ou seja, 2.
print(lista[0]) # imprimi o elemento localizado no índice 0, ou seja, 1.
print(lista[-1:]) # imprimi o elemento localizado no índice -1, ou seja, 4
print(lista[-3:])#imprimi elementos localizados do índice -1 até -3.
print(lista[-4:])#imprimi elementos localizados do índice -1 até -4.
[2, 3, 4]
[1, 2, 3, 4]
2
1
[4]
[2, 3, 4]
[1, 2, 3, 4]

#48
Trabalhando com slice de 'lista' no parâmetro fim.
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista[:2])# aqui o print começa no 0 (:) e vai até o segundo índice(2-1).
print(lista[:4])# aqui o print começa no 0 (e vai até o 4th índice(4-1).
print(lista[:6])# aqui o print começa no 0 e vai até o 6th índice.(6-1)
print((lista[1:3]))#
[1, 2]
[1, 2, 3, 4]
[1, 2, 3, 4, 5, 6]
[2, 3]


#49
Trabalhando com slice de 'lista' no parâmetro passo.
print(lista[1::2]) # começa em 1 e vai até o fim de 2 em 2.
print(lista[::2]) # começa em 0 e vai até o fim de 2 em 2.
print(lista[1:-1]) # começa em 1 e vai até o fim de
print(lista[1::-1])# 2h03min!!
[1, 3]
[2, 3]
[2, 1]

#revisão de string.
curso = 'programacao em python essencial'
print(curso[::-1])
laicnesse nohtyp me oacamargorp

#50
invertendo valores em uma lista.

#forma 1
nomes = ['geek', 'university']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
['university', 'geek']


#forma 2
nomes = ['geek', 'university']
nomes.reverse()
print(nomes)
['university', 'geek']


#51
para o sum, max e min os elementos devem ser números inteiros ou reais.
#soma, valor_max, valor_min, tamanho Nomes, codigos... não são aceitos.
lista = [1,2,3,4,5,6]
print(sum(lista))  # soma os valores de uma lista.
print(max(lista))  # acho o valor maior de uma lista.
print(min(lista))  # acho o valor mínimo de uma lista.
print(len(lista))  # acho o comprimento de uma lista, qtos elementos ela possue.
21
6
1
6

#52
#transformar uma lista em tupla
#aqui, a diferença entre a lista e a tupla é a apenas o parênteses () para tupla e colchetes [] para lista.

lista = [1,2,3,4,5,6]
print(lista)
print(type(lista))
[1, 2, 3, 4, 5, 6]
<class 'list'>

lista = [1,2,3,4,5,6]
tupla = tuple(lista)
print(tupla)
print(type(tupla))
(1, 2, 3, 4, 5, 6)
<class 'tuple'>

#53
desempacotamento de listas.
lista = (1,2,3)
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)
1
2
3

#54
#Deep Copy
# Deep copy ( Não há alteração em uma lista dada uma alteração em outra!)
#Copiando uma lista para a outra
# Utilizamos lista.copy() para copiar dados de uma lista para uma nova.
# A modificação da segunda lista(nova) não afetou a primeira(lista).

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



#55
#Shallow copy
# Nessa forma uma modificação em uma lista modifica a outra. No python isso é shallow copy!
#(Há alteração de uma cópia pra outra.)

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

"""
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista[:2])# aqui o print começa no 0 (:) e vai até o segundo índice(2-1).
print(lista[:4])# aqui o print começa no 0 (e vai até o 4th índice(4-1).
print(lista[:6])# aqui o print começa no 0 e vai até o 6th índice.(6-1)
print((lista[1:3]))# aqui o print começa no índice 1  (número 2) e vai até o 3th índice(número 3)
