#072 School subjects
topics_list = ["Maths", "French", "German", "English", "Sports", "Art"]
print(sorted(topics_list))
listComplete = "no"

while listComplete != input("Would you like to change subjects? yes/no "):
    d = input("What subject would you like to delete? ")
    r = input("What new subject would you like to add? ")
    topics_list.remove(d)
    topics_list.append(r)
    print(sorted(topics_list))
    
