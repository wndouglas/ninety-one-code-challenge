import os
import json
import logging.config

from num_conv.runner import run


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
    setup_logging()
    run("example2_input.txt", "example2_output.txt")


if __name__ == '__main__':
    main()
