''' Python List '''

myList = ["apple", "banana", "cherry", "apple", "orange"]
print("My list :", myList)
print("Length :", len(myList))
print("Type :", type(myList))

myList[0] = "melon"
print("\nNew list :", myList)

# Mengurutkan list
myList.sort(reverse=True)
print("\nSorted list :", myList)


# Tipe data lain
numbers = [1, 5, 3, 8, 6]
my_list = [True, True, False, True]

print("\nNumbers :", numbers)
print("My list :", my_list)

new_list = ["Apple", True, 3.14, 127, "okey"]
print("\nNew list :", new_list)
print("List at 2 :", new_list[2])

new_list.sort()
for x in new_list:
    print(x)
