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
