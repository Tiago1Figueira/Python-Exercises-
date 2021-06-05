def volume_esfera(raio):
    v = 4/3 * 3.14 * raio ** 3
    return f' O volume desta esfera é {v}'

print(volume_esfera(3))
# a formula abaixo foi usada.
#return f"O volume da esfera é: {round(volume, 2)} m³"