"""
Uso da tabela verdade.

#1
'and' (no 'n > 1 and  n < 4' precisamos que a variável recebida seja verdadeira para o n > 1 e para o n < 4.
Usamos o "and" quando ambas as entradas precisarem ser verdadeiras.

#2
'or' ( no 'n > 1 or n < 4 ' precisamos que a variável recebida seja verdadeira para um dos 'Ns' .)
Usamos o "or" quando, pelo menos, uma das entradas for verdadeira. Caso ambas entradas sejam falsas o
processamento será negado.

#3
Usamos o "not" para inverter a variável. Assim, se o valor for "true" vira falso e vice-versa. O "not" nega
um valor.

#4
Usamos o "is" para comparar um valor de variável com outro.
ex.:
if num is True:
    print('O número está correto!')

#4
#entradas
ativo = true
logado = true
#processamento
if ativo and logado:
    print("Bem-vindo usuário!")
else:
    print("Vocẽ precisa ativar a sua conta. Cheque o seu email!!")

#4.1
#uso do not
ativo = True
logado = False
if not ativo:
    print("Vocẽ precisa ativar a sua conta. Cheque o seu email!!")
else:
    print("Bem-vindo usuário!")

#5
# veio do Python Console
nome = 'Geek'
dir(nome)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
 '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
 '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
 '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold',
 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map',
 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate',
 'upper', 'zfill']

#5.1
o nome tá todo em maiúsculo?
nome.isupper()
False

#5.2
a primeira letra do nome tá com maiúscula? Sim! Entao a resposta é True!
nome.istitle()
True

#5.3
nome.istitle() VS nome.title()

nome.istitle() Aqui checar se a primeira letra do nome está com capital letter.
True
nome.title() Aqui coloca a primeira letra do nome em capital letter.
'Geek'

#5.4
nome.title().istitle()
True

#5.5
Is pode se usado no lugar de ==
1==1
True

1 is 1
True

nome = 'Geek'
nome is 'Geek'

"""
