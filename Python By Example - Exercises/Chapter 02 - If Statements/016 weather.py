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
        
    
