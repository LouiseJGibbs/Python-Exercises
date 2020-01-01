#041 Repeat up to 10 times
name = input("What is your name? ")
num = int(input("How many times shall I display the name? "))

if(num>10):
    print("Too many times!!!")
else:
    for i in range(0,num):
        print(name)
        
