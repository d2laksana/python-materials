import datetime
import random
now = datetime.datetime.now()

pil = 0
makanan = [(16000, "Nasi Goreng"),
           ("Mie Goreng", 18000),
           ("Mie Kuah", 18000),
           ("Bihun Goreng", 17000),
           ("Bihun Kuah", 17000),
           ("Kwetiaw Goreng", 19000),
           ("Kwetiaw Siram", 19000),
           ("Capcay Goreng", 18000),
           ("Capcay Kuah", 18000)]

minuman = [("Air Mineral", 4000),
           ("Teh Panas", 4000),
           ("Es Teh", 4000),
           ("Es Jeruk", 4000),
           ("Jeruk Hangat", 4000),
           ("Es Jeruk Nipis", 6000),
           ("Jeruk Nipis Hangat", 6000)]

pesanan_makan = []
pesanan_minum = []

total = 0


def hitungTotalMakanan(order_list):
    global total
    for x in order_list:
        subtotal = int(x[1]) * int(x[2])
        print(x[0], "x", x[2], ":")
        print(subtotal)
        total = total + subtotal
        # for y in makanan:
        #     if (x[0] == y[0]):
        #         # subtotal = jml porsi * harga
        #         subtotal = int(x[1]) * int(y[1])
        #         print(x[0], "x", x[1], ":")
        #         print(subtotal)
        #         total = total + subtotal


def hitungTotalMinuman(order_list):
    global total
    for x in order_list:
        for y in minuman:
            if (x[0] == y[0]):
                subtotal = int(x[1]) * int(y[1])
                print(x[0], "x", x[1], ":")
                print(subtotal)
                total = total + subtotal


def reset():
    total = 0
    nama = ""
    pesanan_makan = []
    pesanan_minum = []


nama = ""

while True:

    if (nama == ""):
        nama = input("Masukkan Nama Pemesan: ")

    print("******** APLIKASI KASIR ********")
    print("1. Pilih Makanan")
    print("2. Pilih Minuman")
    print("3. Lihat Pesanan")
    print("4. Hitung Total dan Bayar")
    print("5. Auto generate order (random)")
    print("0. Keluar Aplikasi")
    pil = input("Masukkan pilihan anda:")

    if pil == '1':
        jawabOrderMakanLagi = "Y"
        while(jawabOrderMakanLagi == "Y" or jawabOrderMakanLagi == "y"):
            print("******** PILIH MAKANAN ********")
            no_urut_mkn = 1
            for x in makanan:
                print(no_urut_mkn, x)
                no_urut_mkn += 1

            print("Pilih no menu makanan yang Anda inginkan :")
            no_menu = int(input())

            print("Berapa porsi", makanan[no_menu-1]
                  [0], "yang Anda inginkan :")
            jml_pesan_menu = int(input())

            tuple_makan_pesan = (
                makanan[no_menu-1][0], makanan[no_menu-1][1], jml_pesan_menu)
            pesanan_makan.append(tuple_makan_pesan)
            print(jml_pesan_menu, "porsi", makanan[no_menu-1][0], "dicatat...")

            jawabOrderMakanLagi = input(
                "ingin memilih makanan lainnya? (Y/N) ")

    elif pil == '2':
        jawabOrderMinumLagi = "Y"
        while (jawabOrderMinumLagi == "Y" or jawabOrderMinumLagi == "y"):
            print("******** PILIH MINUMAN ********")
            no_urut_mnm = 1
            for x in minuman:
                print(no_urut_mnm, x)
                no_urut_mnm += 1

            print("Pilih no menu minuman yang Anda inginkan :")
            no_menu = int(input())

            print("Berapa porsi", minuman[no_menu - 1]
                  [0], "yang Anda inginkan :")
            jml_pesan_menu = int(input())

            tuple_minum_pesan = (minuman[no_menu - 1][0], jml_pesan_menu)
            pesanan_minum.append(tuple_minum_pesan)
            print(jml_pesan_menu, "porsi",
                  minuman[no_menu - 1][0], "dicatat...")

            jawabOrderMinumLagi = input(
                "ingin memilih minuman lainnya? (Y/N) ")

    elif pil == '3':
        print("Nama Pemesan :", nama)
        print("******** PESANAN MAKANAN ********")
        for x in pesanan_makan:
            print(x)

        print("******** PESANAN MINUMAN ********")
        for y in pesanan_minum:
            print(y)

    elif pil == '4':
        print("************* STRUK PESANAN *************")
        print("Nama Pemesan :", nama)
        print("\nTotal Makanan")
        hitungTotalMakanan(pesanan_makan)  # Daftar makanan dan jumlah porsi
        print("\nTotal Minuman")
        hitungTotalMinuman(pesanan_minum)
        print("*****************************************")
        print("Total Tagihan : Rp.", total)

        total_bayar = int(input("Nominal dibayarkan : Rp."))

        # KOndisi jika uang bayar kurang
        if total_bayar < total:
            print("Maaf, Uang Anda kurang!")
        else:
            print("Kembalian : Rp.", total_bayar-total)
            reset()

        print("*****************************************")
        print("dibuat pada:", now)

    elif pil == '5':
        print("************* AUTO GENERATE *************")
        random_jml_pesan_makan = random.randint(1, 5)
        random_jml_pesan_minum = random.randint(1, 5)

        for x in range(random_jml_pesan_makan):
            tuple_makan_pesan = (
                makanan[random.randint(0, 8)][0], random.randint(1, 3))
            pesanan_makan.append(tuple_makan_pesan)

        for x in range(random_jml_pesan_minum):
            tuple_minum_pesan = (
                minuman[random.randint(0, 6)][0], random.randint(1, 3))
            pesanan_minum.append(tuple_minum_pesan)

        print("Order berhasil digenerate random....")

    elif pil == '0':
        print("******** KELUAR APLIKASI ********")
        print("Sampai jumpa....")
        break

    else:
        print("******** ERROR APLIKASI ********")
        print("Menu yang Anda pilih tidak ada....")
