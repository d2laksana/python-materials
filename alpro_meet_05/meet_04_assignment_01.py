def main():
    getPanjangLebar()


def getPanjangLebar():
    global panjang, lebar

    print("\n====== REKAP INPUTAN ======")
    print("Panjang :", panjang, "cm")
    print("Lebar :", lebar, "cm")

    luas = hitungLuasPP(panjang, lebar)
    # luas = 108.0
    tampilLuasPP(luas)


def hitungLuasPP(p, l):
    print("funct hitungLuas -> l =", l)
    return p * l


def tampilLuasPP(l):
    print("funct tampilLuas -> l =", l)
    print("\nLuas bangunan ini adalah", l, "cm2")


"""
Program start here
"""
panjang = float(input("Panjang : "))
lebar = float(input("Lebar : "))
# Call main function
main()
