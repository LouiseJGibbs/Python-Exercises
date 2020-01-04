#082 Display part of poem
poem = "To be or not to be, that is the question; Whether tis nobler in the mind to suffer"

start = 999
while start < 0 or start > len(poem) - 1:
    start = int(input("Please enter a number between 0 and " + str(len(poem) - 1) + ": "))

end = -1
while end < start + 1 or end > len(poem):
    end = int(input("Please enter a number between " + str(start + 1) + " and " + str(len(poem)) + ": "))

print(poem[start:end])

