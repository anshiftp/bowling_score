def bowling_score(game):
    rolls = []
    for ch in game:
        if ch == 'X':
            rolls.append(10)
        elif ch == '-':
            rolls.append(0)
        elif ch == '/':
            rolls.append(10 - rolls[-1])
        else:
            rolls.append(int(ch))

    score = 0
    roll_index = 0

    for _ in range(10):
        if rolls[roll_index] == 10:
            score += 10 + rolls[roll_index + 1] + rolls[roll_index + 2]
            roll_index += 1
        elif rolls[roll_index] + rolls[roll_index + 1] == 10:
            score += 10 + rolls[roll_index + 2]
            roll_index += 2
        else:
            score += rolls[roll_index] + rolls[roll_index + 1]
            roll_index += 2

    return score
