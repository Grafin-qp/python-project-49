
"""Main module for brain games."""

import os
import sys
import logging
from cli import welcome_user

sys.path.append(os.path.expanduser('~/python-project-49/brain_games'))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """Run main function for brain games."""
    logger.info('Welcome to the Brain Games!')


if __name__ == '__main__':
    main()
    welcome_user()
