
# This is a first part of brain games. A game for defining even numbers.

import random
from ..cli import welcome_user
from .. import game_logic


def even_game_logic():
    """checking is the number even"""
    num = random.randint(1, 100)
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return num, correct_answer


def main():
    user_name = welcome_user()
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    game_logic.game_play(user_name, even_game_logic, rules)


if __name__ == '__main__':
    main()

