peso1 = 1
peso2 = 2
print('=' * 50, 'CÁLCULO MÉDIA PONDERADA!', '=' * 50)
while True:
    nota1 = float(input(f'Informe a 1ª nota de 0 a 100:'))
    nota2 = float(input(f'Informe a 2ª nota de 0 a 100:'))
    nota3 = float(input(f'Informe a 3ª nota de 0 a 100:'))
    media_ponderada = (nota1 * peso1 + nota2 * peso1 + nota3 * peso2) / (peso1 + peso1 + peso2)

    print(f'A média ponderada das notas é igual a {media_ponderada}!!')
    if media_ponderada >= 60:
        print('Aluno aprovado!')
        print('=' * 50, 'CÁLCULO MÉDIA PONDERADA!', '=' * 50)
    else:
        print('Aluno reprovado!')
        print('=' * 50, 'CÁLCULO MÉDIA PONDERADA!', '=' * 50)
        
nota1 = float(input(f'Informe a 1ª nota de 0 a 100:'))
nota2 = float(input(f'Informe a 2ª nota de 0 a 100:'))
nota3 = float(input(f'Informe a 3ª nota de 0 a 100:'))














