#026 pig latin
word = input("Please enter a word: ").lower()
if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
    print(word + "way")
else:
    print(word[1:len(word)] + word[0] + "ay")

#026 pig latin
vowels = ("a", "e", "i", "o", "u")
word = input("Please enter a word: ").lower()

if word[0] in vowels:
    print(word.Lower() + "way")
else:
    print(word[1:len(word)] + word[0] + "ay")
