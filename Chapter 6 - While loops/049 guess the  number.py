#049 guess the number
compnum = 50
count = 1
guess = int(input("Guess the number: "))
while guess != compnum:
    if(guess>compnum):
        print("Too High")
    else:
        print("Too Low")
    count = count + 1
    guess = int(input("Guess the number: "))

print("You finally guessed it. It only took you "+ str(count) +" attempts")
