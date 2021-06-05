#entradas
sexo = input("Informe o sexo:m\f \n")
altura = float(input("Informe a altura:\n"))

#processamento
if sexo.lower () == 'm':
    peso_ideal = (72.7 * altura) - 58
    print("Seu peso ideal é {0:.2f}".format(peso_ideal))
elif sexo.lower () == 'f':
    peso_ideal = (62.1 * altura) - 44.7
    print("Seu peso ideal é {0:.2f}".format(peso_ideal))
else:
    print("Sexo não reconhecido! Informe m/f:")
