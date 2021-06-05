#entrada
num1 = int(input("Informe o primeiro número:"))
num2 = int(input("Informe o segundo número:"))
num3 = int(input("Informe o terceiro número:"))
num4 = int(input("Informe o quarto número:"))

#processamento
q1 = num1 * num1
q2 = num2 * num2
q3 = num3 * num3
q4 = num4 * num4

if (q3 >= 100):
    print(q3)
#saída
print("num1 = {0} e q1 = {1}".format(num1, q1))
print("num2 = {0} e q2 = {1}".format(num2, q2))
print("num3 = {0} e q3 = {1}".format(num3, q3))
print("num4 = {0} e q4 = {1}".format(num4, q4))