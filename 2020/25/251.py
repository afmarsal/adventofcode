import functools
import itertools


def do_it(card_pk, door_pk):
    transform = lambda subject, value: (subject * value) % 20201227

    def find_loop(pk):
        subject = 7
        value, loop = subject, 1
        while value != pk:
            value = transform(subject, value)
            loop += 1
        return loop

    def encrypt(pk, loop):
        return functools.reduce(lambda x, y: transform(pk, x), range(loop-1), pk)

    card_loop = find_loop(card_pk)
    door_loop = find_loop(door_pk)
    print(f'card_loop: {card_loop}, door_loop: {door_loop}')
    card_encr = encrypt(door_pk, card_loop)
    door_encr = encrypt(card_pk, door_loop)
    print(f'card_encr: {card_encr}, door_enc: {door_encr}')
    if card_encr != door_encr:
        raise Exception('Dont match!')
    return card_encr


if __name__ == '__main__':
    # card_pk, door_pk = 5764801, 17807724
    card_pk, door_pk = 15628416, 11161639
    print(f'Part 1: {do_it(card_pk, door_pk)}')

# Part 1: 19774660
