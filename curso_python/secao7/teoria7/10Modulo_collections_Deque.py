"""
modulo collections deque
Podemos dizer que o deque é uma lista de alta performance, pois pode adicionar, usando o comando 'append', elementos
ao fim da lista e no começo.
Deques servem para adicionar, remover elementos em uma lista, a esquerda ou a direita.

"""
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

