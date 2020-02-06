#104 Remove someone
d = {}

for i in range(1, 5):
    name = input("What is the name of person " + str(i) + "? ").strip()
    age = int(input("How old is person " + str(i) + "? "))
    shoeSize= int(input("What is the shoe size of person " + str(i) + "? "))

    d[name] = {"age":age, "shoe size": shoeSize}

print(d)

name = input("Who would you like to remove? ")
if name in d:
    if input("Remove this record (Y/N): " + name + ": " +str(d[name])).lower() == "y":
        del d[name]
else:
    print("Person not found")

print("New Dictionary: ")
for name in d:
    print(name +  ": " + str(d[name]))
