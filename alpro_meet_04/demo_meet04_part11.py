# subprograms
# function - it returns something
def getName():
    uName = input("Please enter your name : ")
    return uName

# subroutine - it doesn't need to return anything
# passing in the 'userName' parameter, as it will be used in this subroutine


def printMsg(userName):
    print("Hello", userName)


# Dijalankan dari sini
userName = getName()
# calling the function and adding an argument in the brackets
printMsg(userName)
