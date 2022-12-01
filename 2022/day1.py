with open("day1.txt") as f:

    highest_total = 0
    running_total = 0
    for i in f.readlines():
        if i == "\n":
            highest_total = max(running_total, highest_total)
            running_total = 0
            continue
        running_total += int(i)
    # account for end of file
    highest_total = max(running_total, highest_total)
    print("pt 1 highest total: {}".format(highest_total))

def check_list(new_value, top_three):
    # assume the list is ALWAYS sorted.
    # this is totally not efficient.

    if len(top_three) < 3:
        top_three.append(new_value)
        top_three.sort()
    if new_value > top_three[0]:
        top_three.append(new_value)
        top_three = top_three[1:]
        top_three.sort()
        assert len(top_three) == 3
    return top_three

with open("day1.txt") as f:

    highest = []
    current = []
    running_total = 0
    for i in f.readlines():
        if i == "\n":
            highest = check_list(running_total, highest)
            running_total = 0
            continue
        running_total += int(i)
    # account for end of file
    highest = check_list(running_total, highest)

    print("pt 2 top three sum: {}".format(sum(highest)))
