"""
Recebendo dados do usuário:

# Usando a versão antiga do python 2x
# Entrada de dados
print("Qual é o seu nome?")
nome = input()
print('Seja bem-vindo(a) %s' % nome)

print("Qual sua idade?")
idade = input()

# Processamento

#Saída
print('A %s tem %s anos'% (nome, idade))


# Usando a versão moderna do python 3x
# Entrada de dados
print("Qual é o seu nome?")
nome = input()
print('Seja bem-vindo(a) {0}'.format(nome))

print("Qual sua idade?")
idade = input()

# Processamento

# Saída
print('O {0} tem {1} anos'.format(nome, idade))


# Usando a versão atual do python 3x
# Entrada de dados
print("Qual é o seu nome?")
nome = input()
print(f'Seja bem-vindo(a) {nome}!')

print("Qual sua idade?")
idade = input()

# Processamento

# Saída
print(f'O {nome} tem {idade} anos! Ele nasceu em {2022 - int(idade)}!')

"""

# Usando a versão atual do python 3x
# Entrada de dados

nome = input("Qual é o seu nome?")
print(f'Seja bem-vindo(a) {nome}!')

idade = int(input("Qual sua idade?"))

# Processamento

# Saída
print(f'O {nome} tem {idade} anos! Ele nasceu em {2022 - idade}!')
