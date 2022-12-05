import re


def read_file(name):
    lines = []
    with open(name) as f:
        for line in f:
            lines.append(line.strip("\n"))
        return lines


def get_number_of_stacks(lines):
    for line in lines:
        if line.lstrip().startswith("1"):
            stacks = [int(s) for s in line.split() if s.isdigit()]
            num_stacks = stacks[-1]
            return num_stacks


result = []
l = read_file("input.txt")
number_of_stacks = get_number_of_stacks(l)
# Create dictionary with empty lists
stack = {}
for i in range(1, number_of_stacks + 1):
    stack[i] = []
# Create a list for each stack
for line in l:
    if line.lstrip().startswith("["):
        n = 1
        for i in range(1, number_of_stacks + 1):
            stack[i].append(line[n].strip())
            n += 4
    # Remove blanks (no crate)
    for i in range(1, number_of_stacks + 1):
        stack[i] = list(filter(None, stack[i]))

# Part 1

# for line in l:
#     if line.startswith("move"):
#         instructions = [int(s) for s in line.split() if s.isdigit()]
#         i = 0
#         while i < instructions[0]:
#             stack[instructions[2]].insert(0, stack[instructions[1]].pop(0))
#             i += 1

# Part 2

for line in l:
    if line.startswith("move"):
        instructions = [int(s) for s in line.split() if s.isdigit()]
        stack[instructions[2]] = (
            stack[instructions[1]][: instructions[0]] + stack[instructions[2]]
        )
        stack[instructions[1]] = stack[instructions[1]][instructions[0] :]

for i in range(1, number_of_stacks + 1):
    result.append(stack[i][0])
print(result)
