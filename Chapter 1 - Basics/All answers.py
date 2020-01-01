#001 print name
name = input("What is your name? ")
print("Hello", name)

#002 print first and last name
firstname = input("What is your first name? ")
surname = input("What is your surname? ")
print("Hello", firstname, surname)

#003 print joke using 1 line of code
print("What do you call a bear with no teeth?\nA Gummy Bear!")

#004 Add 2 numbers
num1 = int(input("Please enter a number "))
num2 = int(input("Please enter another number "))
print("Sum of these 2 numbers is ", num1 + num2)

#005 Add 2 then multiple
num1 = int(input("Please enter a number "))
num2 = int(input("Please enter another number "))
num3 = int(input("Please enter a third number which the sum of the first 2 numbers will be multiplied by "))
print("(", num1, "+", num2, ")*", num3, "=", (num1+num2)*num3)

#006 Pizza Slices
slices = int(input("How many slices of pizza did you start with "))
eat = int(input("How many slices of pizza have you eaten "))
print("You have ", slices - eat, " left")

#007 Next birthday age
name = input("What is your name? ")
age = int(input("How old are you? "))
print(name, "next birthday you will be ", age + 1)

#008 Restaurant Bill
price = int(input("What is the total value of the bill? "))
diners = int(input("How many diners are there? "))
print("Each person should pay ", price/diners, " towards the cost of the meal")

#009 Days into hours, minutes and seconds
days = int(input("How many days have there been? "))
hours = days/24
minutes = hours/60
seconds = minutes/60
print(days, "days is the same as ", hours, " hours or ", minutes, " minutes or ", seconds, " seconds.") 

#010 KG into pounds
kilograms = int(input("How many kilograms? "))
pounds = kilograms/2204
print(kilograms, " is equivalent to ", pounds)

#011 number under 10 in number over 100
small = int(input("Please enter a number under 10"))
large = int(input("Please enter a number over 100"))
print(small, "goes into ", large, " ", large//small, " times")
