
# This is a first part of brain games. A game for defining even numbers.

import random


def welcome_user():
    """Ask for the user's name and print a greeting."""
    print('Welcome to the Brain Games!\n')
    name = input('May I have your name?\n')
    print(f'Hello, {name}!\n\n')
    return name


def answer_checker(num):
    """checking is the number even"""
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def brain_even(name):
    """main function for game_even"""
    be_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(be_rules)
    counter = 0
    while counter < 3:
        random_num = random.randint(1, 99)
        print(f'Question: {random_num}')
        answer = input(f'Your answer: ')
        correct_answer = answer_checker(random_num)
        if correct_answer == answer.lower():
            print('\nCorrect!\n')
            counter += 1
        else:
            print(f"\n'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}")
            break


    if counter == 3:
        print(f'\nCongratulations, {name}!')


def main():
    user_name = welcome_user()
    brain_even(user_name)


if __name__ == '__main__':
    main()
