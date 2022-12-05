import re

# Part 1
count = 0
for line in open("input.txt", "r").readlines():
    a, b, c, d = re.split(",|-", line)
    set_a = set(range(int(a), int(b) + 1))
    set_b = set(range(int(c), int(d) + 1))
    if (set_a == set_a.intersection(set_b)) or (
        set_b == set_a.intersection(set_b)
    ):
        count += 1
print(count)

# Part 2
count = 0
for line in open("input.txt", "r").readlines():
    a, b, c, d = re.split(",|-", line)
    set_a = set(range(int(a), int(b) + 1))
    set_b = set(range(int(c), int(d) + 1))
    if set_a.intersection(set_b):
        count += 1
print(count)
