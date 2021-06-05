"""
Documentando uma função em docstring

Podemos ter acesso a documentação de uma função em Python utiliando a propriedade especial __doc__ .
Podemos ainda fazer acesso a documentação com a função help().

"""

def diz_oi():
    """ Uma função simples que retorna a string oi!"""
    return 'oi!'

def exponencial(numero, potencia=2):

    """

Função que retorna por padrão o quadrado de um número ou número a potência informada.
param número: números que desejamos geram um exponencial.
param exponencial: potência que queremos gerar o exponencial. Por padrão é o 2.
return: retorna o exponencial de um número por potência.
    """
#return numero ** potencia

