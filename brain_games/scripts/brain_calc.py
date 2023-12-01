mport random
from ..cli import welcome_user
from .. import game_logic


def calc_game_logic():
    random_num1 = random.randint(1, 100)
    random_num2 = random.randint(1, 100)
    symbols = ['-', '+', '*']
    random_sym = random.choice(symbols)
    expression = f'{random_num1} {random_sym} {random_num2}'
    correct_answer = str(eval(expression))
    return expression, correct_answer


def main():
    user_name = welcome_user()
    rules = 'What is the result of the expression?'
    game_logic.game_play(user_name, calc_game_logic, rules)


if __name__ == '__main__':
    main()
