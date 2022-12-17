with open("day4.txt") as f:
    total = 0
    for i in f.readlines():
        ranges = i.strip().split(",")
        assert len(ranges) == 2
        left_start, left_end = map(int, ranges[0].split("-"))
        right_start, right_end = map(int, ranges[1].split("-"))
        if (
            (left_start >= right_start and left_end <= right_end) or
            (right_start >= left_start and right_end <= left_end)
        ):
            total += 1

    print("Part 1 total: {}".format(total))


with open("day4.txt") as f:
    total = 0
    for i in f.readlines():
        ranges = i.strip().split(",")
        assert len(ranges) == 2
        left_start, left_end = map(int, ranges[0].split("-"))
        right_start, right_end = map(int, ranges[1].split("-"))
        if (
            (left_start > right_start and left_start > right_end) or
            (left_end < right_start and left_end < right_end)
        ):
            continue
        total += 1

    print("Part 2 total: {}".format(total))