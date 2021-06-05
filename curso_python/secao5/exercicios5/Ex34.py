while True:
    print('=' * 50, 'CALCULO DA NOTA:', '=' * 50)
    faltas = int(input('Informe quantas faltas o aluno tem:'))
    nota = float(input('Informe a nota do aluno:'))
    if faltas < 20:
        if 9 <= nota <= 10:
            print(f'O conceito desse aluno é A!')
        elif 7.5 <= nota <= 8.9:
            print(f'O conceito desse aluno é B!')
        elif 5 <= nota <= 7.4:
            print(f'O conceito desse aluno é C!')
        elif 4 <= nota <= 4.9:
            print(f'O conceito desse aluno é D!')
        elif 0 <= nota <= 3.9:
            print(f'O conceito desse aluno é E!')
        else:
            print('Nota inválida!')

    if faltas > 20:
        if 9 <= nota <= 10:
            print(f'O conceito desse aluno é B!')
        elif 7.5 <= nota <= 8.9:
            print(f'O conceito desse aluno é C!')
        elif 5 <= nota <= 7.4:
            print(f'O conceito desse aluno é D!')
        elif 4 <= nota <= 4.9:
            print(f'O conceito desse aluno é E!')
        elif 0 <= nota <= 3.9:
            print(f'O conceito desse aluno é E!')
        else:
            print('Nota inválida!')
