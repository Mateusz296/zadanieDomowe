with open("slowa.txt", "r") as f:
    is_anagram = 0
    for line in f.readlines():
        elements = line.split()
        if sorted(elements[0]) == sorted(elements[1]):
            is_anagram += 1

print(is_anagram)