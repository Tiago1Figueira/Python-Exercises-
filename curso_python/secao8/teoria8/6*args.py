"""
O que é o *args ?
O parâmetro *args, utilizado em uma função, coloca os valores extras informados como entrada em uma tupla.
Então, desde já, lembre-se que tuplas são imutáveis.

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
# entendendo o *args - fazendo a somatória com o 'sum( )'
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
#entendendo o *args - fazendo a somatória com o 'sum( )'
# o 'sum( ) ' faz a somatória de números inteiros ou reais. Strings não são aceitas!
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

#desempacotar: devemos desempacotar a lista já que o 'sum' entende que todos os números dela como sendo um elemento
#e não vários. Qdo eles são desempacotados o 'sum' pode finalmente entender que cada número é um elemento.
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

#desempacotar rapidamente: aqui a ação é feita com o '*'. O python entende que a lista com números precisa ser
#desempacotada para que a soma ocorra.
numeros = [1,2,3,4,5,6,7]

print(soma_dos_numeros(*numeros))
28

"""

























