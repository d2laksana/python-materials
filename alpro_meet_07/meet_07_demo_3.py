''' Python Tuple '''

# myTuple = ("apple", "banana", "cherry")
myTuple = ("apple", 3.14, False, 3.14, "apple", False, 3.14)
print("Type ", type(myTuple))
print("My Tuple :", myTuple)

myTuple[1] = False

# Mencari lokasi indek dari elemen
print(myTuple.index("apple"))
