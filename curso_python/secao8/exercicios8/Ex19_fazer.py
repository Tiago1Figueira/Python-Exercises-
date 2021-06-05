
def maior_fator_primo(numero):
    if numero >  - 2 and numero < 2: #(-1,0,1,)
        return 'Não é possível decompor o número em fatores primos!'
    num = numero
    fator_primo = 2
    while numero != 1 and numero != -1:
        if numero % fator_primo == 0:
            numero = numero / fator_primo
        else:
            fator_primo = fator_primo + 1
    return f'O maior fator primo de {num} é {fator_primo}'

print(maior_fator_primo(32))


"""
def maior_fator_primo(numero):
    if numero < 2:
        return 'Não é possível decompor o número em fatores primos!'
    num = numero
    fator_primo = 2
    while numero != 1 and numero != -1:
        if numero % fator_primo == 0:
            numero = numero / fator_primo
        else:
            fator_primo = fator_primo + 1

"""








