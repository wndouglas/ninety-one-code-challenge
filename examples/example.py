import os
import json
import logging.config

from num_conv.input_parser import InputParser
from num_conv.line_streamer import TxtFileLineStreamer
from num_conv.number_to_word_converter import Converter

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
    setup_logging("blabla.json", logging.DEBUG)
    txt_file_streamer = TxtFileLineStreamer('example_input.txt')
    input_parser = InputParser(txt_file_streamer)
    number_list = input_parser.get_numbers()
    converter = Converter()
    string_out = []
    for num in number_list:
        string_out.append(converter.convert(num))


if __name__ == '__main__':
    main()
