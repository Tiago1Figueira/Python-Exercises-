"""
#0
for horas in range(0,4):
    for minutos in range(1,55):
        for segundos in range(1,60):
            print(horas,minutos,segundos)
"""
#1
for a in range(1,3):                    #1_000_000_000
    for b in range(1, 3):               #1_000_000
        for c in range(1, 3):           #até 1000
            soma = (a*a) + (b*b)
            if c ** 2 == soma and a + b + c == 3:
                print(a,b,c)
#não entendi o propósito final desse esquema de loop for sobre loop for.






