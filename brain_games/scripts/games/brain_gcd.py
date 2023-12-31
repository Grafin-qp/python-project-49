import random
from ...cli import welcome_user
from ... import game_logic


def gcd_game_logic():
    """
    Find the greatest common divisor of two random numbers.
    Returns:
        tuple: A tuple containing the random numbers and the correct answer.
    """
    random_num1 = random.randint(1, 100)
    random_num2 = random.randint(1, 100)
    nums = random_num1, random_num2
    sorted_nums = sorted(nums, reverse=True)
    divider = sorted_nums[0] % sorted_nums[1]
    divisible = sorted_nums[1]

    while divider > 0:
        cur_amount = divisible % divider
        divisible = divider
        divider = cur_amount

    quest_nums = f"{random_num1} {random_num2}"
    correct_answer = str(divisible)
    return quest_nums, correct_answer


def main():
    """
    Main entry point of the greatest common divisor game.
    """
    user_name = welcome_user()
    rules = 'Find the greatest common divisor of given numbers.'
    game_logic.game_play(user_name, gcd_game_logic, rules)


if __name__ == '__main__':
    main()
