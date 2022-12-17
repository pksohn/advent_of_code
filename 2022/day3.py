def get_priority(item):
    # >>> ord("a")
    # 97
    # >>> ord("A")
    # 65
    priority = -1
    codepoint = ord(item)
    if codepoint >= 97:
        # a to z
        priority = codepoint - 96
    else:
        priority = codepoint - 64 + 26
    assert priority > 0
    return priority

with open("day3.txt") as f:
    total = 0

    for i in f.readlines():

        # remove trailing newline.
        line = i.strip()

        # split two compartments
        midpoint = int(len(line) / 2)
        first = set(line[:midpoint])
        second = set(line[midpoint:])

        # get the common item
        common = first.intersection(second)
        assert len(common) == 1
        item = common.pop()

        total += get_priority(item)

    print("part 1 total: {}".format(total))


with open("day3.txt") as f:
    total = 0
    current_group = []

    for i in f.readlines():
        assert len(current_group) <= 3
        bag = set(i.strip())
        current_group.append(bag)
        if len(current_group) == 3:
            set_1 = current_group[0].intersection(current_group[1])
            set_2 = set_1.intersection(current_group[2])
            assert len(set_2) == 1
            item = set_2.pop()

            total += get_priority(item)

            current_group = []

    print("part 2 total: {}".format(total))




