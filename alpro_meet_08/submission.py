import os
import sys

menu = 0
# Data Default
merk = ['HONDA', 'BMW', 'TESLA']

while True:
    print('\n##### List Menu','#'*5)
    print('1. Insert data merk mobil')
    print('2. Lihat data merk mobil')
    print('3. Ubah data merk mobil')
    print('4. Hapus data merk mobil')
    print('5. Hapus semua merk mobil')
    print('6. Mengurutkan data merk mobil')
    print('7. Keluar aplikasi')
    menu = int(input('Pilih Menu : '))
    if menu == 1:
        os.system('cls')
        print('#'*5,'INSERT MERK','#'*5)
        addMerk = input('Masukan merk yang ingin ditambahkan : ').upper()
        merk.append(addMerk)
        print('Data %s berhasil ditambahkan'%addMerk)
    elif menu == 2:
        os.system('cls')
        print('#'*5,'List Data Merk Mobil','#'*5)
        # print(merk,end='\n\n')
        for x in merk:
            print(x)
    elif menu == 3:
        os.system('cls')
        print('#'*5,'Ubah data Merk Mobil','#'*5)
        print('\nMerk mobil')
        for x in merk:
            print(x)
        merkLama = input('\nMasukan merk mobil yang akan diubah : ').upper()
        try:
            merk.index(merkLama)
            indexKe = merk.index(merkLama)
            merkBaru = input('Masukan merk baru : ').upper()
            merk[indexKe] = merkBaru
            print('Merk %s berhasil diubah menjadi'%merkLama ,merkBaru,end='\n\n')
        except:
            print("Merk mobil tidak ada!")
            print("Error", sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
    elif menu == 4:
        os.system('cls')
        print('#'*5,'Menghapus merk mobil','#'*5)
        print('\nMerk mobil')
        for x in merk:
            print(x)
        delMerk = input('\nMasukan merk mobil yang akan dihapus : ').upper()
        merk.remove(delMerk)
        print('\n data %s berhasil dihapus'%delMerk)
    elif menu == 5:
        os.system('cls')
        print('#'*5,'Menghapus semua merk','#'*5)
        print('\nMerk mobil')
        for x in merk:
            print(x)
        confirm = input('\nApakah anda yakin ingin menghapus semua data ? (y/n) : ').lower()
        if confirm == 'y':
            merk.clear()
            print("Data berhasil dihapus")
    elif menu == 6:
        os.system('cls')
        print('#'*5,'Mengurutkan data merk (A-Z)','#'*5)
        print('\nMerk mobil')
        for x in merk:
            print(x)
        merk.sort(reverse=True)
        print('\nData berhasil diurutkan')
        print('\nMerk mobil')
        for x in merk:
            print(x)
    elif menu == 7:
        os.system('cls')
        print('#'*5,'Keluar aplikasi','#'*5)
        print('Terima Kasih')
        print('See you soon....')
        break
    else:
        print('Mohon maaf, menu tidak tersedia..')
        print('silahkan pilih menu dibawah ini')