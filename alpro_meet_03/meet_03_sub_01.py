# deklarasi vaariabel
p = 0
l = 0
r = 0
t = 0
a = 0
phi = 3.14

# input
p = int(input("input panjang : "))
l = int(input("iput lebar : "))
r = int(input("input jari jari : "))
a = int(input("input alas : "))
t = int(input("input tinggi : "))

# hitung Luas
luas = (p * l) + (0.5 * phi * r * r) + (0.5 * a * t)
# result
print("Panjang =", p)
print("Lebar =", l)
print("Jari-jari =", r)
print("ALas =", a)
print("Tinggi =", t, end='\n\n')
print("Luas Total =", luas)
