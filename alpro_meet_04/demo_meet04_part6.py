
# If the number of keyword arguments is unknown, add a double ** before the parameter name

def my_function(**kid):
    print("Jumlah yg dikirim :", len(kid))
    print("His middle name is " + kid["mname"])
    print("His age is " + str(kid["age"]))


my_function(fname="Tobias", mname="Alex", lname="Refsnes", age=21)
