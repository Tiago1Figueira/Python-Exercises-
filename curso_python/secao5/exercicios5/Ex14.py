peso1 = 2
peso2 = 3
peso3 = 5
while True:
    print('=' * 75, 'CÁLCULO DA MÉDIA!', '=' * 75)
    laboratorio1 = float(input('Informe a nota laboratório de 0 a 10:'))
    semestral2 =   float(input('Informe a nota semestral de 0 a 10:'))
    exame_final3 = float(input('Informe a nota exame final de 0 a 10:'))
    media_ponderada = (laboratorio1 * peso1 + semestral2 * peso2 + exame_final3 * peso3) /(peso1 + peso2 + peso3)

    print(f'A média ponderada é {media_ponderada}!!')
    if media_ponderada <= 2.9:
        print('Aluno reprovado!')
    if media_ponderada >= 3 and media_ponderada <= 4.9:
        print('Aluno de recuperação!')
    if media_ponderada >= 5:
        print('Aluno aprovado!')

print('=' * 75, 'CÁLCULO DA MÉDIA!', '=' * 75)
laboratorio1 = float(input('Informe a nota laboratório de 0 a 10:'))
semestral2 =   float(input('Informe a nota semestral de 0 a 10:'))
exame_final3 = float(input('Informe a nota exame final de 0 a 10:'))


