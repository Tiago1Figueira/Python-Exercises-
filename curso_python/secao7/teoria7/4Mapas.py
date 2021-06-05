"""
Mapas - conhecidos em python como dicionários(representados por {}).

receita = {'jan':'100', 'fev':'250', 'mar':'400'}
print(receita)
{'jan': '100', 'fev': '250', 'mar': '400'}

#1
# interar sobre dicionários.
imprimindo as chaves!!
receita = {'jan':'100', 'fev':'250', 'mar':'400'}
for chave in receita:
    print(chave)
jan
fev
mar

#2
imprimindo os valores!!
receita = {'jan':'100', 'fev':'250', 'mar':'400'}
for chave in receita:
    print(receita[chave])
100
250
400

#3
receita = {'jan':'100', 'fev':'250', 'mar':'400'}
for chave in receita:
    print(f'Recebi em {chave} valor de R$ {receita[chave]}!')
Recebi em jan valor de R$ 100!
Recebi em fev valor de R$ 250!
Recebi em mar valor de R$ 400!
# usa-se {receita[chave]} para se obter os valores referentes as chaves. As chaves são usadas aqui para se obter os valores

#4
#acessando os valores
receita = {'jan':'100', 'fev':'250', 'mar':'400'}
print(receita.keys())
for chave in receita.keys():
    print(receita[chave])
dict_keys(['jan', 'fev', 'mar'])
100
250
400

#4.1
#acessando valores.
receita = {'jan':'100', 'fev':'250', 'mar':'400'}
print(receita)
{'jan':'100', 'fev':'250', 'mar':'400'}

#4.2
receita = {'jan':'100', 'fev':'250', 'mar':'400'}
print(receita.values())
for valor in receita.values():
    print(valor)
#dict_values(['100', '250', '400'])
#100
#250
#400


#5
#desempacotando valores
receita = {'jan':'100', 'fev':'250', 'mar':'400'}
print(receita)
print(receita.items())

#{'jan': '100', 'fev': '250', 'mar': '400'}
#dict_items([('jan', '100'), ('fev', '250'), ('mar', '400')])

#5.1
for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

chave = jan e valor = 100
chave = fev e valor = 250
chave = mar e valor = 400

#6
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

"""
