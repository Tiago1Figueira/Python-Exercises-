"""
O que é **kwargs?
Poderiamos chamar esse parâmetro de **xis, mas por convenção o chamamos de **kwargs.
Este é só mais uma parâmetro, mas diferente do args, que coloca os valores extras em uma tupla, o **kwargs
exige que utilizemos argumentos nomeados e transforma esses argumentos extras em um dicionário.

#1
# os argumentos são nomeados e o 'print' é um dicionário.
def cores_favoritas(**kwargs):
    print(kwargs)

cores_favoritas(marco='verde', julia='amarelo', fernanda='azul', vanessa='branco')
#{'marco': 'verde', 'julia': 'amarelo', 'fernanda': 'azul', 'vanessa': 'branco'}

#1.1
# os argumentos são nomeados e o 'print' é um dicionário.
def cores_favoritas(a,b,c ,**kwargs):
    print(kwargs)

cores_favoritas(1,2,3, marco='verde', julia='amarelo', fernanda='azul', vanessa='branco')
#{'marco': 'verde', 'julia': 'amarelo', 'fernanda': 'azul', 'vanessa': 'branco'}

#1.2
# os argumentos são nomeados e o python entende como se todos eles fizessem parte do **kwargs.
def cores_favoritas(**kwargs):
    print(kwargs)

cores_favoritas(a=1,b=2,c=3, marco='verde', julia='amarelo', fernanda='azul', vanessa='branco')
#{'a': 1, 'b': 2, 'c': 3, 'marco': 'verde', 'julia': 'amarelo', 'fernanda': 'azul', 'vanessa': 'branco'}

#1.3
#aqui o 'print' escreve o que está descrito no argumento.
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items(): # usamos o itens pq o kwargs é um dicionário tb.
        print(f'A cor favorita de {pessoa} é {cor}.')

cores_favoritas(marco='verde', julia='amarelo', fernanda='azul', vanessa='branco')

#A cor favorita de marco é verde.
#A cor favorita de julia é amarelo.
#A cor favorita de fernanda é azul.
#A cor favorita de vanessa é branco.

#1.4
#aqui o 'print' escreve o que está descrito no argumento e com o comando 'title' o nome adquire letra maiúscula.

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items(): # usamos o comando 'itens' pq o kwargs é um dicionário tb.
        print(f'A cor favorita de {pessoa.title()} é {cor}.') # usamos o comando "title"

cores_favoritas(marco='verde', julia='amarelo', fernanda='azul', vanessa='branco')


#2
# a- verifica se eu tenho a chave 'geek' dentro do meu dicionário 'kwargs'. Se sim, se o valor dessa chave "geek" é python.
# Se sim, retorna a mensagem:' Vocẽ recebeu um cumprimento pythonico Geek!'

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python': # a
        return 'Vocẽ recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f" {kwargs ['geek']} Geek! "
    return 'Não tenho certeza de quem vc é .....'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))
# Não tenho certeza de quem vc é .....
# Vocẽ recebeu um cumprimento Pythônico Geek!
# Oi Geek!
# especial Geek!

#2
# a- verifica se eu tenho a chave 'geek' dentro do meu dicionário 'kwards'. Se sim, se o valor dessa chave "geek" é python.

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python': # a
        return 'Vocẽ recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f" {kwargs ['geek']} Geek! "
    return 'Não tenho certeza de quem vc é .....'

#2.1
#mais exemplos
def carros_legais(**kwargs):
    if 'carro' in kwargs and kwargs['carro'] == 'Ferrari':
        return 'Esse carro é o mais carro!'
    elif 'carro' in kwargs:
        return f" {kwargs ['carro']} legal! "
    return 'Carro não identificado!'

print(carros_legais(carro='Ferrari'))
print(carros_legais())
print(carros_legais(carro='Carrão'))

Esse carro é o mais carro!
Carro não identificado!
Carrão legal!

#2.2
# mais exemplos
def nome_flores(**kwargs):
    if 'flores' in kwargs and kwargs['flores'] == 'margarida':
        return 'Esta é a flor mais bonita.' # qdo se tem uma chave, e a chave (flores) é igual a uma info qqer, aqui margarita retorna-se essa.
    elif 'flores' in kwargs:
        return  f"{kwargs['flores']} são as mais bonitas!" # qdo se tem a chave, mas o que está na chave não se encontra no código é essa.
    return 'Não sei que flor vc é !!' # qdo não se tem qqer info no parênteses do print é essa mensagem que retorna.

print(nome_flores())
print(nome_flores(flores= 'margarida'))
print(nome_flores(flores='Tulipas'))
#Não sei que flor vc é !!
#Esta é a flor mais bonita.
#Tulipas são as mais bonitas!

#2.3
def cidades_bonitas(**kwargs):
    if 'cidades' in kwargs and kwargs ['cidades'] == 'Ubatuba':
        return 'Ubatuba é a cidade mais bonita do litoral paulista.'
    elif 'cidades' in kwargs:
        return f"{kwargs['cidades']} é maravilhosa e quente!"
    return 'Acho que eu não entendi o nome da cidade!'

print(cidades_bonitas(cidades='Ubatuba'))#1
print(cidades_bonitas(cidades='Caragua'))#2
print(cidades_bonitas())#3
#Ubatuba é a cidade mais bonita do litoral paulista.
#Caragua é maravilhosa e quente!
#Acho que eu não entendi o nome da cidade!

#3
# Qdo declararmos as nossas funções, podemos ter NA ORDEM ABAIXO:
# 1° parâmetros obrigatórios;
# 2° args (não são obrigatório serem declarados)
# 3° parâmetros default (declaração não obrigatórios);
# 4° kwargs ( não obrigatório)
Assim, esses são os parâmetros corretos de declaração.

#20minutos
# exemplo de ORDEM está abaixo. n° 1 é o único obrigatório!
#                   1    1     2          3              4
def minha_funcao(idade, nome, args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos.')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8, 'Julia', 5)
minha_funcao(18, 'Felicity', 4,5,6, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9,4,3, java=False, python=True)
#Julia tem 8 anos.
#5
3Casado
#{}

#4
#entendendo pq é importante manter a ordem dos parâmetros na declaração;
def mostra_info(a,b,*args, instrutor='Geek', **kwargs):
    return [a,b,args,instrutor,kwargs]
#a = 1
#b = 2
#args = (3,)
#instrutor = 'Geek'
#kwargs = { 'sobrenome': 'University', 'cargo': 'Instrutor'}
print(mostra_info(1,2,3,sobrenome='University', cargo='Instrutor'))

#[1, 2, (3,), 'Geek', {'sobrenome': 'University', 'cargo': 'Instrutor'}]

#5
# Desempacotando com o **kwargs
def mostra_nomes(*kwargs):
    return f"{kwargs['nome'] } {kwargs['sobrenome']}"

nomes = {'nome':'Felicity', 'sobrenome': 'Jones'}

#1ª forma
#print(mostra_nomes(nome='Felicity', sobrenome='Jones'))

# 2ª forma
#print(mostra_nomes(**nomes))
#Felicity Jones

#6
def soma_multiplos_numeros(a,b,c):
    print(a + b + c)
soma_multiplos_numeros(1,2,3)
6

#6.1
#para a lista, tupla e set usamos um asteristico para o desempacotamento.
def soma_multiplos_numeros(a,b,c):
    print(a + b + c)
lista = [1,2,3]
tupla = (3,4,5)
set_ou_conjuntos = {4,5,6}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*set_ou_conjuntos)
6
12
15

#6.2
#para o dicionário usamos 2 asteristicos para o desempacotamento.
def soma_multiplos_numeros(a,b,c):
    print(a + b + c)
dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(**dicionario)
6

#6.3
# os parâmetros do dicionário(#b) devem ser iguais aos do **dwargs(#a)!Caso contrário haverá 'typeError'!
def soma_multiplos_numeros(a,b,c, **dwargs):#a
    print(a + b + c)
dicionario = dict(d=1, e=2, f=3, nome='Geek')#b
soma_multiplos_numeros(**dicionario, lang='Python')
6

#6.4
# os trẽs parâmetros foram dados. O '**dwargs' foi acrescentado para mostrar que é opcional.
def soma_multiplos_numeros(a,b,c, **dwargs):
    print(a + b + c)
dicionario = dict(a=1, b=2, c=3, nome='Geek')
soma_multiplos_numeros(**dicionario, lang='Python')
6


"""


