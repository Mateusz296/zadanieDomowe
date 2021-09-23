
with open('slowa.txt', 'r') as f:
    ending_with_a = 0
    for line in f.readlines():
        for word in line.split():
            if word.endswith("A"):
                ending_with_a += 1
print(ending_with_a)


