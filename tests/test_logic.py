import unittest
import num_conv.logic
from num_conv.logic import Converter


class TestLineParser(unittest.TestCase):
    def test_no_input(self):
        line = ""

        output = num_conv.logic.parse_line(line)

        self.assertEqual(None, output)

    def test_example_inputs(self):
        input_strings = [
            'The pump is 536 deep underground.',
            'We processed 9121 records.',
            'Variables reported as having a missing type #65678.',
            'Interactive and printable 10022 ZIP code.',
            'The database has 66723107008 records.',
            'I received 23 456,9 KGs.'
        ]
        output_ints = [536,9121, None, 10022, 66723107008, None]

        for input_string, output_int in zip(input_strings, output_ints):
            self.assertEqual(output_int, num_conv.logic.parse_line(input_string))

    def test_broken_number_input(self):
        input_string = 'ABC 12 3'  # Should fail since number format is broken
        self.assertEqual(None, num_conv.logic.parse_line(input_string))


class TestConverter(unittest.TestCase):
    def test_single_digit_input(self):
        int_input = 7
        converter = Converter()

        converted_int = converter.convert(int_input)
        expected_int = "seven"

        self.assertEqual(expected_int, converted_int)

    def test_teen_input(self):
        int_input = 14
        converter = Converter()

        converted_int = converter.convert(int_input)
        expected_int = "fourteen"

        self.assertEqual(expected_int, converted_int)

    def test_double_digit_input(self):
        int_input = [83, 50]
        converter = Converter()

        converted_int = [converter.convert(int_input[0]), converter.convert(int_input[1])]
        expected_int = ["eighty-three", "fifty"]

        self.assertEqual(expected_int[0], converted_int[0])
        self.assertEqual(expected_int[1], converted_int[1])

    def test_hundreds_inputs(self):
        int_inputs = [400, 370, 232, 105]
        converter = Converter()
        expected_ints = ["four hundred", "three hundred and seventy", "two hundred and thirty-two",
                         "one hundred and five"]

        for int_input, expected_int in zip(int_inputs, expected_ints):
            converted_int = converter.convert(int_input)
            self.assertEqual(expected_int, converted_int)

    def test_thousands_inputs(self):
        int_inputs = [2000, 3006, 5050, 4071, 6200, 7404, 8210, 1285]
        converter = Converter()
        expected_ints = [
            "two thousand",
            "three thousand and six",
            "five thousand and fifty",
            "four thousand and seventy-one",
            "six thousand two hundred",
            "seven thousand four hundred and four",
            "eight thousand two hundred and ten",
            "one thousand two hundred and eighty-five"
        ]
        for int_input, expected_int in zip(int_inputs, expected_ints):
            converted_int = converter.convert(int_input)
            self.assertEqual(expected_int, converted_int)

    def test_millions_inputs(self):
        int_inputs = [4731234, 567213, 2000000, 5000653, 967000, 7603400]
        converter = Converter()
        expected_ints = [
            "four million seven hundred and thirty-one thousand two hundred and thirty-four",
            "five hundred and sixty-seven thousand two hundred and thirteen",
            "two million",
            "five million six hundred and fifty-three",
            "nine hundred and sixty-seven thousand",
            "seven million six hundred and three thousand four hundred"
        ]
        for int_input, expected_int in zip(int_inputs, expected_ints):
            converted_int = converter.convert(int_input)
            self.assertEqual(expected_int, converted_int)


if __name__ == '__main__':
    unittest.main()
