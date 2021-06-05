"""
definindo funções:
- partes do código que realizam funções específicas;
- fazem funções semelhantes e repetitivas;

exemplos
print()
append()
max()
min()

#1
funções estão baseadas no princípio 'DRY':
DRY - (dont repeat yourself - não faça você mesmo ou não repita vc msm!)

#2
#Definindo uma função
A forma geral de se definir uma função em python é:

def nome_da_função(parametros_de_entrada):
    blocos_da_função

nos quais:
nome_da_função : minusculo e separado por underline.
parâmetro_de_entrada:  opcionais e tendo mais de 1 são separados por vírgula.
bloco_da_função: é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno.

#2.1
obs.: para definir uma função usamos a palavra 'def' informando ao python que estamos definindo uma função.
Dois pontos(:) são usados para abrir ou iniciar um outro bloco.

def nome_da_função(parametros_de_entrada):
    blocos_da_função

#3
definindo(criando) uma função:

def diz_oi!():
    print(oi!)

obs.:
- dentro das nossas funções podemos utilizar outras funções;
- a função só faz uma tarefa; somente diz oi ;
- a função não recebe nenhum parâmetro de entrada;
- a função não retorna qualquer coisa;

#3.1
# para se utilizar essa função precisa-se fazer a chamada da execução:
diz_oi

,ou seja,

def diz_oi():
    print('oi')
diz_oi()
# oi

#4
Atenção:
certo
' diz_oi() '

errado
'diz_oi' # sem o parênteses.
'diz_oi ()# com espaço.

#5
def cantar_parabens():
    print('Parabens pra vc')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
cantar_parabens()

#6
# iterando com a função recem-criada.
def cantar_parabens():
    print('Parabens pra vc')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')

for i in range(5):
   cantar_parabens()

#Parabens pra vc
#Nesta data querida     5x
#Muitas felicidades
#Muitos anos de vida

#7
# é possível:
# iterando com a função recem-criada.

def cantar_parabens():
    print('Parabens pra vc')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')

canta = cantar_parabens
canta()
#Parabens pra vc
#Nesta data querida
#Muitas felicidades
#Muitos anos de vida

"""
