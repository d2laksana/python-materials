'''
TODO: Program Klasifikasi Skor TOEFL ITP PBT
'''


def klasifikasiSkor():
    global listen, writen, reading

    # Perhitungan
    jumlah_skor = listen+writen+reading
    skor = jumlah_skor * 10
    skor_akhir = skor / 3
    print("\nSkor TOEFL =", skor_akhir)

    # Pesan
    if skor_akhir >= 310 and skor_akhir <= 420:
        print("Tingkat dasar (Elementary)")
    elif skor_akhir >= 421 and skor_akhir <= 480:
        print("Tingkat menengah bawah (low intermediet)")
    elif skor_akhir >= 481 and skor_akhir <= 520:
        print("Tingkat menengah atas (high intermediet)")
    elif skor_akhir >= 521 and skor_akhir <= 677:
        print("Tingkat mahir (advance)")


listen = int(input("Listening = "))
writen = int(input("Structure & Writen = "))
reading = int(input("Reading = "))

# Panggil function klasifikasiSkor
klasifikasiSkor()
