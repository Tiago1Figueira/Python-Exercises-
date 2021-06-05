"""
Introdução - Collections - High-performance container datetypes
Counter : recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com
um dicionário, contendo como chaves os elementos da 'lista' dada como parâmetro e como valor a quantidade
de elementos que esse valor aparece.

#para se obter mais informaçoes sobre o 'Counter'
#checar: docs.python/3/library/collections.html#collections.counter

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
# o comando 'split' separa todas as palavras que estão no texto.

# texto =    recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um
#dicionário, contendo como chaves os elementos da 'lista' dada como parâmetro e como valor a quantidade de elementos
#que esse valor aparece."""

#palavras = texto.split()
#print(palavras)

#3.1
# o comando ' counter ' coloca números nos elementos
# Aqui há uma reunião dos 2 comandos.
#from collections import Counter

#res = Counter(palavras)
#print(res)

['recebe', 'um', 'iterável', 'como', 'parâmetro', 'e', 'cria', 'um', 'objeto', 'do',
 'tipo', 'Collections', 'Counter', 'que', 'é', 'parecido', 'com', 'um', 'dicionário,',
 'contendo', 'como', 'chaves', 'os', 'elementos', 'da', "'lista'", 'dada', 'como',
 'parâmetro', 'e', 'como', 'valor', 'a', 'quantidade', 'de',
 'elementos', 'que', 'esse', 'valor', 'aparece.']

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
#ATIVIDADES

#4.0
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

#"""





