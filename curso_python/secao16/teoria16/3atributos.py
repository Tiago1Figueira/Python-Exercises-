"""
Atributos: representam as caracteristicas de um objeto. Pelos atributos representamos os estados de um objeto do mundo
real computacionalmente.
Ex.: lampada(objeto) - atributos: azul, verde, vermelha(cor), acesa ou apagada(estado), pequena ou grande(tamanho)

Criterios: Publicos ou privado ?
A-privado: só pode ser acessado dentro da própria classe que o criou. Utiliza-se __ (duplo underscore) para que fique
privado.
B-público: em python, por conversao todo atributo e considerado como publico, ou seja, pode ser acessado em qqer parte
do projeto.
naming mangling: e o acesso a dados privados como se fossem publicos. e.g._Lampada__voltagem (nome da classe e do
atributo)

1-atributos de instancia: são aqueles declarados dentro de um método construtor. Método construtor: metodo especial
utilizado para construir objetos. Instancia e um objeto da classe e.g. voltagem e um objeto da classe Lampada. Em um
atributo de instancia/objeto de uma classe, todas as instancias terao estes atributos.

# aqui e atributo privado ja que tem __underscore!
class Lampada:
    def __init__(self, voltagem, cor): #(__init__ é chamado de metodo construtor.'self' é o proprio objeto ou Lampada.)
        self.__voltagem = voltagem#(atributos de instancia sao declarados dentro do método construtor:voltagem,cor,ligada!)
        self.__cor = cor #(o objeto Lampada no atributo cor receberá cor)
        self.__ligada = False

#aqui e atributo publico ja que nao tem __ underscore!!
class ContaCorrente:
    def__init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

2-atributos de classe:
Se parecem o a variavel global. Sao atributos que sao declarados diretamente na classe, fora do construtor. Geralmente
ja inicializamos com um valor e este valor e compartilhado em todas as instancias da classe, ou seja, ao inves de cada
instancia de classe ter seus proprios valores, como e o caso dos atributos de instancia, com os atributos de classe
todas as instancias terao o mesmo valor para este atributo.

No exemplo abaixo, o atributo 'imposto' é o atributo de classe, já que é usado para todos os atributos de instancia.

class Produto:
# atributo de classe:
    imposto = 1.05  #0.05% de imposto

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor =(valor * Produto.imposto)

p1 = Produto('PlayStation 4', 'video game', 2300)
p2 = Produto('Xbox', 'video game', 4500) #p1 e p2 sao (instancias)
print(p1.valor)# acesso possivel mas incorreto a um atributo de classe.
print(p2.valor)# acesso possivel mas incorreto a um atributo de classe.

#obs.: não precisamos criar uma instancia de uma classe para fazer acesso a um atributo de classe.
print(Produto.imposto) #acesso correto de um atributo de classe.

#print
#2415.0
#4725.0
#1.05

3-atributos dinamicos 1h10min
Um atributo de instância que pode ser criado no momento da execução, ou seja, qdo se está criando o código.
O atributo dinâmico será exclusivo da instância que o criou. Esse atributo não é comum, já que a declaração de
atributos acontece qdo se está fazendo atributos de instância. Ou seja, atributos de instância e atributos de classe.
__dict__ = dictionary : esse código mostra toda a estrutura ligada a um objeto:atributos de instancia e dinâmicos. Mostra
a informação como se fosse um dicionario
e.g.: print(p2.__dict__) imprime toda a estrutura do objeto produto 2.

"""

class Produto:
# atributo de classe:
    imposto = 1.05  #0.05% de imposto

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor =(valor * Produto.imposto)

p1 = Produto('PlayStation 4', 'video game', 2300)

p2 = Produto('arroz', 'mercearia', 5.99) #p1 e p2 sao (instancias)
p2.peso = '5kg' #Aqui temos um atributo dinâmico. Note que na classe produto não foi criado o atributo peso!

print(f'produto: {p2.nome}\ndescrição: {p2.descricao}\nvalor: {p2.valor}\npeso: {p2.peso}')

# deletando atributos dinâmicos dinamicamente:
print(p1.__dict__)
print(p2.__dict__)

del p2.peso # deletou atributo peso de p2.(atributo dinamico)
del p2.valor # deletou atributo valor de p2. (atributo de instância)
print(p1.__dict__)
print(p2.__dict__)


