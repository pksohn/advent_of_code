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
                    fabric[coordinate].append(id)
                else:
                    fabric[coordinate] = [id]


claims_without_overlap = set()
claims_with_overlap = set()
for square in fabric.values():
    if len(square) > 1:
        for claim in square:
            claims_with_overlap.add(claim)
            if claim in claims_without_overlap:
                claims_without_overlap.remove(claim)
    elif len(square) == 1:
        if square[0] not in claims_with_overlap:
            claims_without_overlap.add(square[0])

print claims_without_overlap

