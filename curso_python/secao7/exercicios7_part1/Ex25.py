"""
#Lembre-se: para identificar se alguma posição possui o número que vc procura passe-a para 'string' e coloque aspas no número!
#0
vetor = []
n = 0
while len(vetor) != 100:
    i = str(n)
    if n%7 == 0:
        vetor.append(n)
    elif i[-1:] == '7':
        i = int(i)
        vetor.append(i)
    n += 1
print(vetor)

#1
vetor = []
i = 0
while len(vetor) != 100:
    if not(i % 7 == 0) or ('7' not in str(i)[-1]):
        vetor.append(i)
    i += 1
print(vetor)

#2
vet = [ ]
for i in range(1, 101):
    if not i % 7 == 0:
        vet.append(i)

print(vet)
# não consegui achar um código pra números terminados em 7.

#3
vetor = [ ]
vetor1 = [ ]
for i in range(1,101):
    if i % 7 != 0:
        vetor.append(i)
for i in vetor:
    x = str(i)
    if x[-1] != 7:
        vetor1.append(i)
print(f'Lista 1 a 100 sem divisores de 7 ou terminados em 7 {vetor1}! ')

#3.1
vetor = [ ]
vetor1 = [ ]
for i in range(1,101):
    if i % 7 != 0:
        vetor.append(i)
for i in vetor:
    if str(i)[-1] != 7:
        i = int(i)
        vetor1.append(i)
print(f'Lista 1 a 100 sem divisores de 7 ou terminados em 7 {vetor1}! ')

#4
vetor = [ ]
for i in range(1,101):
    if i % 7 != 0 and str(i)[-1] != '7':
        vetor.append(i)
print(f'Lista 1 a 100 sem divisores de 7 ou terminados em 7 {vetor}! ')
#Lembre-se: para identificar se alguma posição possui o número que vc procura passe-a para 'string' e coloque aspas no número!
"""
#5
vetor = [ ]
for i in range(1,130):
    if i % 7 != 0 and str(i)[-1] != '7':
        vetor.append(i)#só entra aqui quem não for qqer das duas coisas(and): divisível por 7 or com o n° 7 no fim.

print(len(vetor)) #100 primeiros números sem a influencia do número 7.
print(vetor)


























