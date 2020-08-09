import sys
import Base_Converter
import argparse


def main(argv):
    lets_convert = None

    # Check to see if args were passed in and if they were then use them
    if len(argv) > 1:
        lets_convert = populate_from_console(argv)
        lets_convert.convert(lets_convert)

    else:
        # If not print the interactive menu
        print("base converter")
        print("select starting base:")
        starting_base = print_and_get_choices()
        print("enter starting base value: ")
        starting_base_value = str(input())
        print("select ending base:")
        ending_base = print_and_get_choices()

        lets_convert = Base_Converter.BaseConverter(starting_base, starting_base_value, ending_base)
        lets_convert.convert()
        print("Ending Value: ")

    print("".join(lets_convert.ending_base_value))


def print_and_get_choices():
    print("2 standard_binary")
    print("8 standard_base_8")
    print("10 standard_base_10")
    print("16 standard_hex")
    print("32 standard_base_32")
    print("Or simply enter the base value you want and we'll try our best")
    print("enter # choice:")
    return int(input())


def populate_from_console(lets_convert):

    parser = argparse.ArgumentParser()
    parser.add_argument("-sb", "starting_base", help="The base in which the value to convert from is", type=int)
    parser.add_argument("-sv", "starting_value", help="The value to convert from")
    parser.add_argument("-eb", "ending_base", help="The base in which the value to convert to is", type=int)

    args = parser.parse_args()

    return Base_Converter.BaseConverter(args.starting_base, args.starting_value, args.ending_base)


if __name__ == '__main__':
    main(sys.argv[1:])
