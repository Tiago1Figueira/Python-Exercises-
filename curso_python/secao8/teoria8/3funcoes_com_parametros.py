"""
funções com parâmetros de entrada
- funções que recebem dados para serem processados dentro da mesma.
- um programa qualquer geralmente tem entrada/ processamento / saída.

Há funçoes que:
A - não possuem entrada
B - não possuem saída
C - possuem entrada, mas não saída
D - não possuem entrada, mas têm saída
E - possuem entrada e saída

#Refatoração ou redefinição

#1
def quadrado_de_7():
      return 7 * 7
print(quadrado_de_7())

#2
def quadrado(numero):
    return numero * numero
print(quadrado(7))
print(quadrado(2))
print(quadrado(5))
49
4
25

#3
def quadrado(numero):
    return numero * numero
ret = quadrado(6)
print(ret)

print(quadrado())#typeError

#4
def cantar_parabens(aniversariante):
    print('Parabens pra vc')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva {aniversariante}!')
cantar_parabens('o Marcos')

#Parabens pra vc
#Nesta data querida
#Muitas felicidades
#Muitos anos de vida
#Viva o Marcos!

#5
#funções podem receber quantos parâmetros forem necessário, desde que usando vírgulas.
def soma(a,b):
    return a + b
def multiplicacao(num1, num2):
    return num1 * num2
def outa(num1, b,msg):
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

#6
#nomeando parâmetros
def nome_completa(nome, sobrenome ): #parâmentros
    return f' O seu nome completo é {nome} {sobrenome}.'
print(nome_completa('Angelina', 'Jolie')) #argumentos
#O seu nome completo é Angelina Jolie.

# Parâmetro vs Argumento
# Parâmentros: variáveis declaradas na definição de uma função.
# Argumentos: dados passados durante uma execução.

#7
#Argumentos Nomeados(Keywords Arguments)
# A ordem dos argumentos importa! Logo, no argumento, 'nome' e 'sobrenome' gera resultados diferentes de 'sobrenome' e 'nome'.
# Caso se informe o "nome e sobrenome" nos argumentos, a ordem não importará mais. Exemplos abaixo.

#7.1
def nome_completa(nome, sobrenome ): #parâmentros
    return f' O seu nome completo é {nome} {sobrenome}.'

print(nome_completa(sobrenome= 'Valentina' , nome='Márcia')) #argumentos
#O seu nome completo é Márcia Valentina.

#7.2
(caso precise)
nome = 'Antonia'
sobrenome = 'Valentina'

def nome_completa(nome, sobrenome ): #parâmentros
    return f' O seu nome completo é {nome} {sobrenome}.'

print(nome_completa(sobrenome= 'Jolie' , nome='Angelina'))
print(nome_completa(sobrenome=sobrenome, nome=nome ))
print(nome_completa(sobrenome= 'Valentina' , nome='Márcia'))

# O seu nome completo é Angelina Jolie.
# O seu nome completo é Antonia Valentina.
# O seu nome completo é Márcia Valentina.

#8
# erro comun na utilização do ' return':

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total # o erro acontece qdo se coloca o 'return' no bloco do 'total' e, consequentemente, o return retornará somente o valor 1,
    # pois somará somente uma vez.


numeros = [1,2,3,4,5,6,7]
print(soma_impares(numeros))


"""

#FUNÇÕES COM PARÂMETRO PADRÃO























