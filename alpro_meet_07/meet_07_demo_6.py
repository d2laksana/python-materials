''' Python Breakpoint '''

cars = ["BMW", "Toyota", "Volvo", "Marcedes", "Honda"]

# Break
# for car in cars:
#     if car == "Volvo":
#         print("Volvo ditemukan")
#         break

#     print(car)

# Continue
# for car in cars:
#     print(car)
#     if car == "Volvo":
#         continue
#     print("Okee")

# for car in cars:
#     if car == "Volvo":
#         print("Volvo ditemukan")
#         break

#     print(car)
# else:
#     print("\nLoop selesai")


i = 0
while i < len(cars):
    i += 1
    if cars[i-1] == "Toyota":
        print("Toyota ada di indeks ke-", i-1)
        continue

    print(i-1)
else:
    print("Loop selesai")
