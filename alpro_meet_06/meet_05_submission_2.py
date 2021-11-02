def getDataPetinju():
    nama = str(input("input nama petinju : "))
    usia = str(input("input usia petinju : "))
    tinggiBadan = float(input("input tinggi badan petinju : "))
    beratBadan = float(input("input berat badan petinju : "))
    kebangsaan = str(input("input kebangsaan petinju : "))

    # Cetak data petinju
    print("\n====== Data Petinju ======")
    print("Nama         :", nama)
    print("Usia         :", usia)
    print("Tinggi Badan :", tinggiBadan)
    print("Berat Badan  :", beratBadan)
    print("Kebangsaan   :", kebangsaan)

    # Panggil function tampilKelasPetinju
    tampilKelasPetinju(beratBadan)


def cekKelasPetinju(bb):
    if bb >= 41 and bb <= 54:
        return "Kelas Terbang"
    elif bb >= 55 and bb <= 59:
        return "Kelas Bulu"
    elif bb >= 60 and bb <= 66:
        return "Kelas Ringan"
    elif bb >= 67 and bb <= 77:
        return "Kelas Menengah"
    elif bb >= 78:
        return "Kelas Berat"

    return "Tidak masuk kualifikasi"


def tampilKelasPetinju(berat):
    # kelas = cekKelasPetinju(berat)
    print("Kelas Petinju	:", cekKelas(berat))


def cekKelas(bb):
    kelas = "Tidak masuk kualifikasi"
    if bb >= 41 and bb <= 54:
        kelas = "Kelas Terbang"
    elif bb >= 55 and bb <= 59:
        kelas = "Kelas Bulu"

    return kelas


# TODO: Program start here
getDataPetinju()
