#entradas
peso = float(input("Informe o peso:"))

#processamento
if (peso > 50):
    e = (peso - 50)
    m = (e * 4.00)
#saída 1
    print("Excesso: R${0}".format(e))
    print("Multa: R${0}".format(m))
else:
#saída 2
    e = 0
    m = 0
    print("Excesso: R${0} Multa: R${1}".format(e,m))



