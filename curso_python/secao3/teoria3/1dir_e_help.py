"""

#PEP8 - PYTHON_ENHANCEMENT_PROPOSAL(guia de estilos ou padrão do código python)

propostas de melhoria do python - zen o python! usando o comando 'import this'!
Forma pytonica - a forma bonita ou visualmente agradável seguindo o ' The Zen of Python'!
#1
não gosta dos underlines debaixo de palavras em português? File/setting/editing/proofreading/spelling/conf_speelingmistakes/typo/

Forma pytonica - a forma bonita ou visualmente agradável seguindo o ' The Zen of Python'!
#1
não gosta dos underlines debaixo de palavras em português? File/setting/editing/proofreading/spelling/conf_speelingmistakes/typo/

dir vs help

python3
Python 3.8.5 (default, Sep 24 2020, 13:36:45)
[GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> "geek university"
'geek university'
>>> 'geek university'
'geek university'
>>> print("geek university")
geek university
>>> 4+5
9

O comando 'dir'!!!

# dir("geek") Com o 'dir' e uma string "geek" podemos acessar todos esses tipos de dados!
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
'__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count',
'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',
'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title',
'translate', 'upper', 'zfill']
'geek'.upper()
'GEEK'

'GEEK'.lower()
'geek'

'geek'.title()
'Geek'
Com o dir podemos acessar o tipo de dado ou variável. ex. 'GEEK'.lower, 'geek'.upper, 'geek'.title. Se nós não
soubermos como usar uma dessas ferramentas, daí então, usamos o comando help para explicar que elas fazem.
Digite help('geek'.lower) no terminal do python(nao do linux) para aprender o que essa propriedade faz.

Assim: terminal/python/help('geek'.lower). resposta:
   ' lower() method of builtins.str instance '
    'Return a copy of the string converted to lowercase. '
Pressione a letra 'q' para sair do terminal.
Em outras palavras o comando 'dir' acessa funçoes e o comando 'help' explica qqer uma das funções desejadas.


Agora comando dir com números e não com strings(letras em sequência)
dir(4)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__',
 '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__',
  '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__',
   '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__',
    '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__',
     '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__',
      '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__',
       '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__',
        '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__',
         '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio',
          'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag',
           'numerator', 'real', 'to_bytes']

#RECEBENDO DADOS

print('Qual é o seu nome?')
nome = input()
print('Qual é a sua idade?')
idade = input()
print('A %s tem %s anos'% (nome,idade) )         #forma antigo do python!
print('A {0} tem {1} anos.'.format(nome,idade)   #forma moderna do python!
print(f'A {nome} tem {idade} anos.')             #forma mais moderna do python!
#Qual é o seu nome?
#angelina
#Qual é a sua idade?
#46
#A angelina tem 46 anos

"""