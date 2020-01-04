#070 Country Tuple (select index)
country_tuple = ("UK", "France", "Germany", "Holland", "Spain")

for i in range(0,len(country_tuple)):
    print(i, country_tuple[i])

selection = int(input("Which country would you like. Enter a number between 0 and " + str(len(country_tuple)- 1)+ ": "))
while selection > (len(country_tuple)-1):
    selection = int(input("Which country would you like. Enter a number between 0 and " + str(len(country_tuple) - 1) + ": "))

print("You have selected " + country_tuple[selection])
