"""Contains the main entry point to the converter."""
from num_conv.io_handling import output_streamer_factory
from num_conv.io_handling import OutputStreamer, TxtFileInputStreamer
from num_conv.logic import Converter
from num_conv.logic import parse_line
import logging
import argparse

logger = logging.getLogger(__name__)


def run(input_file_location, output_file_location=None):
    """Runs the number converter on the file specified in input_file_location to the output file specified"""

    input_streamer = TxtFileInputStreamer(input_file_location)  # Currently only supports text file input
    output_streamer = output_streamer_factory(output_file_location)

    converter = Converter()

    logging.info("Processing input file")

    line = input_streamer.get_line()
    number_list = []
    while line:
        logging.debug("Processing the word:\t{}".format(line.rstrip()))
        number_from_line = parse_line(line)
        converted_number = converter.convert(number_from_line)

        output_streamer.set_line(converted_number)
        number_list.append(converted_number)

        # Get the next line of input
        line = input_streamer.get_line()

    return number_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert numbers in given file into words in given output location.')
    parser.add_argument('input', metavar='i', nargs=1, help='input file location')
    parser.add_argument('output', metavar='o', nargs=1, help='output file location')

    args = parser.parse_args()

    input_file_location = args.input[0]
    output_file_location = args.output[0]

    run(input_file_location, output_file_location)