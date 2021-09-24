with open("liczby.txt", "r") as f:
    is_sorted = 0
    for lines in f.readlines():
        numbers = lines.split()
        if numbers == sorted(numbers):
            is_sorted += 1

    print(is_sorted)
