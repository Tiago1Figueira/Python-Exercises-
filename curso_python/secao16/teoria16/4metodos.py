"""
Método funções: representam o comportamento do objeto, ou seja, as açoes que ele pode fazer no seu sistema.
Há dois tipos: método de instância e método de classe.
Métodos são escritos em letra minúscula. Quando forem compostos, eles terão as letras divididas por underline.

1- Método de instância:
__init__ (dunder init) é um método especial que busca construir um objeto a partir da classe.

2- Método de classe:

class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrete:
    contador = 4999
    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrete.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrete.contador = self.__numero

class Produto:
    contador = 0
    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id
    def desconto(self, porcentagem):
        #retorna o valor do produto com desconto
        return (self.__valor * (100 - porcentagem)) / 100

class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
#1
p1 = Produto('playstation 4', 'video game', 2300)
print(p1.desconto(50))

#2
user1 = Usuario('Tiago' ,'Figueira', 'tiago@gmail.com', '123456')
user2 = Usuario('Figueira' ,'Figueira', 'figueira@gmail.com', '654321')

print(user1.nome_completo())# executand com o atributo
print(user2.nome_completo())# executand com o a classe.
print(Usuario.nome_completo(user1)) # executando com a classe

#3

nome = input('Informe o nome:')
sobrenome = input('Informe o sobrenome:')
email = input('Informe o email:')
senha = input('Informe a senha:')
confirme_senha = input('Confirme a senha:')
if senha == confirme_senha:
    user = Usuario(nome, sobrenome, email, senha )
else:
    print('Senha não confere!')
    exit(42)
print('Usuário criado com sucesso!')

senha = input('Informe a senha para acesso:')
if user.checar_senha(senha):
    print('Acesso permitido!')
else:
    print('Acesso negado!')
print(f'A senha user criptografada {user._Usuario__senha}')#acesso errado!
"""
class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrete:
    contador = 4999
    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrete.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrete.contador = self.__numero

class Produto:
    contador = 0
    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id
    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto."""
        return (self.__valor * (100 - porcentagem)) / 100

from passlib.hash import pbkdf2_sha256 as cryp
class Usuario:
    def __init__(self, nome, sobrenome, email, senha):#método de classe, pois está abaixo da classe.
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, round=200000, salt_size=16)#encrypt senha e os parâmetros round/salt_size (embaralhar e uni os nun da senha
    def nome_completo(self): #método de instancia, pois foca no dado de instancia(nome e sobrenome)
        return f'{self.__nome} {self.__sobrenome}'
    def checar_senha(self, senha):
        if cryp.verify(senha, self.__senha):#compara a senha digitada com a do banco de dados falando se é True ou False.
            return True
        return False
