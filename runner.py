import argparse
from num_conv.engine import run


def main():
    parser = argparse.ArgumentParser(description='Convert numbers in given file into words in given output location.')

    parser.add_argument('--i', metavar='input', nargs=1, type=str, help='input file location', required=True)
    parser.add_argument('--o', metavar='output', nargs=1, type=str, help='output file location', required=False)

    args = parser.parse_args()

    input_file = args.i[0]

    if args.o is not None:
        output_file = args.o[0]
    else:
        output_file = None

    try:
        run(input_file, output_file)
    except FileNotFoundError:
        print("Incorrect file path provided")


if __name__ == "__main__":
    main()
