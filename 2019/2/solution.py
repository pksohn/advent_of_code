with open("input.txt") as f:
    data = f.readlines()
    original_input = [int(i) for i in data[0].split(",")]

# PART 1

# before running the program, replace position 1 with the value 12 and
# replace position 2 with the value 2.
input_list = list(original_input)
input_list[1] = 12
input_list[2] = 2

opcode_position = 0
while True:
    opcode = input_list[opcode_position]
    if opcode not in (1, 2, 99):
        raise ValueError("oops, something went wrong")

    if opcode == 99:
        break

    a_position = input_list[opcode_position + 1]
    a = input_list[a_position]

    b_position = input_list[opcode_position + 2]
    b = input_list[b_position]

    where_to_store = input_list[opcode_position + 3]

    if opcode == 1:
        value_to_store = a + b
    elif opcode == 2:
        value_to_store = a * b

    input_list[where_to_store] = value_to_store
    opcode_position += 4

print("solution: " + str(input_list[0]))


# PART 2


def try_input(input_list, noun, verb):

    input_list = list(input_list)
    input_list[1] = noun
    input_list[2] = verb

    opcode_position = 0
    while True:
        opcode = input_list[opcode_position]
        if opcode not in (1, 2, 99):
            raise ValueError("oops, something went wrong")

        if opcode == 99:
            break

        a_position = input_list[opcode_position + 1]
        a = input_list[a_position]

        b_position = input_list[opcode_position + 2]
        b = input_list[b_position]

        where_to_store = input_list[opcode_position + 3]

        if opcode == 1:
            value_to_store = a + b
        elif opcode == 2:
            value_to_store = a * b

        input_list[where_to_store] = value_to_store
        opcode_position += 4

    return input_list[0]


for n in range(100):
    for v in range(100):
        if try_input(original_input, n, v) == 19690720:
            print(
                "part 2 solution: 100 * {} + {} = {}".format(n, v, 100 * n + v)
            )
            break
