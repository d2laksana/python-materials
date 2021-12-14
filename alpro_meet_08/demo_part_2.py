import os
import math


makanan = [{"harga": 16000, "nama": "Nasi Goreng"},
           {"nama": "Mie Goreng", "harga": 18000},
           {"nama": "Mie Kuah", "harga": 18000},
           {"nama": "Bihun Goreng", "harga": 17000},
           {"nama": "Bihun Kuah", "harga": 17000},
           {"nama": "Kwetiaw Goreng", "harga": 19000},
           {"nama": "Kwetiaw Siram", "harga": 19000},
           {"nama": "Capcay Goreng", "harga": 18000},
           {"nama": "Capcay Kuah", "harga": 18000}]

minuman = [{"nama": "Air Mineral", "harga": 4000},
           {"nama": "Teh Panas", "harga": 4000},
           {"nama": "Es Teh", "harga": 4000},
           {"nama": "Es Jeruk", "harga": 4000},
           {"nama": "Jeruk Hangat", "harga": 4000},
           {"nama": "Es Jeruk Nipis", "harga": 6000},
           {"nama": "Jeruk Nipis Hangat", "harga": 6000}]


def showMenu():
    daftar_menu = """
    ******* Aplikasi Kasir *******
    1. Pilih Makanan
    2. Pilih Minuman
    3. Lihat Pesanan
    4. Pembayaran
    0. Keluar Aplikasi
    ______________________________
    """
    print(daftar_menu)


def showMakanan():
    global makanan

    print("******* Menu Makanan *******")
    indeks = 1
    for makan in makanan:
        print("%s. %s : %s" % (indeks, makan["nama"], makan["harga"]))
        indeks += 1
    print("______________________________\n")


def showMinuman():
    global minuman

    print("******* Menu Minuman *******")
    indeks = 1
    for minum in minuman:
        print("%s. %s : %s" % (indeks, minum["nama"], minum["harga"]))
        indeks += 1
    print("______________________________\n")


def showPesanan():
    global pesanan_makanan, pesanan_minuman, nama
    indeks = 1
    for makan in pesanan_makanan:
        print("%s. %s (%s) : %s" %(indeks, makan["nama"], makan["jumlah"], makan["harga"]))
        indeks += 1
    for minum in pesanan_minuman:
        print("%s. %s (%s) : %s" %(indeks, minum["nama"], minum["jumlah"], minum["harga"]))
        indeks += 1


def clear():
    os.system("cls")


pesanan_makanan = []
pesanan_minuman = []

nama = ""

while True:
    if(nama == ""):
        nama = input("Nama Pemesan: ")

    showMenu()
    pilih_menu = input("Masukkan pilihan Anda: ")

    clear()

    if pilih_menu == '1':
        orderMakananLagi = 'y'
        while (orderMakananLagi == 'y'):
            showMakanan()

            no_menu = int(input("Pilih nomor menu makanan: "))
            jml_porsi = int(input("Jumlah porsi %s: " %makanan[no_menu-1]["nama"]))

            pesan_makan = {"nama": makanan[no_menu-1]["nama"],
                           "harga": makanan[no_menu-1]["harga"],
                           "jumlah": jml_porsi}
            pesanan_makanan.append(pesan_makan)

            print("\n%s porsi %s dicatat." %(jml_porsi, makanan[no_menu-1]["nama"]))

            orderMakananLagi = input("\nTambah makanan lagi? [Y/N] ").lower()
        
        clear()
    elif pilih_menu == '2':
        orderMinumLagi = 'y'
        while (orderMinumLagi == 'y'):
            showMinuman()

            no_menu = int(input("Pilih nomor menu minuman: "))
            jml_porsi = int(input("Jumlah porsi %s: " %minuman[no_menu-1]["nama"]))

            pesan_minum = {"nama": minuman[no_menu-1]["nama"],
                           "harga": minuman[no_menu-1]["harga"],
                           "jumlah": jml_porsi}
            pesanan_minuman.append(pesan_minum)

            print("\n%s porsi %s dicatat." %(jml_porsi, minuman[no_menu-1]["nama"]))

            orderMinumLagi = input("\nTambah minuman lagi? [Y/N] ").lower()
        
        clear()
    elif pilih_menu == '3':
        print("******** Detail Pesanan ********")

        if pesanan_makanan != 0 or pesanan_minuman != 0:
            showPesanan()

        input("\nTekan Enter untuk kembali...")
        clear()
    elif pilih_menu == '0':
        clear()
        pesan = """
        ******* KELUAR APLIKASI *******
        Sampai jumpa...
        """
        print("******* KELUAR APLIKASI *******")
        print("Sampai jumpa...")
        break
