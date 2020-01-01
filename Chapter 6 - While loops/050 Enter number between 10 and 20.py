#050 Enter number between 10 and 20
num = int(input("Please enter a number between 10 and 20: "))
while num<=10 or num>=20:
    if num<=10:
        print("Too Low")
    else:
        print("Too High")
    num = int(input("Please enter a number between 10 and 20: "))
print("Thankyou")
