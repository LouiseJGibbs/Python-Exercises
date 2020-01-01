#012 Order 2 numbers
num1 = int(input("Please enter an number: "))
num2 = int(input("Please enter another number: "))

if num1>=num2:
    print(num1)
    print(num2)
else:
    print(num2)
    print(num1)
    
#013 Check less than 20
num = int(input("Please enter a number that is less than 20: "))

if num<=20:
    print("Thankyou")
else:
    print("Too High")

#014 Check between 10 and 20
num = int(input("Please enter a number between 10 and 20: "))

if num<=20 and num >=10:
    print("Thankyou")
else:
    print("Incorrect Answer")

#015 I like red
colour = input("What is your favourite colour? ")

if colour.lower() == "red":
    print("I like red too")
else:
    print("I don't like", colour.lower(), ", I prefer red")

#016 Check weather
raining = input("Is it raining? ")

if raining.lower() == "yes":
    windy = input("Is it windy? ")
    if windy == "yes":
        print("It is too windy for an umbrella")
    elif windy == "no":
        print("Take an umbrella")
    else:
        print("invalid answer")
elif raining.lower() == "no":
    print("Have a nice day")
else:
    print ("Invalid answer")

#017 age check
age = int(input("How old are you? "))

print("You can go trick or treating")

if age>=16:
    print("You can buy a lottery ticket")
if age>=17:
    print("You can drive")
if age>=18:
    print("You can vote")

#018 too high, too low
num = int(input("Please enter a number between 10 and 20: "))

if num<=20 and num >=10:
    print("Correct")
elif num > 20:
    print("Too High")
elif num < 10:
    print("Too Low")

#019 enter 1, 2 or 3
age = int(input("Enter 1, 2 or 3: "))

if age==1:
    print("Thank you")
elif age==2:
    print("Well done")
elif age==3:
    print("Correct")
else:
    print("Error Message")
    



    





