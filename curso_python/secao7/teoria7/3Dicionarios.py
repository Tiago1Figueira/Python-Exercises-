"""
Dicionários {} são conhecidos como mapas em algumas linguagens de programação.
Assim como as listas [] e as tuplas (), os dicionários são coleções, contudo possuem chave e
valor como elementos.
Observação:
1- Chaves {} e valores são separados por ':'.
chave:valor - ex. {'br':'Brasil'}
2- chave e valor podem ter qquer tipo de dado.
3- podemos misturar tipos de dados.

# Métodos de dicionário
dir({})(terminal dir())
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__',
 '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
 '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']


#1
paises = {'br':'Brasil','usa':'Estados Unidos', 'py':'Paraguai'}
print(paises)
print(type(paises))
{'br': 'Brasil', 'usa': 'Estados Unidos', 'py': 'Paraguai'}
<class 'dict'>

#2
paises = dict(br='brasil', usa='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))
{'br': 'brasil', 'usa': 'Estados Unidos', 'py': 'Paraguai'}
<class 'dict'>

# Acessando elementos
Em listas e tuplas acessamos elementos dessas coleçoes usando o colchete [].
Ex.: print(lista[2]) ou print(tupla1[4]), nos quais 2 e 4 são os índices de referência.
Já em dicionários a ideia é a mesma, contudo usamos chaves ao invés de parênteses.

#3
Acesse elementos do dicionario de 2 formas parecidas com as listas e com o tuplas.

Forma 1
(qdo não se acha o país aparece mensagem de erro!!)
paises = {'br':'Brasil','usa':'Estados Unidos', 'py':'Paraguai'}
print(paises['br'])
print(paises['py'])
Brasil
Paraguai

Forma 2
(qdo não se acha o país não aparece mensagem de erro!! Essa é a forma mais popular!)
paises = {'br':'Brasil','usa':'Estados Unidos', 'py':'Paraguai'}
print(paises.get('br'))
print(paises.get('py'))
Brasil
Paraguai

#4
paises = {'br':'Brasil','usa':'Estados Unidos', 'py':'Paraguai'}
pais = paises.get('py')
if pais:
    print('Encontrei o país.')
else:
    print('Não encontrei o país.')
# Encontrei o país.

#4.1
usando a forma 2 (paises.get( )) e não a forma 1, caso não se ache o país (ru = Russia), não haverá erro!
paises = {'br':'Brasil','usa':'Estados Unidos', 'py':'Paraguai'}
pais = paises.get('ru')
if pais:
    print('Encontrei o país.')
else:
    print('Não encontrei o país.')
# Não encontrei o país.

#5
paises = {'br':'Brasil','usa':'Estados Unidos', 'py':'Paraguai'}
pais = paises.get('py', 'Não encontrado!')#5.1 segunda variável é acionada qdo a primeira não é encontrada.
print(f'Encontrei o país: {pais}.')
# Encontrei o país: Paraguai. #5.2 caso o get encontre o país pedido, o print o mostrará.

#6
# Podemos determinar se uma chave('br', 'usa', 'py') se encontra em um dicionário(paises).
# A busca não é válida para valores(Brasil, Estados Unidos, Paraguai), mas somente para chaves.

paises = {'br':'Brasil','usa':'Estados Unidos', 'py':'Paraguai'}
print('br' in paises)
True
print('ru' in paises)
False
print('Estados Unidos' in paises)
False
# aqui se a chave encontra um correspondente valor no dicionário é true, senão false.
Não achou? Não há erros, há descarte e a resposta 'falso' é dada.

#7
#Como chaves de dicionário, podemos utilizar qqer tipo de dado(int, float, string, boolean)
inclusive, lista e tupla. Tuplas são boas para serem utilizadas como chaves, pois ambas são imutáveis.
localidades = {
    (3544, 5656): ' Escritório em Japão:',
    (4244, 9056): ' Escritório em NYC:',
    (4444, 2356): ' Escritório em São Paulo:',
}
print(localidades)
print(type(localidades))
{(3544, 5656): ' Escritório em Japão:', (4244, 9056): ' Escritório em NYC:', (4444, 2356): ' Escritório em São Paulo:'}
<class 'dict'>

#8
#adicionar elementos em um Dicionário
receita = {'jan':'245', 'fev':'345', 'mar': '123'}
print(receita)
print(type(receita))
{'jan': '245', 'fev': '345', 'mar': '123'}
<class 'dict'>

#forma 1 (mais comum)
receita['abr'] = 3789
print(receita)
{'jan': '245', 'fev': '345', 'mar': '123', 'abr': 3789}

#forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)
{'jan': '245', 'fev': '345', 'mar': '123', 'abr': 3789}
{'jan': '245', 'fev': '345', 'mar': '123', 'abr': 3789, 'mai': 500}

#9
#atualizando dados de um Dicionário.(atualizar ou adicionar têm o mesmo processo e resultado.
#conclusão1:a forma é a mesma para se atualizar ou adicionar um elemento à um dicionário.
#conclusão2: fica claro que não podemos repetir chaves, pois valores diferentes para uma mesma chave
atualizam o valor da chave.
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
#remover dados de um dicionário:
# na lista e aqui o 'pop' é usado para remover o último elemente da coleção.
# Exceçao: tuplas pois são imutáveis.

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

#11
#Imagine que vc tem um comércio eletrônico, onde temos um carrinho de compras e adicionamos produtos:

# Forma1 (com listas)
Carrinho de compras:
  Produtos 1:
  - nome
  - quantidade
  - preço
  Produto 2:
  - nome
  - quantidade
  - preço

carrinho = []
produto1 = ['playstation 4', '1', '2300']
produto2 = ['god of war 4', '1', '150']
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
[['playstation 4', '1', '2300'], ['god of war 4', '1', '150']]
# teríamos que saber o índice de cada ítem.

#Forma2 (com tuplas)

produto1 = ('playstation 4', '1', '2300')
produto2 = ('god of war 4', '1', '150')

carrinho = (produto1, produto2)
print(carrinho)
(('playstation 4', '1', '2300'), ('god of war 4', '1', '150'))
# teríamos que saber o índice de cada ítem.

#Forma3 (com dicionários)
carrinho = []
produto1 = {'nome':'playstation 4','quantidade':'1','valor':'2300'}
produto2 = {'nome':'god of war 4','quantidade':'1','valor':'150'}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
[{'nome': 'playstation 4', 'quantidade': '1', 'valor': '2300'}, {'nome': 'god of war 4', 'quantidade': '1', 'valor': '150'}]

#12
# limpar o dicionário.(zerar o dicionário)
d.clear()
print(d)

d= dict(a=1,b=2,c=3)
print(d)
print(type(d))
{'a': 1, 'b': 2, 'c': 3}
<class 'dict'>

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
# Como na tupla, quando se faz uma alteração no dicionário novo altera-se também o original.
# forma 2 (shallow copy) (Há alteração no dicionário original)
d= dict(a=1,b=2,c=3)
print(d)
print(type(d))
{'a': 1, 'b': 2, 'c': 3}
<class 'dict'>

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
<class 'dict'>

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))
{'nome': 'desconhecido', 'pontos': 'desconhecido', 'email': 'desconhecido', 'profile': 'desconhecido'}
<class 'dict'>

#16
veja = {}.fromkeys('teste','valor')
print(veja)
print(type(veja))
{'t': 'valor', 'e': 'valor', 's': 'valor'}# um valor por letra. só não ha repetição de chaves como nas letras 't' e 'e'.
<class 'dict'>

veja = {}.fromkeys(range(1,11),'novo')
print(veja)
{1: 'novo', 2: 'novo', 3: 'novo', 4: 'novo', 5: 'novo', 6: 'novo', 7: 'novo', 8: 'novo', 9: 'novo', 10: 'novo'}

"""

