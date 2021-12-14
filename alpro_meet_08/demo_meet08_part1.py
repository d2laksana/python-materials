
pil = 0
'''                 0         1                 '''
makanan = [("Nasi Goreng", 16000),      # 0
           ("Mie Goreng", 18000),       # 1
           ("Mie Kuah", 18000),         # 2
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

nama = ""

while True:

    if(nama == ""):
        nama = input("Masukkan Nama Pemesan: ")

    print("******** APLIKASI KASIR ********")
    print("1. Pilih Makanan")
    print("2. Pilih Minuman")
    print("3. Lihat Pesanan")
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

            tuple_makan_pesan = (makanan[no_menu-1][0], jml_pesan_menu)
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

    elif pil == '0':
        print("******** KELUAR APLIKASI ********")
        print("Sampai jumpa....")
        break

    else:
        print("******** ERROR APLIKASI ********")
        print("Menu yang Anda pilih tidak ada....")
