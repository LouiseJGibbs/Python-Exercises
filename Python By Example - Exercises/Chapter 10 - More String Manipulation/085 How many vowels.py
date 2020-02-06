#085 how many vowels
vowels = ("a", "e", "i", "o", "u")
name = input("Please type a word: ")
count = 0;
for i in name.lower():
    if i in vowels:
        count = count + 1

print("There are", count, "vowels in", name)
