"""
Tipo String

CTRL + L para limpar o terminal !
#1
'String'
nome = 'geek'
print(nome[::-1])
keeg

#1.1
#    0    1    2    3    4    5    6    7    8   9     10   11   12   13   14   (15 posições contando com o 0!)
# [ 'g', 'e', 'e', 'k', ' ', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y' ]

nome = 'geek university'
nome[0:4]
nome[5:15]
'geek'
'university'

#1.2
nome ='geek university'
print(nome.replace('g','p'))
peek university

#1.3
nome = 'Geek University'
print(nome.split())
# ['Geek', 'University']

#1.4
          0         1
nome = ['Geek', 'University']
print(nome.split()[0])
# Geek
print(nome.split()[1])
# University

#1.5
nome = 'geek'
print(nome[::-1])
keeg

#2
nome = 'geek university'
print(nome[::])
geek university

#3
nome = 'geek university'
nome[0:15]
'geek university'

#4
nome = 'geek university'
nome[0:4]
'geek'

#5
nome ='geek university'
print(nome.replace('g','p'))
peek university

#6
nome ='geek university'
print(nome.replace('g','p'))
peek university
print(type(nome))
<class 'str'>

#7
nome ='socorram me subi no onibus em marrocos'
print(nome[::-1])
socorram me subino on ibus em marrocos #Palíndromo

#7.1
texto = 'O que eu penso sobre você não importa!'
print(texto.split()[::-1])
#['importa!', 'não', 'você', 'sobre', 'penso', 'eu', 'que', 'O']

#8
nome=Angelina Jolie
print=(nome)
print(type(nome))

#8.1
nome=Angelina \n Jolie
print=(nome)
print(type(nome))

#8.2
nome='geek university'
print=(nome.upper())

#8.3
nome= "GEEK UNIVERSITY"
print=(nome.lower())

#9
nome = 'geek university'
print(nome[::])
print(type(nome))
geek university
<class string>

#10
nome = 'geek university'
nome[0:15] Aqui inicia-se na posição 0 e vai até a 14. A posição 15 não é utilizada.
nome[0:4] Lembre-se: aqui a posição 4 não é utilizada. Vai da posição 0 (letra 'g') até posição 3(letra 'k').
'geek university'
'geek'

#11
colocar o número em uma certa sequẽncia usando índices:
numero = input('Digite um número entre 1000 e 9999:')
print(numero[0])
print(numero[1])
print(numero[2])
print(numero[3])


"""

