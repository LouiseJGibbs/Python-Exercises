#020 Name length
name = input("What is your name: ")
print("Your name has", len(name), "characters in it")

#021 Full name length
firstname = input("What is your first name: ")
surname = input("What is your surname: ")
print("Your full name has", len(firstname + surname), "characters in it")

#022 Full name to title
firstname = input("Please enter your first name in lower case: ")
surname = input("Please enter your surname in lower case: ")
print(firstname.title(),surname.title())

#023 Print section of string
rhyme = input("Please enter the first line of a nursery rhyme: ")
rhymeLength = len(rhyme)
print("You've entered", rhymeLength, "characters")

num1 = int(input("Please enter a number that is less than " + str(rhymeLength) + ": "))
num2 = int(input("Please enter a number between " + str(num1) + " and "+ str(rhymeLength) + ": "))
print(rhyme[num1:num2])

#024 Convert to upper
word = input("Please enter a word: ")
print(word.upper())

#025 Surname if firstname is less than 5
firstname = input("Please enter your first name: ")

if len(firstname) <= 5:
    surname = input("Please enter your surname: ")
    print((firstname + surname).upper())
else:
    print(firstname.lower())

#026 pig latin
word = input("Please enter a word: ").lower()
if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
    print(word + "way")
else:
    print(word[1:len(word)] + word[0] + "ay")

#026 pig latin v2
vowels = ("a", "e", "i", "o", "u")
word = input("Please enter a word: ").lower()

if word[0] in vowels:
    print(word.Lower() + "way")
else:
    print(word[1:len(word)] + word[0] + "ay")



    
