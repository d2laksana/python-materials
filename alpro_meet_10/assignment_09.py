import datetime
import random
from colorama import init, Fore, Back, Style

init(convert=True)
pil = 0

makanan = [("Nasi Goreng", 16000),
           ("Mie Goreng", 18000),
           ("Mie Kuah", 18000),
           ("Bihun Goreng", 17000),
           ("Bihun Kuah", 17000),
           ("Kwetiaw Goreng", 19000),
           ("Kwetiaw Siram", 19000),
           ("Capcay Goreng", 18000),
           ("Capcay Kuah", 18000)]

minuman = [("Air Mineral", 4000), # 0
           ("Teh Panas", 4000), # 1
           ("Es Teh", 4000),
           ("Es Jeruk", 4000),
           ("Jeruk Hangat", 4000),
           ("Es Jeruk Nipis", 6000),
           ("Jeruk Nipis Hangat", 6000)]

pesanan_makan = []
pesanan_minum = []

nama = ""


def hitungTotalMakanan(order_list):
    total = 0
    print("Total Makanan")
    for pesanan in order_list:
        print(f"{pesanan[0]} x {pesanan[1]} : ")  # menampilkan nama dan jumlah
        for menu in makanan:
            if menu[0] == pesanan[0]:
                # menampilkan total harga
                print("{:,}".format((pesanan[1] * menu[1])))
                total += pesanan[1] * menu[1]
    return total


def hitungTotalMinuman(order_list):
    total = 0
    print("Total Minuman")
    for pesanan in order_list:
        print(f"{pesanan[0]} x {pesanan[1]} : ")  # menampilkan nama dan jumlah
        for menu in minuman:
            if menu[0] == pesanan[0]:
                # menampilkan total harga
                print("{:,}".format((pesanan[1] * menu[1])))
                total += pesanan[1] * menu[1]
    return total


while True:
    if(nama == ""):
        nama = input("Masukkan Nama Pemesan: ")

    print("******** APLIKASI KASIR ********")
    print("1. Pilih Makanan")
    print("2. Pilih Minuman")
    print("3. Lihat Pesanan")
    print("4. Tagihan dan Pembayaran")
    print("5. Auto Generate Order")

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

            print("Berapa porsi", makanan[no_menu-1][0], "yang Anda inginkan :")
            jml_pesan_menu = int(input())

            tuple_makan_pesan = (makanan[no_menu-1][0], jml_pesan_menu)
            pesanan_makan.append(tuple_makan_pesan)
            print(jml_pesan_menu, "porsi", makanan[no_menu-1][0], "dicatat...")

            jawabOrderMakanLagi = input("ingin memilih makanan lainnya? (Y/N) ")
    
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

            print("Berapa porsi", minuman[no_menu - 1][0], "yang Anda inginkan :")
            jml_pesan_menu = int(input())

            tuple_minum_pesan = (minuman[no_menu - 1][0], jml_pesan_menu)
            pesanan_minum.append(tuple_minum_pesan)
            print(jml_pesan_menu, "porsi", minuman[no_menu - 1][0], "dicatat...")

            jawabOrderMinumLagi = input("ingin memilih minuman lainnya? (Y/N) ")
    
    elif pil == '3':
        print("Nama Pemesan :", Fore.CYAN + nama + Style.RESET_ALL)
        print("******** PESANAN MAKANAN ********")
        for x in pesanan_makan:
            print(x[0],"x", x[1])
        
        print("******** PESANAN MINUMAN ********")
        for y in pesanan_minum:
            print(y[0],"x", y[1])
    
    elif pil == '4':
        print("******** STRUK PESANAN ********")
        print("Nama Pemesan :",Fore.CYAN + nama + Style.RESET_ALL, end='\n\n')
        # Menghitung total tagihan
        total_makanan = hitungTotalMakanan(pesanan_makan)
        print("")
        total_minuman = hitungTotalMinuman(pesanan_minum)
        print("*"*32)
        print("Total Tagihan : Rp. {:,}".format((total_makanan + total_minuman)))

        nominal_dibayarkan = int(input("Nominal dibayarkan : Rp. "))
        while nominal_dibayarkan < (total_makanan + total_minuman):
            print(Fore.YELLOW + "Nominal yang anda bayarkan kurang",str((total_makanan + total_minuman) - nominal_dibayarkan) + Style.RESET_ALL)
            nominal_dibayarkan = int(input("Masukkan Nominal dibayarkan Lagi : Rp. "))
        
        print("Kembalian : Rp. {:,}".format(nominal_dibayarkan - (total_makanan + total_minuman)))
        print("*"*32)
        print("dibuat pada : ",Fore.YELLOW + str(datetime.datetime.now()) + Style.RESET_ALL)
        
        pesanan_makan = []
        pesanan_minum = []
        pesan_lagi = input("Apakah anda ingin memesan lagi ? (y/n) : ")
        if pesan_lagi == 'n' or pesan_lagi == 'N':
            nama = ""
            print(Fore.YELLOW + "******** KELUAR APLIKASI ********")
            print("Sampai jumpa....")
            break
    
    elif pil == '5':
        print("******** AUTO GENERATE ORDER ********")
        print(Fore.GREEN + ' Aplikasi berhasil generate order Anda ' + Style.RESET_ALL)
        
        # Makanan
        i = 0
        while i < random.randint(1,5):
            # Acak dari 0-8 -> 0
            # pesanan_makan.append([makanan[random.randint(0, len(makanan) - 1)][0], random.randint(1,3)])
            # pesanan = (makanan[random.randint(0, len(makanan) - 1)]["nama"],  random.randint(1,3))
            pesanan = {"nama": makanan[random.randint(0, len(makanan) - 1)]["nama"],
                       "harga": makanan[random.randint(0, len(makanan) - 1)]["harga"],
                       "porsi": random.randint(1,3)}
            pesanan_makan.append(pesanan)
            i+=1
        
        # Minuman
        i = 0
        while i < random.randint(1,5):
            pesanan_minum.append([minuman[random.randint(0, len(minuman) - 1)][0], random.randint(1,3)])
            i+=1

    elif pil == '0':
        nama = ""
        print(Fore.YELLOW + "******** KELUAR APLIKASI ********")
        print("Sampai jumpa....")
        break
    
    else:
        print("******** ERROR APLIKASI ********")
        print("Menu yang Anda pilih tidak ada....")