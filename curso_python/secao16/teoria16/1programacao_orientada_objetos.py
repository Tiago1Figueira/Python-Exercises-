"""
Programação orientada a objetos (Poo)

Poo: é um paradigma de programação que utiliza o mapeamento de objetos do mundo real para
modelos computacionais.

Paradigma de programação: é a forma/metodologia utilizada para pensar/desenvolver sistemas.

Principais elementos da orientação a objetos:
-classe: modelo de objeto do mundo real sendo representado computacionalmente.
-atributo: caracteristicas do objeto.
-método : comportamento do objeto(funçoes); são funçoes, dados com parenteses, que estão localizadas em uma
classe.
- construtor: metodo especial utilizado para criar objetos.
- objeto: instancia da classe.
"""
numero = 10
print(numero)
print(type(numero))

nome = 'geek'
print(nome)
print(type(nome))

class Produto:
    pass
ps4 = Produto()
print(ps4)
print(type(ps4))

"""
10
<class 'int'>

geek
<class 'str'>

<__main__.Produto object at 0x7f0a49a10070>
<class '__main__.Produto'>
Para a palavra ps4(playstation4) não há classe, ou seja, não há int, 'str', float. 
Assim devemos criá-la como ocorre aqui com a criação da classe produto. Logo, temos um outro tipo de dado
chamado produto, como são os outros int, 'str', float .... Qual é o tipo de dado? É da classe produto, int,
float.....
 
"""