def main():
    getDataNasabah()


def getDataNasabah():
    nama = str(input("Nama       : "))
    nomorRekening = str(input("No. Rek    : "))
    saldo = int(input("Saldo      : "))
    bunga = int(input("Suku Bunga : "))

    print("====== Data Nasabah ======")
    print("Nama       :", nama)
    print("No. Rek    :", nomorRekening)
    print("Saldo      : Rp", saldo)
    print("Suku Bunga :", bunga, "%")

    bungaNetto = round(hitungBungaNetto(saldo, bunga), 2)
    print("Bunga yang diterima : Rp", bungaNetto, end="\n\n")


def hitungBungaBruto(saldo, bunga):
    return saldo * (1 / 365) * bunga


def hitungBungaNetto(saldo, bunga):
    bungaBruto = hitungBungaBruto(saldo, bunga)
    return bungaBruto - (bunga / 100) * bungaBruto


"""
Program start here
"""
# Call main function
main()
