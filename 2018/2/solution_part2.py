# I kind of hate this solution, but oh well. Who's got time for nice side-code?


def common_letter_string(a, b):
    new_string = ""
    for i, character in enumerate(a):
        if b[i] == character:
            new_string += character
    return new_string


halves = dict()


with open("input.txt") as f:
    for line in f:
        line = line.rstrip()
        # Throw the full ID into a dict twice, with the first and second half
        # of the ID as separate keys. The match will be in one of these lists.
        for half in [line[:13], line[13:]]:
            if half in halves:
                halves[half].append(line)
            else:
                halves[half] = [line]

for half in halves:
    # Now that our search space is small, I feel OK about looping through
    # all the combinations.
    list_of_ids = halves[half]
    if len(list_of_ids) > 1:
        for a in list_of_ids:
            for b in list_of_ids:
                new_string = common_letter_string(a, b)
                if len(new_string) == 25:
                    print new_string
                    break
