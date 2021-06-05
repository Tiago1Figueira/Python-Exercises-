#imc = indice de massa corporal
while True:
    print('='*150)
    peso = float(input('Informe o seu peso:'))
    altura = float(input('Informe a sua altura:'))
    imc = peso / (altura)**2
    if imc < 18.5:
        print(f'I.M.C = {imc:.2f} Abaixo do peso!')
    elif imc >= 18.5 and imc <= 24.9:
        print(f'I.M.C. = {imc:.2f} Saudável!')
    elif imc >= 25 and imc <= 29.9:
        print(f'I.M.C = {imc:.2f} Peso em excesso!')
    elif imc >= 30 and imc <= 34.9:
        print(f'I.M.C = {imc:.2f} Obesidade grau I!')
    elif imc >= 35 and imc <= 39.9:
        print(f'I.M.C = {imc:.2f} Obesidade grau II(severa)!')
    else:
        print(f'I.M.C = {imc:.2f} Obesidade grau III(mórbida)!')




