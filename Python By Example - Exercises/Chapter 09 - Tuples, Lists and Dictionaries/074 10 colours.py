#074 10 colours

colour = []
for i in range(1,11):
    colour.append(input("Please enter a colour (" + str(11-i)+ " to go): "))

start = int(input("Please enter a number between 0 and 4: "))
end = int(input("Please enter a number between 5 and 9: "))

print(colour[start:end])
