import random

# contoh Array
cars = ["Ford", "Volvo", "BMW"]

# index -> posisi item dalam array
# index dimulai dari 0
print("Banyak mobil :", len(cars), end='\n\n')

# Akses array dengan perulangan For
for x in cars:
    print(x)


# Menambah elemen baru
cars.append("Toyota")

print("\nArray baru:")
for x in cars:
    print(x)


# Menghapus elemen
cars.pop(1)
cars.pop(2)
print("\nArray setelah pop():")
for x in cars:
    print(x)

# Menghapus elemen dengan remove() -> case-sensitive
cars.remove("Ford")
print("\nArray setelah remove():")
for x in cars:
    print(x)


# Menambah elemen baru dengan input
newCar = str(input("\ninput new car : "))

# Add newCar to variable array
cars.append(newCar)

print("\nArray baru :")
for x in cars:
    print(x)
