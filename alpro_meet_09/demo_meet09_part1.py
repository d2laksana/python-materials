import random
from colorama import Fore, Back, Style

min = 1
max = 4

lagi = 'Y'
while(lagi == 'Y' or lagi == 'y'):
    aku = int(input("masukkan angka tebakan Anda : "))
    x = random.randint(min, max)

    if aku == x:
        print(Fore.GREEN + "Tebakan benar, Anda menang!!" + Style.RESET_ALL)
        break
    else:
        print(Fore.RED + "Tebakan salah!" + Style.RESET_ALL)
        print("Angka hasil random adalah",
              x, ", angka tebakan anda", aku)
        lagi = input("Coba lagi? (Y/N)")

    print(Style.RESET_ALL)
