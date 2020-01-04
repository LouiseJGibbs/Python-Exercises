#069 Country Tuple
country_tuple = ("UK", "France", "Germany", "Holland", "Spain")

print(country_tuple[0:5])
selection = input("Which country would you like: ")
print("You have selected " + selection+ ". The index for this is " + str(country_tuple.index(selection)))
