""" Module for handling the logic for parsing and converting numbers into their text representation. """

import json
import settings
import logging
import os

logger = logging.getLogger(__name__)
here = os.path.dirname(os.path.abspath(__file__))


def parse_line(line):
    """Function for parsing a number out of a line of words.

    Parameters
    ----------
    line : string
        A string representing a single line of input.

    Returns
    -------
    int
        Integer containing the output integer.
    """

    words = line.split(" ")
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


class Converter:
    """Class responsible for converting an integer into its textual representation.

    Flexible to the language the integer should be converted into (currently only
    supports UK English).

    Attributes
    ----------
    language : string
        String containing the language for the integer to be converted in to.

    Methods
    -------
    convert(number)
        Converts a number into its text representation
    """

    def __init__(self, language='UK', invalid_number_string="number invalid"):
        with open(os.path.join(here, settings.LOCALE_DIR), 'rt') as json_file:
            lang_dict = json.load(json_file)

        if language not in lang_dict:
            logging.error("Unsupported language for converter.")
            raise ValueError("Unsupported language.")

        self.lang_words = lang_dict[language]
        self.__ones, self.__teens, self.__tens, self.__higher_groups, self.__hundred_string, self.__and = \
            self._set_text_representations()

        self.invalid_number_string = invalid_number_string

    def convert(self, number):
        """Converts the integer into its textual representation.

        Parameters
        ----------
        number : int
            The integer to be converted into its text representation

        Returns
        -------
        string
            The string containing the number converted into textual format.

        Raises
        ------
        ValueError
            If a negative integer is passed, throws a value error.
        """
        if number is None:
            return self.invalid_number_string
        elif number < 0:
            raise ValueError("Conversion accepts non-negative values only.")
        else:
            # The conversion involves recursively calling the function below. Here we call it with the initial
            # parameter values. The flag 'used_and' ensures that numbers such as 'three thousand AND 'two' get the 'and'
            # at the right time. The 'add_dash' flag is to ensure numbers like 'ninety-one' get the dash at the correct
            # time and the 'small_num' flag is there to ensure that numbers less than 1000 such as 31 don't get an and
            # at the front.
            return self._recursive_converter(number, "", 0, False, False, number < 1000)

    def _recursive_converter(self, number, digits_already_typed, thousands, used_and, add_dash=False, small_num=False):
        if number == 0:
            return digits_already_typed

        temp_digits_typed = digits_already_typed

        if len(temp_digits_typed) > 0:
            if add_dash is True:
                temp_digits_typed += "-"
            else:
                temp_digits_typed += " "

        include_and = not used_and and thousands == 0 and not small_num

        if number < 10:
            number_string = self.__ones[number]
            if include_and and not add_dash:
                temp_digits_typed += self.__and + " " + number_string
            else:
                # Here, we don't want to include an 'and' or we want to add a dash. Examples could be
                # either a small number like 7 or a number with a tens digit before hand like 38
                temp_digits_typed += number_string
                used_and = True
        elif number < 20:
            number_string = self.__teens[number - 10]
            if include_and:
                temp_digits_typed += self.__and + " " + number_string
            else:
                temp_digits_typed += number_string
                used_and = True
        elif number < 100:
            number_string = self._recursive_converter(number % 10,  self.__tens[number//10 - 2], 0, used_and, True)
            if include_and:
                temp_digits_typed += self.__and + " " + number_string
            else:
                temp_digits_typed += number_string
                used_and = True
        elif number < 1000:
            mod_number = number % 100
            appended_string = self.__ones[number//100] + self.__hundred_string
            if mod_number != 0:
                appended_string += " " + self.__and

            temp_digits_typed += self._recursive_converter(number % 100, appended_string, 0, True)
        else:
            # If we have a number larger than a thousand, we can split the number into it's first three digits, along
            # with its subsequent digits. For example: 500,654 is the same as 654 but with a five hundred thousand
            # component tacked on the front.
            temp_digits_typed += \
                self._recursive_converter(number % 1000,
                                          self._recursive_converter(number//1000, "",
                                                                    thousands+1, True), 0, used_and)
            if number % 1000 == 0:
                return temp_digits_typed

        return temp_digits_typed + self.__higher_groups[thousands]

    def _set_text_representations(self):
        return tuple(self.lang_words["ones"]), tuple(self.lang_words["teens"]), tuple(self.lang_words["tens"]), \
               tuple(self.lang_words["higher_groups"]), self.lang_words["hundred_string"], self.lang_words["and"]
