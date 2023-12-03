
### This code is for the progression game###

import random
from ...cli import welcome_user
from ... import game_logic


def progression_game_logic():
    """
    Generate an arithmetic progression and determine the missing number.
    Returns:
        tuple: A tuple containing the formatted progression string and the correct answer.
    """
    random_length = random.randint(5, 10)
    random_num = random.randint(0, 100)
    random_summ = random.randint(2, 25)
    random_secret = (random.randint(5, random_length) - 1)
    random_list = []
    counter = 0

    while counter < random_length:
        random_list.append(random_num)
        random_num += random_summ
        counter += 1

    correct_answer = str(random_list[random_secret])
    random_list[random_secret] = '..'

    # Преобразование чисел списка в строки и их объединение
    formatted_string = ' '.join(map(str, random_list))
    return formatted_string, correct_answer


def main():
    """
    Main entry point of the progression game.
    """
    user_name = welcome_user()
    rules = 'What number is missing in the progression?'
    game_logic.game_play(user_name, progression_game_logic, rules)


if __name__ == '__main__':
    main()

