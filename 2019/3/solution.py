with open("input.txt") as f:
    data = f.readlines()
    wires = [r for r in data]


# PART 1

locations = dict()


def move(location, direction):
    x, y = location
    directions = {
        "U": (x, y + 1),
        "D": (x, y - 1),
        "L": (x - 1, y),
        "R": (x + 1, y)
    }
    return directions[direction]


for w, wire in enumerate(wires):
    path = [i.strip() for i in wire.split(",")]

    location = (0, 0)
    for p in path:
        direction = p[0]
        distance = int(p[1:])

        for _ in range(distance):
            location = move(location, direction)
            if location in locations:
                locations[location].append(w)
            else:
                locations[location] = [w]


def manhattan_distance_from_origin(location):
    x, y = location
    return abs(x) + abs(y)


distances = list()
for location, visited_list in locations.items():
    if 0 in visited_list and 1 in visited_list:
        distances.append(manhattan_distance_from_origin(location))

print("solution: {}".format(min(distances)))


# PART 2

# will have two keys, one for each wire
# each wire will have a dict for all the points it has visited, with the
# distance traveled by first visit
visited_points = {0: dict(), 1: dict()}

for w, wire in enumerate(wires):
    visited = visited_points[w]
    path = [i.strip() for i in wire.split(",")]

    location = (0, 0)
    distance_traveled = 0
    for p in path:
        direction = p[0]
        distance = int(p[1:])

        for _ in range(distance):
            location = move(location, direction)
            distance_traveled += 1
            if location in visited:
                continue
            visited[location] = distance_traveled


distances_traveled = list()
intersections = set(visited_points[0].keys()).intersection(
    set(visited_points[1].keys())
)
for i in intersections:
    distances_traveled.append(visited_points[0][i] + visited_points[1][i])

print("solution part 2: {}".format(min(distances_traveled)))
