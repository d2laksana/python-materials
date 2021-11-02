def getBilanganBulat():
    bilangan = int(input("Input bilangan : "))

    # Panggil function cekGanjilGenap
    cekGanjilGenap(bilangan)


def cekGanjilGenap(bil):
    if bil % 2 == 0:
        print("Angka yang diinputkan yaitu:", bil, "adalah bilangan genap")
    else:
        print("Angka yang diinputkan yaitu:", bil, "adalah bilangan ganjil")


# TODO: Program start here
getBilanganBulat()
