#variáveis
p = 0
i = 0
#entradas
numero = int(input("Informe um número:"))

#processamento
if (numero % 2 == 0):
    p = numero
else:
    i = numero

#saída
print("número par {0}".format(p))
print("número ímpar {0}".format(i))

