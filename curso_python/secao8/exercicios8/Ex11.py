"""
#1
def media_notas(nota1, nota2, nota3, escolha):
    p1, p2, p3 = 5, 3, 2
    mediaaritimetica = (nota1 + nota2 + nota3) / 3
    mediaponderada = ((nota1 * p1) + (nota2 * p2) + (nota3 * p3)) / (p1 + p2 + p3)
    if escolha == "A" or escolha == "a":
        return f"a média aritmética das notas é: {mediaaritimetica}"
    elif escolha == "P" or escolha == "p":
        return f"a média ponderada é: {mediaponderada}"
    return f"Escolha inválida!! 'A' para média aritimética, 'P' para média ponderada"

a = int(input("Digite o valor da nota da P1"))
b = int(input("Digite o valor da nota da P2"))
c = int(input("DIgite o valor da nota da P3"))
d = input("Digite 'A' para calcular a média aritimética ou 'P' para média ponderada")
print(media_notas(a, b, c, d))

#2
def media_notas(nota1,nota2,nota3,escolha):
    p1,p2,p3 = 5,3,2
    media_aritmetica = (nota1 + nota2 + nota3) / 3
    media_ponderada = (nota1 * p1) + (nota2 * p2) + (nota3 * p2) / p1 + p2 + p3
    if escolha == 'A' or escolha == 'a':
        return f'A média aritmética das notas é {media_aritmetica}!'
    if escolha == 'P' or escolha == 'p':
        return f'A média ponderada das notas é {media_ponderada}!'
    return f'Nota inválida!! "A" para média aritmética ou "P" para média ponderada!! '

a = int(input('Digite o valor da nota da p1:'))
b = int(input('Digite o valor da nota da p2:'))
c = int(input('Digite o valor da nota da p3:'))
d = int(input('Escolha "a" para média aritmética e "p" para média aritmética:'))
print(media_notas(a,b,c,d))

#3
def calcula_media(opc,nota1,nota2,nota3):

    if opc == 'a' or opc == 'A':
        media_aritmetica = nota1 + nota2 + nota3 / 3
        return f'O valor da média aritmética para os números {nota1}, {nota2}, {nota3} é igual a {media_aritmetica:.2f}!'

    if opc == 'p' or opc == 'P':
        p1, p2, p3 = 5, 3, 2
        media_ponderada = (nota1 * p1) + (nota2 * p2) + (nota3 * p3) / p1 + p2 + p3
        return f'O valor da média ponderada para os números {nota1}, {nota2}, {nota3} é igual a {media_ponderada:.2f}!'
    else:
        return f'Letra inválida! "A" para média aritmética ou "P" para média ponderada!'

opc = input(f'Opções:\na- Média Aritmética\np- Média Ponderada\nLetra:')
x = float(input('Informe a 1ª nota:'))
y = float(input('Informe a 2ª nota:'))
z = float(input('Informe a 3ª nota:'))

print(calcula_media(opc,x,y,z))

#4
def media_notas(nota1,nota2,nota3,opc):
    p1,p2,p3 = 5, 3, 2
    if opc == 'A' or opc == 'a':
        media_aritmetica = (nota1 + nota2 + nota3) / 3
        return f'A média aritmética das suas notas é {media_aritmetica:.2f}!'
    if opc == 'P' or opc == 'p':
        media_ponderada = ((nota1 * p1) + (nota2 * p2) + (nota3 * p3)) / (p1 + p2 + p3)
        return f'A média ponderada das suas notas é {media_ponderada:.2f}'
    return f'Atenção: nota inválida!"A" para média aritmética ou "P" para média ponderada!'

a = float(input('Informe a 1ª nota: '))
b = float(input('Informe a 2ª nota: '))
c = float(input('Informe a 3ª nota: '))
opc = input('Opção: "A" para média aritmética ou "P" para média ponderada!Opção:')

print(media_notas(a,b,c,opc))

"""


