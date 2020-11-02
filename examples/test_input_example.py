import sys
sys.path.insert(0, "..")
from num_conv.engine import run
import json
import logging.config
import os


def setup_logging(
    default_path='logging.json',
    default_level=logging.INFO,
):
    """ Setup logging configuration """

    if os.path.exists(default_path):
        with open(default_path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def main():
    # setup_logging() # uncomment this function to add logging
    run("test_input.txt")


if __name__ == '__main__':
    main()
