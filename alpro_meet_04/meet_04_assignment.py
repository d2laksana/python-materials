def main():
    getDataNasabah()


def getDataNasabah():
    global saldo, bunga

    print("====== Data Nasabah ======")
    nama = str(input("Nama       : "))
    nomorRekening = str(input("No. Rek    : "))
    saldo = int(input("Saldo      : Rp "))

    # bunga = int(input("Suku bunga : "))
    inpBunga = str(input("Suku Bunga : "))
    bunga = int(inpBunga[:-1])

    print("Bunga yang diterima : Rp ", round(
        hitungBungaNetto(saldo, bunga), 2))


def hitungBungaBruto(saldo, bunga):
    return saldo * (1 / 365) * bunga


def hitungBungaNetto(saldo, bunga):
    bungaBruto = hitungBungaBruto(saldo, bunga)
    return bungaBruto - (bunga / 100) * bungaBruto


saldo = 0
bunga = 0.0

# Program start here
main()
