#087 Reverse the word
word = input("Please enter a word: ")

for i in range(len(word) - 1, -1, -1):
    print(word[i])
