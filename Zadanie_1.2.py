with open("slowa.txt", "r") as f:
    a_is_in_b = 0
    for line in f.readlines():
        elements = line.split()
        if elements[0] in elements[1]:
            a_is_in_b += 1

print(a_is_in_b)
