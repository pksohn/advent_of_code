
with open("input.txt") as f:
    data = f.readlines()
    data.sort()
    for line in data:
        print line, type(line)


# never finished.