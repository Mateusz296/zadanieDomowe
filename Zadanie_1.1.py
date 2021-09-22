words = open("slowa.txt", "r")


ending_with_a = 0
for line in words.readlines():
    for word in line.split(" "):
        if word[-1] == "A":
            ending_with_a += 1

print(ending_with_a)
words.close()
