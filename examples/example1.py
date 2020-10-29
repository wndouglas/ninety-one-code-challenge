import os
import json
import logging.config


def setup_logging(
    default_path='logging.json',
    default_level=logging.INFO,
):
    """
    Setup logging configuration
    """

    if os.path.exists(default_path):
        with open(default_path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def main():
    setup_logging("blabla.json", logging.DEBUG)


if __name__ == '__main__':
    main()
