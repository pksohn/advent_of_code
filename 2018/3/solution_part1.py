import re

# Keys are (x, y) tuples, and values are number of claims on that spot
fabric = dict()

pattern = (
    r"#(?P<id>\d+) @ " 
    r"(?P<left>\d+),(?P<top>\d+): "
    r"(?P<wide>\d+)x(?P<tall>\d+)"
)

with open("input.txt") as f:
    for line in f:
        line = line.rstrip()
        match = re.match(pattern, line)
        id, left, top, wide, tall = (int(i) for i in match.groups())

        columns = range(left + 1, left + 1 + wide)
        rows = range(top + 1, top + 1 + tall)

        for c in columns:
            for r in rows:
                coordinate = (c, r)
                if coordinate in fabric:
                    fabric[coordinate] += 1
                else:
                    fabric[coordinate] = 1


num_squares_with_multiple_claims = 0
for count in fabric.values():
    if count > 1:
        num_squares_with_multiple_claims += 1

print num_squares_with_multiple_claims

