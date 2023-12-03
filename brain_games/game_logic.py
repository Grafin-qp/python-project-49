
# This is a main file with logic of all brain games.

import random


def question_asker(question):
    """Display a question."""
    print(f'Question: {question}')


def game_play(name, game_logic, game_rules):
    """Main function for game_even"""
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

# Пример использования функции game_play:
# game_play("Player"\или функцию из приветствия, game_logic_functio, переменную с правилами)
# Замените game_logic на фактическую функцию логики игры

