with open("liczby.txt", "r") as f:
    count = 0
    for lines in f.readlines():
        numbers = lines.split()
        for number in numbers:
            number_list = list(number)
            sum(number_list[0: -1])
            if number_list[0] + number_list[1] + number_list[2] == 35:
                count += 1


print(count)