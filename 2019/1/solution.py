with open("input.txt") as f:
    data = f.readlines()
    data.sort()
    total_fuel = 0
    for line in data:
        mass = int(line)
        # In python 2, division is floor division so don't need to round down
        fuel = (mass / 3) - 2
        total_fuel += fuel

print("Part 1 Answer:" + str(total_fuel))


def recursive_fuel_for_mass(mass):
    fuel = (mass / 3) - 2
    if fuel > 0:
        fuel += recursive_fuel_for_mass(fuel)
    return max(fuel, 0)


with open("input.txt") as f:
    data = f.readlines()
    data.sort()
    total_fuel = 0
    for line in data:
        mass = int(line)
        total_fuel += recursive_fuel_for_mass(mass)


print("Part 2 Answer:" + str(total_fuel))
