#083 Check if upper case

s = input("Please enter a word: ")
while s.isupper() != True:
    print("This is not uppercase")
    s = input("Please enter a word: ")
    
print(s + " contains just uppercase letters")
