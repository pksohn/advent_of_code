def score(us, them):
    WIN = 6
    DRAW = 3
    LOSE = 0

    selection_score = -1
    result_score = -1

    if us == "X": # rock
        selection_score = 1
        if them == "A": # rock
            result_score = DRAW
        elif them == "B": # paper
            result_score = LOSE
        else: # scissors
            result_score = WIN

    elif us == "Y": # paper
        selection_score = 2
        if them == "A": # rock
            result_score = WIN
        elif them == "B": # paper
            result_score = DRAW
        else: # scissors
            result_score = LOSE

    else: # scissors
        selection_score = 3
        if them == "A": # rock
            result_score = LOSE
        elif them == "B": # paper
            result_score = WIN
        else: # scissors
            result_score = DRAW

    assert selection_score != -1
    assert result_score != -1
    return selection_score + result_score

def selection_from_result(them, result):
    if them == "A": # rock
        if result == "X": # lose
            return "Z" # scissors
        elif result == "Y": # draw
            return "X" # rock
        else:
            return "Y" # paper
    elif them == "B": # paper
        if result == "X": # lose
            return "X"
        elif result == "Y": # draw
            return "Y"
        else:
            return "Z"
    else: # scissors
        if result == "X": # lose
            return "Y"
        elif result == "Y": # draw
            return "Z"
        else:
            return "X"

with open("day2.txt") as f:
    total = 0
    for i in f.readlines():
        them = i[0]
        us = i[2]
        round_score = score(us, them)
        total += round_score

    print("pt 1 total: {}".format(total))

with open("day2.txt") as f:
    total = 0
    for i in f.readlines():
        them = i[0]
        result = i[2]
        round_score = score(selection_from_result(them, result), them)
        total += round_score

    print("pt 2 total: {}".format(total))
