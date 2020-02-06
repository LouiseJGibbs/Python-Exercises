#071 List of sports
sports_list = ["Football", "Cricket"]
anothersport = "yes"
print(sorted(sports_list))
while input("Another Sport? yes/no: ") == "yes":
    sports_list.append(input("What is your favourite sport? "))
    print(sorted(sports_list))
