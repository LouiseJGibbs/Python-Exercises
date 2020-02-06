
#035 Display name 3 times
name = input("What is your name? ")
for i in range(0,3):
    print(name)

#036 Display name X times
name = input("What is your name? ")
num = int(input("How many times shall I display the name? "))

for i in range(0,num):
    print(name)

#037 Display each letter on separate line
name = input("What is your name? ")

for i in range(0, len(name)):
    print(name[i])

#038 Display each letter on separate line, repeat X times
name = input("What is your name? ")
num = int(input("How many times shall I display the name? "))

for i in range(0, num):
    for k in range(0, len(name)):
        print(name[k])

#039 Times table
num = int(input("Please enter a number: "))

for i in range(0,11):
    print(num*i)

#040 Count down
num = 999

while(num>50):
    num = int(input("Please enter a number less than 50: "))

for i in range(num,0, -1):
    print(i)

#041 Repeat up to 10 times
name = input("What is your name? ")
num = int(input("How many times shall I display the name? "))

if(num>10):
    print("Too many times!!!")
else:
    for i in range(0,num):
        print(name)

#042 Add num to total if true
total = 0

for i in range(0, 5):
    num = int(input("Please enter a number: "))
    include = input("Include in total? yes or no ")

    while include != "yes" and include != "no":
            include = input("Invalid answer. Include in total? yes or no ")

    if include == "yes":
       total = total + num
       
    print(total)

#043 Count up or down

direction = input("Would you like to count up or down: ")

while direction != "up" and direction != "down":
    direction = input("Invalid answer. Please type 'up' or 'down': ")
    
if direction == "up":
    num = int(input("Please enter a number: "))
    for i in range(1,num + 1):
        print(i)
else:
    num = int(input("Please enter a number less than 20: "))
    while num > 20:
        num = int(input("Invalid answer, please enter a number less than 20: "))
    for i in range(num,0,-1):
        print(i)
    
#044 Invitation list

count = int(input("How many people will you invite to the party: "))

if count<=10:
    for i in range(1,count + 1):
        name = input("What is the name of guest " + str(i) + "? ")
        print(name, "has been invited")
else:
    print("Too many people, party cancelled")
    



              

