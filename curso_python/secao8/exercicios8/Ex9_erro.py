def calculo_cilindro_circular(altura,raio):
    volume = 3.14 * raio **2 * altura
    return f'O volume do cilindro circular é {volume:.2f}!'

altura = float(input('Informe a altura do cilindro circular:'))
raio = float(input('Informe o raio do cilindro circular:'))

print(calculo_cilindro_circular(altura,raio))
# acredito que haja um erro aqui.
# return f"O volume do cilindo é de {round(volume,2)} cm³ ou {round(volume,2)} ml"
