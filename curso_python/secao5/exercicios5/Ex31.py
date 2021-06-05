while True:
    altura = float(input('Informe a altura:'))
    peso = float(input('Informe o peso:'))

    if peso < 60 and altura < 1.20:
        print("A")
    elif peso < 60 and altura >= 1.20 and altura <= 1.70:
        print("B")
    elif peso < 60 and altura > 1.70:
        print("C")

    elif peso >= 60 and peso <= 90 and altura < 1.20:
        print("D")
    elif peso >= 60 and peso <= 90 and altura >= 1.20 and altura <= 1.70:
        print("E")
    elif peso >= 60 and peso <= 90 and altura > 1.70:
        print("F")

    elif peso > 90 and altura < 1.20:
        print("G")
    elif peso > 90 and altura >= 1.20 and altura <= 1.70:
        print("H")
    elif peso > 90 and altura > 1.70:
        print("I")

