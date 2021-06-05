"""
#1
def somar_digitos(n):
    soma = 0
    if n > 0:
        while n != 0:
            soma += n % 10  #  retorna e soma os números depois da vírgula na divisão
            n //= 10  #  retira os números depois da vírgula na divisão
        return f"A soma dos algarismos é {soma}"
    return "Número inválido"

a = int(input("Digite um número"))
print(somar_digitos(a))

"""
#2
def soma_digitos(num):
    soma = 0
    if num > 0:
        for valor in num:
            soma += valor
        return f'A soma dos dígitos do número{num} é {soma}!'
    return ' Número inválido!'

a = int(input('Informe um número inteiro:'))
print(soma_digitos(a))
# está dando erro nas linhas 20 e 26.


