#!/usr/bin/python3

import argparse
import sys

import Base_Converter
import Charsets


def main(argv):

    # Check to see if args were passed in and if they were then use them
    if len(argv) > 0:
        lets_convert = populate_from_console(argv)
        lets_convert.convert()

    else:
        # If not print the interactive menu
        print("base converter")
        print("select starting base:")
        starting_base = print_and_get_base_choices()
        print("enter starting base character set:")
        starting_character_set = print_and_get_character_set()
        print("enter starting base value: ")
        starting_base_value = str(input())
        print("select ending base:")
        ending_base = print_and_get_base_choices()
        print("enter ending base character set: ")
        ending_character_set = print_and_get_character_set()

        lets_convert = Base_Converter.BaseConverter(starting_base, starting_base_value, ending_base,
                                                    starting_character_set, ending_character_set)
        lets_convert.convert()
        print("Ending Value: ")

    print(lets_convert.return_output_for_viewing())


def print_and_get_base_choices():
    print("  2 standard_binary")
    print("  8 standard_base_8")
    print("  10 standard_base_10")
    print("  16 standard_hex")
    print("  32 standard_base_32")
    print("  Or simply enter the base value you want and we'll try our best")
    print("  enter # choice:")
    return int(input())


def print_and_get_character_set():
    print("  1 - standard (default)")
    print("  2 - unicode")
    print("  3 - ascii")
    charset = str(input())

    if charset == "" or charset == "1" or charset.lower() == Charsets.standard_charset:
        return Charsets.standard_charset
    if charset == "2" or charset.lower() == Charsets.unicode_charset:
        return Charsets.unicode_charset
    if charset == "3" or charset.lower() == Charsets.ascii_charset:
        return Charsets.ascii_charset

    return charset


def populate_from_console(lets_convert):

    parser = argparse.ArgumentParser()
    parser.add_argument("-sb", "--starting_base", help="The base in which the value to convert from is", type=int,
                        required=False, default=10)
    parser.add_argument("-sc", "--starting_character_set", help="The character set to us for the input",
                        required=False, default=Charsets.standard_charset)
    parser.add_argument("-ec", "--ending_character_set", help="The character set to us for the output",
                        required=False, default=Charsets.standard_charset)

    parser.add_argument("starting_value", help="The value to convert from")
    parser.add_argument("ending_base", help="The base in which the value to convert to", type=int)
    args = parser.parse_args()

    return Base_Converter.BaseConverter(args.starting_base, args.starting_value, args.ending_base,
                                        args.starting_character_set, args.ending_character_set)


if __name__ == '__main__':
    main(sys.argv[1:])
