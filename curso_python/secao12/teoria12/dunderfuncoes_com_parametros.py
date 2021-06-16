def soma_impares(*args):
    total = 0
    for num in args:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1,2,3,4,5,6,7,8,9,0,11]
print(soma_impares(lista))
