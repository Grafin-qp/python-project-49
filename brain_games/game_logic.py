
# This is a main file with logic of all brain games.

import random

def question_asker(question):
    print(f'Question: {question}')


def game_play(name, game_logic, game_rules):
    """main function for game_even"""
    print(game_rules)
    counter = 0
    while counter < 3:
        question, correct_answer = game_logic()
        question_asker(question)
        answer = input('Your answer: ').lower()
        if answer == correct_answer:
            print('\nCorrect!\n')
            counter += 1
        else:
            print(f"\n'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}")
            break
        
        if counter == 3:
            print(f"\nCongratulations, {name}!")

