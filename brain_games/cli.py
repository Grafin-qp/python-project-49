"""This module welcomes the user."""


def welcome_user():
    """Ask for the user's name and print a greeting."""
    print('Welcome to the Brain Games!\n')
    name = input("May I have your name?\n")
    print(f'Hello, {name}!\n\n')
    return name


if __name__ == '__main__':
    welcome_user()
