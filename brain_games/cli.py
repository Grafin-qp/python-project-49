"""This module welcomes the user."""

import logging
import prompt

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def welcome_user():
    """Ask for the user's name and print a greeting."""
    name = prompt.string('May I have your name?')
    logger.info('Hello, %s!', name)


if __name__ == '__main__':
    welcome_user()

