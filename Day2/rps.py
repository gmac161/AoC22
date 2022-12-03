# Rock paper scissors
# Part 1
scores = []
for line in open("input.txt", "r").readlines():
    if line[2] == "X":
        score = 1
        if line[0] == "A":
            score = score + 3
        elif line[0] == "B":
            score = score
        else:
            score = score + 6
    elif line[2] == "Y":
        score = 2
        if line[0] == "A":
            score = score + 6
        elif line[0] == "B":
            score = score + 3
        else:
            score = score + 0
    else:
        score = 3
        if line[0] == "A":
            score = score
        elif line[0] == "B":
            score = score + 6
        else:
            score = score + 3
    scores.append(score)
print(sum(scores))


# Part 1 - more efficient way
rps = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
scores = []
for line in open("input.txt", "r").readlines():
    if rps[line[2]] == rps[line[0]]:
        scores.append(rps[line[2]] + 3)
    elif rps[line[2]] == rps[line[0]] + 1:
        scores.append(rps[line[2]] + 6)
    elif rps[line[2]] == rps[line[0]] - 2:
        scores.append(rps[line[2]] + 6)
    else:
        scores.append(rps[line[2]])
print(sum(scores))


# Part 2
scores = []
for line in open("input.txt", "r").readlines():
    # loss
    # Rock (A) beats scissors (C)
    # Paper (B) beats rock (A)
    # Scissors (C) beats paper (B)

    if line[2] == "X":
        if line[0] == "A":
            score = 3
        elif line[0] == "B":
            score = 1
        else:
            score = 2

    # draw
    elif line[2] == "Y":
        score = 3
        if line[0] == "A":
            score = score + 1
        elif line[0] == "B":
            score = score + 2
        else:
            score = score + 3
    # win
    else:
        score = 6
        if line[0] == "A":
            score = score + 2
        elif line[0] == "B":
            score = score + 3
        else:
            score = score + 1
    scores.append(score)
print(sum(scores))


# Part 2 More efficient method
rps = {"A": 1, "B": 2, "C": 3}
scores = []
for line in open("input.txt", "r").readlines():
    if line[2] == "X":  # lose
        if rps[line[0]] != 1:
            scores.append(rps[line[0]] - 1)
        else:
            scores.append(rps[line[0]] + 2)
    elif line[2] == "Y":  # draw
        scores.append(rps[line[0]] + 3)
    else:  # win
        if rps[line[0]] != 3:
            scores.append(rps[line[0]] + 7)
        else:
            scores.append(rps[line[0]] + 4)
print(sum(scores))
