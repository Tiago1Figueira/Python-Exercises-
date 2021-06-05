"""
#1
lista = [ ]
for i in range(1, 999 + 1):
    for j in range(1, 999 + 1):
        res = i * j
        res1 = str(res)
        res1 = res1[::-1]
        res1 = int(res1)
        if res1 == res:
            lista.append(res)
print(max(lista))

#2
lista = [ ]
for i in range(100, 1000):
    for j in range(100, 1000):
        w = i * j
        x = str(w)
        y = x[::-1]
        z = int(y)
        if z == w :
            lista.append(w)
print(max(lista))

#3
"""
lista = [ ]
for i in range(100, 1000):
    for j in range(100, 1000):
        w = i * j
        x = str(w)
        y = x[::-1]
        z = int(y)
        if z == w:
            lista.append(w)
print(max(lista))

















