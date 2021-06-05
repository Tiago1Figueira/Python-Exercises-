"""
FUNÇÕES COM RETORNO

#1
sem retorno
numeros = [1,2,3]
ret_pop = numeros.pop()
print(f'retorno do pop: {ret_pop}' )
#retorno do pop: 3

ret_pt = print(numeros)
#[1, 2]

print(f'o retorno do print {ret_pt }')
#o retorno do print None

#2
#sem retorno
def quadrado_do_7():
    print(7 * 7)
    #49
ret = quadrado_do_7()
print(f'retorno {ret}')
#retorno None

#3
# agora iremos refatorar(reescrever, redefinir) a função acima para que ela gere retorno
# usando a palavra 'return'.Não precisamos criar uma variável para receber o valor retornado.
# Podemos passar a execução das funções para outras funções.

def quadrado_do_7():
    return(7 * 7)

#criamos uma variável para receber a função.
ret = quadrado_do_7() # aqui precisamos de duas linhas para fazer o retorno.
print(f'retorno {ret}')
#retorno 49

print(f'retorno: {quadrado_do_7()}')# aqui precisamos de uma linha para fazer o retorno.
#retorno: 49

#4
#diferenca: com retorno e sem retorno

#4.1
sem retorno
def diz_oi():
    print('oi')
diz_oi()
#oi

#4.2
com retorno: aqui deve-se colocar um 'print' que é a variável que receberá o retorno.
def diz_oi():
    return('oi')
print(diz_oi())
#oi

#5
#com retorno + alguem. aqui, nota-se que o uso do return abre a possibilidade do uso do retorno em conjunto com
#outro dado, no caso, o nome.

def diz_oi():
    return('oi ')

alguem = ('Pedro!')

print(diz_oi( ) +  alguem)
# oi Pedro!

#6
#resumindo:
- 6.1 : o return finaliza a função, ou seja, ele sai da execução da função e nada pode ser executado após ele.
- 6.2 :podemos ter em uma funçao diferentes returns.
- 6.3 :podemos em uma função retornar qualquer tipo de dado e até msm múltiplos valores.

#exemplo 6.1:
#o que está após o 'return' não será impresso.
def diz_oi():
    return('oi ')
    print('Estou sendo executado depois do return.')
print(diz_oi())
#oi

#exemplo 6.2:
#podemos ter em uma funçao diferentes returns.
def nova_funcao():
    variavel = True
    if variavel:
        return(4)
    elif variavel is None:
        return (3)
    return('b')
print(nova_funcao())
#4

#exemplo 6.3:
# podemos, em uma função, retornar qualquer tipo de dado e até msm múltiplos valores.

def outra_funcao():
    return 2,3,4,5 # Aqui se gera uma tupla devido aos números separados por vírgula.
print(outra_funcao())
#(2, 3, 4, 5) Aqui temos uma tupla! Sabemos que não há necessidade de se colocar os números nas variáveis.

#exemplo 6.3.1:
def outra_funcao():
    return 2,3,4,5
num1, num2, num3, num4 = outra_funcao() # aqui estamos desempacotando os números das variáveis.
print(num1, num2, num3, num4)
# 2 3 4 5

#7
#criando função: função para jogar uma moeda
from random import random
def jogar_moeda():
    valor = random() # gera um número pseudo-randomico entre 0 e 1.
    if valor > 0.5:
        return "cara"
    return 'coroa'
print(jogar_moeda())

#8
(não deu certo!!)
#criando função: função para jogar papel, pedra e tesoura.
from random import random
def jogar_papel_pedra_tesoura():
    valor = random() # gera um número pseudo-randomico entre 0 e 1.
    if valor < 0.3:
        return "papel"
    if valor >= 0.3 or valor < 0.6:
        return 'pedra'
    if valor >= 0.6 or valor <=1:
        return 'tesoura'

print(jogar_papel_pedra_tesoura())
print(random())


#9
#criando função: função para jogar uma moeda
from random import random
def jogar_moeda():
    if random() > 0.5:
        return "cara"
    return 'coroa'
print(jogar_moeda())
# gera um número pseudo-randomico entre 0 e 1.

print(random())


"""





















