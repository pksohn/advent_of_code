frequency = 0

with open("input.txt") as f:
    for line in f:
        sign, number = line[0], line[1:]
        multiplier = 1 if sign == "+" else -1
        frequency += int(number) * multiplier

print frequency
