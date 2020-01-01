#042 Add num to total if true
total = 0

for i in range(0, 5):
    num = int(input("Please enter a number: "))
    include = input("Include in total? yes or no ")

    while include != "yes" and include != "no":
            include = input("Invalid answer. Include in total? yes or no ")

    if input("Include in total? yes or no ") == "yes":
       total = total + num
       
    print(total)
