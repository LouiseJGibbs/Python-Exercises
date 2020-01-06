#080 Link names
firstname = input("Please enter your first name: ")
print("There are " + str(len(firstname)) + " characters in your name")

surname = input("Please enter your surname: ")
print("There are " + str(len(surname)) + " characters in your name")

print(firstname + " " + surname)
print("There are " + str(len(firstname) + len(surname)) + " characters in your full name")

#081 Favourite school subject
subject = input("What is your favourite subject at school? ")
newString = ""
for i in subject:
    newString = newString + i + "-"

print(newString[:-1])

#082 Display part of poem
poem = "To be or not to be, that is the question; Whether tis nobler in the mind to suffer"

start = 999
while start < 0 or start > len(poem) - 1:
    start = int(input("Please enter a number between 0 and " + str(len(poem) - 1) + ": "))

end = -1
while end < start + 1 or end > len(poem):
    end = int(input("Please enter a number between " + str(start + 1) + " and " + str(len(poem)) + ": "))

print(poem[start:end])

#083 Check if upper case
s = input("Please enter a word: ")
while s.isupper() != True:
    print("This is not uppercase")
    s = input("Please enter a word: ")
    
print(s + " contains just uppercase letters")

#084 convert postcode to upper
postcode = input("Please enter your postcode: ")
print(postcode[0:2].upper() + postcode[2:])

#085 how many vowels
vowels = ("a", "e", "i", "o", "u")
name = input("Please type a word: ")
count = 0;
for i in name.lower():
    if i in vowels:
        count = count + 1

print("There are", count, "vowels in", name)

#086 password entry
password = input("Please enter a password: ")
password2 = input("Please retype your password: ")

if password!=password2:
    if password.lower() == password2.lower():
        print("The passwords must be in the same case")
    else:
        print("The passwords do not match")
else:
    print("Thankyou, the passwords match")

#087 Reverse the word
word = input("Please enter a word: ")

for i in range(len(word) - 1, -1, -1):
    print(word[i])


