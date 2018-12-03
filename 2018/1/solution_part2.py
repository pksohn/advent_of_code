frequency = 0
seen_frequencies = set()
frequency_seen_twice = None

while frequency_seen_twice is None:
    with open("input.txt") as f:
        for line in f:
            sign, number = line[0], line[1:]
            multiplier = 1 if sign == "+" else -1
            frequency += int(number) * multiplier
            if frequency in seen_frequencies:
                frequency_seen_twice = frequency
                break
            seen_frequencies.add(frequency)

print frequency_seen_twice
