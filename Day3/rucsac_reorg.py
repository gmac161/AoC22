# Part 1

priority = 0
for line in open("input.txt", "r").readlines():
    top, base = line[: len(line) // 2], line[len(line) // 2 :]
    item = "".join(set(top).intersection(base))
    if item.isupper():
        priority += ord(item) - 38
    else:
        priority += ord(item) - 96
print(priority)

# Part 2
priority = 0
with open("input.txt", "r") as f:
    mylist = f.read().splitlines()
    for n in range(0, len(mylist), 3):
        grp = mylist[n : n + 3]
        badge = "".join(set.intersection(*map(set, grp)))
        if badge.isupper():
            priority += ord(badge) - 38
        else:
            priority += ord(badge) - 96
print(priority)
