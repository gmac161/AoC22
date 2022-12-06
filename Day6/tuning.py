# Part 1
for str in open("input.txt", "r").readlines():
    i = 0
    while len(set(str[i : i + 4])) != 4:
        i += 1
    print(i + 4)

# Part 2
for str in open("input.txt", "r").readlines():
    i = 0
    while len(set(str[i : i + 14])) != 14:
        i += 1
    print(i + 14)
