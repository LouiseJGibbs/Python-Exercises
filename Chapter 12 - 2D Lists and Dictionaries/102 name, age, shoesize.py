#102 Name, Age, Shoe Size
d = {}

for i in range(1, 5):
    name = input("What is the name of person " + str(i) + "? ")
    age = int(input("How old is person " + str(i) + "? "))
    shoeSize= int(input("What is the shoe size of person " + str(i) + "? "))

    d[name] = {"age":age, "shoe size": shoeSize}

print(d)

name = input("Who would you like to see the details of? ")
if name in d:
    print(d[name])
else:
    print("Person not found")
    

