# scope - global and local

fname = "Pat"
lname = "Cummins"

def greet():
    fname = "Steven"
    lname = "Smith"
    print("Inside the function")
    print(fname)
    print(lname)

greet()

print("Outside the function")
print(fname)
print(lname)
