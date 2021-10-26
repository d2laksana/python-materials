# If the number of arguments is unknown, add a * before the parameter name

def my_function(*kids):
    print("Jumlah parameter yg dikirim :", len(kids))
    print("The first " + kids[0])


# Emil -> index 0
# Tobias -> index 1
# Linus -> index 2
my_function("Emil", "Tobias", "Linus")
