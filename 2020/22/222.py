def unique_str(deck1, deck2):
    # return ','.join([str(n) for n in deck1]) + ':' + ','.join([str(n) for n in deck2])
    return sum((i + 1) * j for i, j in enumerate(deck1)) * 1000000 + sum((i + 1) * j for i, j in enumerate(deck2))


counter = 1


def add(l, c1, c2):
    l.append(c1)
    l.append(c2)


def win(deck1, deck2, game=1):
    rounds = set()
    round = 1
    while len(deck1) > 0 and len(deck2) > 0:
        # print(f'-- Round {round} (game {game})--\n{deck1}\n{deck2}')
        round += 1
        draw_str = unique_str(deck1, deck2)
        if draw_str in rounds:
            return True

        global counter
        counter += 1
        rounds.add(draw_str)

        c1 = deck1.pop(0)
        c2 = deck2.pop(0)
        if c1 <= len(deck1) and c2 <= len(deck2):
            if win(deck1[:c1], deck2[:c2], game + 1):
                add(deck1, c1, c2)
            else:
                add(deck2, c2, c1)

        else:
            if c1 > c2:
                add(deck1, c1, c2)
            else:
                add(deck2, c2, c1)
    return len(deck1) > len(deck2)


def do_it(lines):
    deck1, deck2 = parse_decks(lines)
    print(f'Start game: \n{deck1}\n{deck2}')
    winner = deck1 if win(deck1, deck2) else deck2

    winner.reverse()
    return sum((i + 1) * c for i, c in enumerate(winner))


def parse_decks(lines):
    deck1 = []
    for i in range(1, len(lines)):
        if len(lines[i]) == 0:
            break
        deck1.append(int(lines[i]))
    deck2 = []
    for i in range(i + 2, len(lines)):
        deck2.append(int(lines[i]))
    return deck1, deck2


if __name__ == '__main__':
    with open('input1.txt') as f:
        lines = list(map(str.strip, f))

    output = do_it(lines)
    print(f'Rounds: {counter}')
    print(f'Part 2: {output}')

# Part 1: 31436
