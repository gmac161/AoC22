def read_file(name):
    lines = []
    with open(name) as f:
        for line in f:
            lines.append(line.strip())
        return lines


all_cals = read_file("./calorie_input.txt")
cal_dict = {}
cal_list = []
elf = 1
for cal in all_cals:
    if cal:
        cal_list.append(int(cal))
    else:
        cal_dict[elf] = sum(cal_list)
        elf += 1
        cal_list = []

print(max(cal_dict.values()))

# Part 2
sorted_dict = dict(
    sorted(cal_dict.items(), key=lambda item: item[1], reverse=True)
)
top3 = {k: sorted_dict[k] for k in list(sorted_dict)[:3]}
print(sum(top3.values()))
