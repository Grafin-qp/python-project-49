import random
import math
from ..cli import welcome_user
from .. import game_logic


def prime_game_logic():
    random_num = random.randint(0, 100)
    max_dil = math.floor(math.sqrt(random_num))
    counter = 2
    correct_answer = 'yes'

    while counter <= max_dil and random_num > 2:
        if (random_num % counter) == 0:
            correct_answer = 'no'
            break
        else:
            counter += 1

        if random_num < 2:
            correct_answer = 'no'
        elif random_num == 2:
            correct_answer = 'yes'

    return random_num, correct_answer


def main():
    user_name = welcome_user()
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game_logic.game_play(user_name, prime_game_logic, rules)


if __name__ == '__main__':
    main()

