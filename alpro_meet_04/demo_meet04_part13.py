# To assign values to global variables you have to use the keyword global

# Create a global variable.
number = 0
print("Number =", number)


def main():
    global number
    number = int(input('Enter a number: '))
    show_number()


def show_number():
    print('The number you entered is', number)


# Call the main function.
main()
