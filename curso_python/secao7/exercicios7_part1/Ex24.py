"""
#1
nAluno = []
alturaAluno = []
for c in range(0, 3):
    nAluno.append(int(input("Digite o número do aluno")))
    alturaAluno.append(int(input(f"Digite a altura do aluno {nAluno[c]}:")))
maxAltura = max(alturaAluno)
minAltura = min(alturaAluno)
indiceAlunoMax = alturaAluno.index(maxAltura)  # vendo o indice do maior aluno na lista das alturas dos aluno
indiceAlunoMin = alturaAluno.index(minAltura)  # vendo o indice do menor aluno na lista das alturas dos aluno
# já que as lista de numeros de alunos e altura de alunos tem o mesmo comprimento e alem disso
# o numero digitado para o aluno estara na mesma posição que a altura dele nas lista então é só acessa-la

print(f"O maior aluno é do aluno {nAluno[indiceAlunoMax]} com {maxAltura} de altura")
print(f"O menor aluno é o aluno {nAluno[indiceAlunoMin]} com {minAltura} de altura")

#2
num_aluno = []
altura_aluno = []
for i in range(1,4):#11
    num = int(input(f'Informe o número do {i}° aluno:'))
    num_aluno.append(num)

    altura = input(f'Informe a altura do {i}° aluno: ')
    altura_aluno.append(altura)

alturamax = max(altura)
alturamin = min(altura)
indice_alturamax = (altura.index(alturamax))
indice_alturamin = (altura.index(alturamin))

print( f'A maior altura é do aluno { altura.index(alturamax)} com {alturamax:.2f} de altura ')
print( f'A menor altura é do aluno { altura.index(alturamin)} com {alturamin} de altura ')
# checar por que a altura e o número dos alunos max e min não estão batendo.

#3
num_aluno = []
altura_aluno = []
for i in range(3):
    num = int(input(f'Informe o {i+1}/3 Número Aluno:'))

    altura = float(input(f'Informe a {i+1}/3 Altura Aluno:'))

    altura_aluno.append(altura)
    num_aluno.append(num)

    max(altura_aluno)
    min(altura_aluno)

    altura_aluno.index(max(altura_aluno))
    altura_aluno.index(min(altura))

print(f'O índice e altura máxima é {num_aluno.index(max(altura_aluno))} e o índice e altura mínima são'
      f'{num_aluno.index(min(altura_aluno))}')
# a altura e o índice não estão aparecendo. Erro ocorre na linha 58.

#4
numero_aluno = [ ]
altura_aluno = [ ]
while True:
    print('#'*100)
    for i in range(1,4):
        num = float(input(f'Informe o número do {i}° aluno:'))
        while num != int(num) or num <=0:
            print('Número inválido!')
            num = float(input(f'Informe o número do {i}° aluno:'))
        numero_aluno.append(num)
        altura = float(input(f'Informe a altura do {i}° aluno:'))
        altura_aluno.append(altura)
        print('='*80)

    altura_min = min(altura_aluno)
    altura_max = max(altura_aluno)

    ind_altura_min = altura_aluno.index(altura_min)
    ind_altura_max = altura_aluno.index(altura_max)

    print(f'Altura mínima {altura_min} Aluno {numero_aluno[ind_altura_min]}\n'
          f'Altura máxima {altura_max} Aluno {numero_aluno[ind_altura_max]}')

# o que fazer para evitar que o numero do aluno se repita?
"""
#5
numero_aluno = [ ]
altura_aluno = [ ]
while True:
    print('#'*50, 'DADOS DOS ALUNOS','#'*50)
    for i in range(1,11):
        num = float(input(f'Informe o número do {i}° aluno:'))
        while num != int(num) or num <= 0:
            print('Número inválido!')
            num = float(input(f'Informe o número do {i}° aluno:'))
        while int(num) in numero_aluno: # encaixei isso pra evitar a repetição do número_aluno. Dá certo na maioria das vezes! Há outra opção?
            if int(num) in numero_aluno:
                print('Número existente!')
                num = float(input(f'Informe o número do {i}° aluno:'))
        numero_aluno.append(num)
        altura = float(input(f'Informe a altura do {i}° aluno:'))
        altura_aluno.append(altura)
        print('='*80)
    altura_minima = min(altura_aluno)
    altura_maxima = max(altura_aluno)

    ind_altura_minima = altura_aluno.index(altura_minima)
    ind_altura_maxima = altura_aluno.index(altura_maxima)

    print('Resultado final')
    print(f'Número {numero_aluno[ind_altura_minima]} Altura Mínima {altura_minima}\n'
          f'Número {numero_aluno[ind_altura_maxima]} Altura Máxima {altura_maxima}\n')
    numero_aluno.clear()
    altura_aluno.clear()

































