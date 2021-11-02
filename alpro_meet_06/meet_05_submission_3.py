def getXdanY():
    global x, y
    x = int(input("X = "))
    y = int(input("Y = "))


def getKuadran(x, y):
    if x > 0 and y > 0:
        return "berada pada kuadran I"
    elif x < 0 and y > 0:
        return "berada pada kuadran II"
    elif x < 0 and y < 0:
        return "berada pada kuadran III"
    elif x > 0 and y < 0:
        return "berada pada kuadran IV"

    return "merupakan titik tengah"


def tampilInfo():
    global x, y
    print("Nilai X =", x)
    print("Nilai Y =", y)
    print("Koordinat(", x, ",", y, ")", getKuadran(x, y))


# TODO: Program start here
x = 0
y = 0

getXdanY()

tampilInfo()
