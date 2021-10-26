# Short Hand If

a = 400
b = 330

if a > b:
    print("a is greater than b")


# Short Hand If ... Else
# a = 400
# b = 330

# print("A") if a > b else print("B")


# One line if else statement, with 3 conditions:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Nested -> bersarang
if a > b:
    print("A")
    if a == b:
        print("=")
    else:
        print("B")
else:
    if a == b:
        print("=")
    else:
        print("B")
