from collections import Counter

three_of_same_letter_count = 0
two_of_same_letter_count = 0

with open("input.txt") as f:
    for line in f:
        unique_counts = set(Counter(line).values())
        if 3 in unique_counts:
            three_of_same_letter_count += 1
        if 2 in unique_counts:
            two_of_same_letter_count += 1

checksum = three_of_same_letter_count * two_of_same_letter_count
print checksum
