pil = 0
cars = ["Ford", "Volvo", "BMW"]

while True:
    print("\n******** APLIKASI SEDERHANA ********")
    print("1. Insert Data")
    print("2. Lihat Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("0. Keluar Aplikasi")
    pil = input("Masukkan pilihan anda:")

    if pil == '1':
        print("******** INSERT DATA ********")
        mobil_baru = input("Masukkan merek mobil baru :")
        cars.append(mobil_baru)
        print("Data mobil baru", mobil_baru, "berhasil di-insert-kan")

    elif pil == '2':
        print("******** LIHAT DATA ********")
        print("Data mobil yang tersimpan : ")
        for x in cars:
            print(x)

    elif pil == '3':
        print("******** UBAH DATA ********")
        index_mobil_ubah = input("Masukkan index mobil yang akan diubah :")

        mobil_baru_ubah = input("Masukkan merek mobil pengganti :")
        cars[int(index_mobil_ubah)] = mobil_baru_ubah
        print("Data mobil pengganti", mobil_baru_ubah, "berhasil di-insert-kan")

    elif pil == '4':
        print("******** HAPUS DATA ********")
        mobil_hapus = input("Masukkan merek mobil yang akan dihapus :")
        cars.remove(mobil_hapus)
        print("Data mobil lama", mobil_hapus, "berhasil dihapus")

    elif pil == '0':
        print("******** KELUAR APLIKASI ********")
        print("Sampai jumpa....")
        break

    else:
        print("******** ERROR APLIKASI ********")
        print("Menu yang Anda pilih tidak ada....")
