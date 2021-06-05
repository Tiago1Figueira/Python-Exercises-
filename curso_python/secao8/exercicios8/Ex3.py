"""
#1
def verifica(a):
     if a > 0:
         return f'1'
     if a < 0:
         return f'-1'
     if a == 0:
         return f'0'

print(verifica(0))

#2
def verifica(a):
    if a > 0:
        return 1
    if a < 0:
        return -1
    return 0
while True:
    num = float(input('Informe um número:'))
    print(verifica(num))

#3
def verifica(a):

   if a > 0:
        return 1
   if a == 0:
        return 0
   return -1
while True:
    valor = int(input('Informe um número:'))

    print(verifica(valor))
"""
#4

def valor(num):
    if num > 0:
        return '1'
    elif num < 0:
        return '-1'
    else:
        return '0'
while True:
    print('&'*100)
    num = int(input('Informe um número inteiro:'))
    print(valor(num))






























