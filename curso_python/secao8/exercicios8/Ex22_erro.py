# exercćico copiado: refazer!
"""
#1
def excla(num):
    for x in range(1, num + 1):
        print('!' * x)

excla(int(input("Insira a quantidade de linhas\n")))

#2
def exclamacao(num):
    for i in range(1, num + 1):
        print("!" * i)

a = int(input('Informe a quantidade de linhas:'))

print(exclamacao(a))
"""

# não sei como tirar o print e colocar o return na linha 24 sem gerar problema no resultado!
# No resultado do print aparece a palavra none!
#3
def multiplica_exclamation(num):
    for i in range(1, num + 1):
        print(f'{"!" * i} ')
while True:
    print('=' * 150)
    a = int(input('Informe um número inteiro e positivo:'))
    print(multiplica_exclamation(a))



