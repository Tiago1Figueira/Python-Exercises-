"""
Escopo de variáveis (limites ou alcance das variáveis)

variáveis globais: alcançam todo o sistema.
variáveis locais: está limitada ao bloco no qual foi declarada.

Exemplo variável global
numero =42
print(numero)
print(type(numero))
42
<class 'int'>

Exemplo variável local : "A variável "novo" é um exemplo de variável específica para o bloco do 'if';
if (numero > 10):
    novo=numero + 10
    print(novo)


"""