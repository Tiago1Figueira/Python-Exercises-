"""
#1
for c in range(1000, 10000):
    w = str(c)
    x = w[0:2]
    y = w[2:]
    z = int(x) + int(y)
    if z ** 2 == c:
        print(c)

#2
for i in range(1000,10_000):
    a = str(i)
    b = a[0:2]
    c = a[2:]
    d = int(b) + int(c)
    if d ** 2 == i:
        print(i)
"""
#3
for i in range(1000,10_000):
    w = str(i)
    x = w[0:2]
    y = w[2:]
    z = int(x) + int(y)
    if z ** 2 == i:
        print(i)


