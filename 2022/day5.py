from collections import defaultdict
import re


def do_part1_move(move_count, move_from, move_to, stacks):
    for _ in range(move_count):
        item_to_move = stacks[move_from].pop()
        stacks[move_to].append(item_to_move)

def do_part2_move(move_count, move_from, move_to, stacks):
    popped = []
    for _ in range(move_count):
        popped.append(stacks[move_from].pop())
    stacks[move_to] += reversed(popped)

def solve(move_function):
    with open("day5.txt") as f:
        found_columns = False
        pattern = r"move (?P<count>\d+) from (?P<from>\d+) to (?P<to>\d+)"

        raw_stacks = []
        stack_positions = []

        stacks = defaultdict(list)

        for i in f.readlines():
            if i.startswith(" 1 "):
                found_columns = True

                # parse this line for positions of each stack
                for idx, num in enumerate(i):
                    if num.isnumeric():
                        stack_positions.append(int(idx))

                # put stacks in a dict of lists
                # in the lists, the bottom of the stack is the first element
                for line in reversed(raw_stacks):
                    for idx, position in enumerate(stack_positions):
                        # stacks are 1-indexed in the prompt
                        item = line[position]
                        if item != " ":
                            stacks[idx + 1].append(item)

            elif found_columns is False:
                raw_stacks.append(i)
            elif i.startswith("move"):
                match = re.match(pattern, i).groupdict()
                move_count = int(match["count"])
                move_from = int(match["from"])
                move_to = int(match["to"])
                move_function(move_count, move_from, move_to, stacks)

        final_top = []
        # dicts are not ordered, i believe
        for n in range(len(stacks) + 1):
            stack = stacks[n]
            if len(stack) > 0:
                final_top.append(stack[-1])

        return "".join(final_top)

print("Part 1: {}".format(solve(do_part1_move)))
print("Part 2: {}".format(solve(do_part2_move)))