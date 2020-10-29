""" Module for dealing with parsing a stream of words into a list of numbers """

import logging

logger = logging.getLogger(__name__)


class InputParser:
    """ The class responsible for converting a stream of words into a list of numbers.

    Attributes
    ----------
    line_streamer : LineStreamer
        The line streamer object responsible for streaming in lines of text from a data source.

    Methods
    -------
    get_numbers()
        Returns a list of numbers contained in the words provided by the line_streamer.
    """

    def __init__(self, line_streamer, delimiter=" "):
        """
        Parameters
        ----------
        line_streamer : LineStreamer
            The LineStreamer object responsible for providing sentences to be parsed
        delimiter : string
            Hypothetically allows for words delimited with characters other than spaces - defaults to spaces.
        """

        self.line_streamer = line_streamer
        self.delimiter = delimiter
        logging.info("Input parser initialised with streamer of type {}".format(type(line_streamer)))

    def get_numbers(self):
        """Returns a list of numbers contained in the words provided by the line_streamer

        Returns
        ------
        list
            The list of numbers parsed out of the sentences streamed in. Note that if there is no valid number
            within a particular line then None is returned for that line.
        """

        logging.info("Processing input file")
        line = self.line_streamer.get_line()
        number_list = []
        while line:
            logging.debug("Processing the word:\t{}".format(line.rstrip()))
            processed_line = self._parse_line(line)
            number_list.append(processed_line)
            line = self.line_streamer.get_line()

        return number_list

    def _parse_line(self, line):
        """Private helper function for parsing a number out of a line of words.

        Parameters
        ----------
        line : string
            A string representing a single line of input.

        Returns
        -------
        int
            Integer containing the output integer.
        """

        words = line.split(self.delimiter)
        no_int_output = None
        for index, word in enumerate(words):
            if _represents_int(word):
                output_integer = int(word)

                # Here we check if we have a 'dodgy' number with a space in the middle followed by another number or
                # string starting like a number
                if index + 1 < len(words):
                    next_word = words[index + 1]
                    if _represents_int(next_word) or _represents_int(next_word[0]):
                        logging.debug("Line contained a number in the wrong format.")
                        return no_int_output

                logging.debug("Word contained the number: {}".format(output_integer))
                return output_integer

        logging.debug("Line did not contain a valid number")
        return no_int_output


def _represents_int(s):
    """Helper function to test if a string represents an integer."""
    try:
        int(s)
        return True
    except ValueError:
        return False
