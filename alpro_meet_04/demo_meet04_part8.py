# You can send any data types of argument to a function
# (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function

def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)
