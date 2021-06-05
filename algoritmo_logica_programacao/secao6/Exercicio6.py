#variáveis
hora_normal = 10
hora_extra = 20
excesso = 0

#entrada
codigo = int(input("Informe o código:"))
numero = int(input("Informe o número de horas trabalhadas:"))

#processamento
if (numero > 50):
    excesso = (numero - 50) * hora_extra
    salario = (numero * hora_normal) + excesso
    print("O salário total é R${0}.".format(salario))
    print("O excesso é R${0}.".format(excesso))

else:
    salario = (numero * hora_normal)
    print("O salário total é {0} e o excesso é {1}!".format(salario, excesso))


