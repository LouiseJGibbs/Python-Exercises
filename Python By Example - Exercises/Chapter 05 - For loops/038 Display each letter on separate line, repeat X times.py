#038 Display each letter on separate line, repeat X times
name = input("What is your name? ")
num = int(input("How many times shall I display the name? "))

for i in range(0, num):
    for k in range(0, len(name)):
        print(name[k])
              
