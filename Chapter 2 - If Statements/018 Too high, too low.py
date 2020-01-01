#018 too high, too low
num = int(input("Please enter a number between 10 and 20: "))

if num<=20 and num >=10:
    print("Correct")
elif num > 20:
    print("Too High")
elif num < 10:
    print("Too Low")
