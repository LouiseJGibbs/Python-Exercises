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
    
