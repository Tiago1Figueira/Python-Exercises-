"""
Funçôes de parâmetros padrão (default paramters)
Funções nas quais a passagem de parâmetros seja opcional.

#1
Usando-se a função print vemos que o usar o parâmetro 'Brasil' ou não usar qualquer parâmetro não gera erro;
Exemplo no qual a provisão do parâmetro é não é obrigatória, mas sim É opcional!
print('Brasil')
print( )

#2
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
#Aqui se usa os expoentes padrôes, 4 e 2. Logo, assume-se que o usuário não digitou qualquer número.
def exponencial(numero=4, expoente=2): #parâmetros
    return numero ** expoente

print(exponencial(2))#argumentos   #2*2 = 4 Apesar de ser somente 1 argumento e não 2, não dá erro! Eleva à potência padronizada.
print(exponencial(3,5))            #3*3*3*3*3 = 243 Eleva à potência dada pelo usuário.
print(exponencial())               #4*4 = 16


#3.3
# Em python, o valores default(padrão) SEMPRE devem estar ao fim da declaração dos parâmetros.
def teste(numero=2, potencia): #ERRO: o número default(padronizado) deve ir ao fim da declaração.
    return numero ** potencia

print(teste(2))

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

Eu pensei que vc era instrutor!
Olá True
Bem-vindo, instrutor Geek!
Olá Sthephany
Olá Tiago

# Por que utilizar parâmetros default or padrão?

# - podemos trabalhar de forma mais flexível com vários parâmetros;
# - evita erros com parâmetros incorretos;
# - Permite-nos trabalhar com exemplos mais legíveis, claros de código;

# Quais tipos de dados podemos utilizar como parâmetro default ou padrão?
# - Quaisquer tipos de dados: listas, tuplas, dicionários, booleanos, floats, int, funções, números etc.


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

total = 0
def incrementa():
    total = total + 1 # a variável global não pode iniciar ou alimentar a variável local. Dá UnboundLocalError!!!

print(incrementa())

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

"""























































