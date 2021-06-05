# definindo funçoes
#1
def diz_oi():
    print('oi')
diz_oi()
#oi

#2
def cantar_parabens():
    print('Parabens pra vc')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
cantar_parabens()

"""
Parabens pra vc
Nesta data querida
Muitas felicidades
Muitos anos de vida
"""

#3
for i in range(5):
   cantar_parabens()
"""
Parabens pra vc
Nesta data querida    x5
Muitas felicidades
Muitos anos de vida
"""

#FUNÇOES COM RETORNO

#1
numeros = [1,2,3]
ret_pop = numeros.pop()
print(f'retorno do pop: {ret_pop}' )
#retorno do pop: 3

#2
def diz_oi():
    return('oi ')

alguem = ('Pedro!')

print(diz_oi( ) +  alguem)
# oi Pedro!

#exemplo 2.1:
#o que está após o 'return' não será impresso.
def diz_oi():
    return('oi ')
    print('Estou sendo executado depois do return.')
print(diz_oi())
#oi

#exemplo 2.2:
#podemos ter em uma funçao diferentes returns.
def nova_funcao():
    variavel = True
    if variavel:
        return(4)
    elif variavel is None:
        return (3)
    return('b')
print(nova_funcao())
4

#exemplo 2.3:
# podemos, em uma função, retornar qualquer tipo de dado e até msm múltiplos valores.

def outra_funcao():
    return 2,3,4,5 # Aqui se gera uma tupla devido aos números separados por vírgula.
print(outra_funcao())
#(2, 3, 4, 5) Aqui temos uma tupla! Sabemos que não há necessidade de se colocar os números nas variáveis.

#exemplo 2.3.1:
def outra_funcao():
    return 2,3,4,5
num1, num2, num3, num4 = outra_funcao() # aqui estamos desempacotando os números das variáveis.
print(num1, num2, num3, num4)
# 2 3 4 5

#3
#criando função: função para jogar uma moeda
from random import random
def jogar_moeda():
    valor = random() # gera um número pseudo-randomico entre 0 e 1.
    if valor > 0.5:
        return "cara"
    return 'coroa'
print(jogar_moeda())

#4
#criando função: função para jogar uma moeda
from random import random
def jogar_moeda():
    if random() > 0.5:
        return "cara"
    return 'coroa'
print(jogar_moeda())
# gera um número pseudo-randomico entre 0 e 1.
print(random())

#5
def quadrado_de_7():
      return 7 * 7
print(quadrado_de_7())

#5.1
def quadrado(numero):
    return numero * numero
print(quadrado(7))
print(quadrado(2))
print(quadrado(5))
49
4
25

#5.2
def quadrado(numero):
    return numero * numero
ret = quadrado(6)
print(ret)

print(quadrado())#typeError


# FUNÇÕES COM PARÂMETROS

#1
def quadrado(numero):
    return numero * numero
print(quadrado(7))
print(quadrado(2))
print(quadrado(5))
49
4
25

#2
def quadrado(numero):
    return numero * numero
ret = quadrado(6)
print(ret)
36

#3
def cantar_parabens(aniversariante):
    print('Parabens pra vc')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}!')
cantar_parabens('Marcos')
#Parabens pra vc
#Nesta data querida
#Muitas felicidades
#Muitos anos de vida
#Viva o Marcos!

#4
#funções podem receber quantos parâmetros forem necessário, desde que usando vírgulas.
def soma(a,b):
    return a + b
def multiplicacao(num1, num2):
    return num1 * num2
def outra(num1, b,msg):
    return (num1 + b) * msg
print(soma(2,5))
print(soma(10,20))
7
30

print(multiplicacao(2,5))
print(multiplicacao(4,7))
10
28

print(outra(3,2,' Geek '))
print(outra(5,4,' Python  '))
# Geek  Geek  Geek  Geek  Geek
# Python   Python   Python   Python   Python   Python   Python   Python   Python

#5
#nomeando parâmetros
def nome_completa(nome, sobrenome ): #parâmentros
    return f' O seu nome completo é {nome} {sobrenome}.'
print(nome_completa('Angelina', 'Jolie')) #argumentos
#O seu nome completo é Angelina Jolie.

#6
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total # o erro acontece qdo se coloca o 'return' no bloco do 'total' e, consequentemente, o return retornará somente o valor 1,
    # pois somará somente uma vez. Lembre-se, após o return nada mais é processado.

numeros = [1,2,3,4,5,6,7]
print(soma_impares(numeros))

# FUNÇÕES COM PARÂMETRO PADRÃO

#1
#Exemplo no qual a provisão do parâmetro é obrigatória, não opcional!
def quadrado(numero):
    return numero ** 2

print(quadrado(9))
print(quadrado()) # aqui dá erro!
81

#3
# Aqui a função está normal!
def exponencial(numero, expoente): #parâmetros
    return numero ** expoente

print(exponencial(2,2))#argumentos #2*2 = 4
print(exponencial(2,3))            #2*2*2 = 8
4
8

#3.1
#Aqui, o parâmetro 'expoente' padronizou o n°2, que dá o quadrado do número. É opcional, caso o usuário não fornece nada.
def exponencial(numero, expoente=2): #parâmetros
    return numero ** expoente

print(exponencial(2))#argumentos   #2*2 = 4 Apesar de ser somente 1 argumento e não 2, não dá erro! Eleva à potência padronizada.
print(exponencial(3,5))            #3*3*3*3*3 = 243 Eleva à potência dada pelo usuário.
4
243

#3.2
#Aqui se usa os expoentes padrôes, 4 e 2. Logo, ambos números serão utilizados se o usuário não digitar qquer valor.
def exponencial(numero=4, expoente=2): #parâmetros
    return numero ** expoente

print(exponencial(2))#argumentos   #2*2 = 4 Apesar de ser somente 1 argumento e não 2, não dá erro! Eleva à potência padronizada.
print(exponencial(3,5))            #3*3*3*3*3 = 243 Eleva à potência dada pelo usuário.
print(exponencial())               #4*4 = 16


#3.3
# Em python, o valores default(padrão) SEMPRE devem estar ao fim da declaração dos parâmetros.
#def teste(numero=2, potencia): #ERRO: o número default(padronizado) deve ir ao fim da declaração.
#    return numero ** potencia

#print(teste(2))

#3.3.1
def teste(potencia,numero=2): #Aqui o número default(padronizado) deve ir ao fim da declaração. Não há erro!!
    return numero ** potencia

print(teste(6)) #2 ** 6 ou 2*2*2*2*2*2 = 64
64

#4
#exemplo de typeError
def soma(num1,num2):
    return num1 + num2

print(soma(3,4))
# print(soma(2)) #typeError
# print(soma()) #typeError

#4.1
# Exemplo sem typeError

def soma(num1 = 4,num2 = 5):
    return num1 + num2

print(soma(3,4))
print(soma(2)) # SEM typeError
print(soma()) #  SEM typeError
7
7
9

#4.2
#exemplo complexo

def mostrar_informacao(nome='Geek', instrutor = False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo, instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que vc era instrutor!'
    return f'Olá {nome}'

print(mostrar_informacao('Geek'))
print(mostrar_informacao(True))
print(mostrar_informacao('Geek', 'True'))
print(mostrar_informacao('Sthephany'))
print(mostrar_informacao('Tiago'))

#Eu pensei que vc era instrutor!
#Olá True
#Bem-vindo, instrutor Geek!
#Olá Sthephany
#Olá Tiago

#5
#exemplos de funções como parâmetro

def diz_oi():
    print('oi')

variavel = diz_oi()

variavel ()

#5.1
def mul(num1, num2):
    return num1 * num2

def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def mat(num1, num2, fun=subtracao):
    return fun(num1, num2)

print(mat(2,3))
print(mat(2,3, subtracao))
print(mat(2,3, mul))
-1
-1
6

#6
# Variável global vs variável Local

# instrutor = 'Tiago' (variável global)

def diz_oi():
    instrutor = 'Python' # (variável local)
    return f'Oi {instrutor}'

print(diz_oi())
#obser.: se tivermos 2 variáveis, uma local e outra global, a local terá preferência sobre a outra.

#6.1
def diz_oi():
    instrutor = 'Python' # (variável local)
    return f'Oi {instrutor}'

print(diz_oi())
# print(instrutor)  variável local não é reconhecida. nameError


#6.2
# Se puder evitar variáveis globais nas funçoes evite-as!

"""
total = 0
def incrementa():
    total = total + 1
    #a variável global não pode iniciar ou alimentar a variável local. Dá UnboundLocalError!!!

print(incrementa())
"""

#6.3
# avisando ao python que a variável global irá alimentar a variável local
total = 0
def incrementa():
    global total # avisando ao python que a variável global irá alimentar a variável local

    total = total + 1
    return total
print(incrementa())
print(incrementa())
print(incrementa())

#6.4
# Podemos ter funções que são declaradas dentro de funções e também têm uma forma especial de escopo de variável .

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())
#print(dentro()) # nameError = aqui, a função dentro está dentro da função fora e assim não é reconhecida.
1
1
1

# Entendendo o args*


#1
#função SEM parâmetro padrão

def soma_todos_numeros(num1,num2,num3):
    return num1 + num2 + num3

print(soma_todos_numeros(4,5,6) )
#print(soma_todos_numeros(4,6)) typeError (menos argumentos do que o necessário.)
#print(soma_todos_numeros(4,5,6,7)) typeError (mais argumentos do que o necessário.)

#2
#função COM parâmetro padrão

def soma_todos_numeros(num1=1,num2=2,num3=3):
    return num1 + num2 + num3

print(soma_todos_numeros(4,5,6) )
print(soma_todos_numeros(4,6)) #não há mais typeError!
#print(soma_todos_numeros(4,5,6,7)) typeError (mais argumentos do que o necessário.)

#3
#entendendo o *args

def soma_dos_numeros(*args):
    print(args)
soma_dos_numeros()
soma_dos_numeros(1)
soma_dos_numeros(2,3)
soma_dos_numeros(2,3,4)
soma_dos_numeros(3,4,5,6)
()
(1,)
(2, 3)
(2, 3, 4)
(3, 4, 5, 6)

#3.1
#entendendo o *args - fazendo somatória com o 'soma':

def soma_dos_numeros(*args):
    total = 0
    for num in args:
        total = total + num
    return total
print(soma_dos_numeros())
print(soma_dos_numeros(1))
print(soma_dos_numeros(2,3))
print(soma_dos_numeros(2,3,4))
print(soma_dos_numeros(3,4,5,6))
0
1
5
9
18

#3.2
# entendendo o *args - fazendo a soma com o 'sum( )'
#podemos fazer uma soma com o 'sum( )' aqui, já que temos uma tupla.

def soma_dos_numeros(*args):
    return sum(args)

print(soma_dos_numeros())
print(soma_dos_numeros(1))
print(soma_dos_numeros(2,3))
print(soma_dos_numeros(2,3,4))
print(soma_dos_numeros(3,4,5,6))
0
1
5
9
18

#3.3
#entendendo o *args - fazendo a soma com o 'sum( )'
# o 'sum( ) ' faz soma de números inteiros ou reais. Strings não são aceitas!
def soma_dos_numeros(*args):
    return sum(args)
print(soma_dos_numeros())
print(soma_dos_numeros(1))
print(soma_dos_numeros(2,3))
print(soma_dos_numeros(2,3,4))
print(soma_dos_numeros(3,4,5,6))

#print(soma_dos_numeros('a')) syntaxError
print(soma_dos_numeros(23.4, 37.3))

0
1
5
9
18
60.699999999999996

#3.4
#entendendo o *args - fazendo a soma com o 'sum( )'

def soma_dos_numeros(nome, sobrenome,*args):
    return sum(args)

print(soma_dos_numeros('Angelina', 'Julie'))
print(soma_dos_numeros('Angelina', 'Julie', 1))
print(soma_dos_numeros('Angelina', 'Julie', 2,3))
print(soma_dos_numeros('Angelina', 'Julie',2,3,4))
print(soma_dos_numeros('Angelina', 'Julie',3,4,5,6))

print(soma_dos_numeros(23.4, 37.3))

#3.5
#outro exemplo de utilização do args;

def verifica_info(*args):
    if 'Geek' in args and 'University ' in args:
        return 'Bem-vindo Geek!'

    return 'Eu não tenho certeza de quem vc é...'

print(verifica_info())
print(verifica_info(1, True, 'University','Geek'))
print(verifica_info(1, 'University', 3.145))
#Eu não tenho certeza de quem vc é...
#Bem-vindo a Geek!
#Eu não tenho certeza de quem vc é...

#3.6
#fazendo desempacotamento!!! 23min
def soma_dos_numeros(*args):
    return sum(args)

#print(soma_dos_numeros( ))
#print(soma_dos_numeros( 1))

#desempacotar: devemos desempacotar a lista já que o 'sum' entende que todos os números dela como sendo um elemento e não vários.
#qdo eles são desempacotados o 'sum' pode finalmente entender que cada número é um elemento.
numeros = [1,2,3,4,5,6,7]
num1, num2, num3, num4, num5, num6,num7 = numeros

print(soma_dos_numeros(num1,num2,num3,num4,num5,num6,num7))
28

#3.6.1
#fazendo desempacotamento rápido com o *!!! 23min
def soma_dos_numeros(*args):
    return sum(args)
#print(soma_dos_numeros( ))
#print(soma_dos_numeros( 1))

#desempacotar rapidamente: aqui a ação é feita com o '*'. O python entende que a lista com números precisa ser desempacotada para que
#a soma ocorra.
numeros = [1,2,3,4,5,6,7]

print(soma_dos_numeros(*numeros))
28

# ** KWARGS

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

#Esse carro é o mais carro!
#Carro não identificado!
#Carrão legal!

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
#Assim, esses são os parâmetros corretos de declaração.

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
#3 #Casado
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



















