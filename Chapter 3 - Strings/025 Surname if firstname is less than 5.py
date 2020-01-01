#025 Surname if firstname is less than 5
firstname = input("Please enter your first name: ")

if len(firstname) <= 5:
    surname = input("Please enter your surname: ")
    print((firstname + surname).upper())
else:
    print(firstname.lower())
