#!/usr/bin/python3

import argparse
import sys

import Base_Converter
from Base_Converter_Exceptions import BaseConverterException
import Charsets


def main(argv):
    # Check to see if args were passed in and if they were then use them
    command_line_execution = False
    if len(argv) > 0:
        command_line_execution = True
        lets_convert = populate_from_console()

    else:
        # If not print the interactive menu
        print()
        print("--------------------------------------------------")
        print("|                 Base Converter                 |")
        print("|                                                |")
        print("| Built for The Information Technology Syndicate |")
        print("--------------------------------------------------")
        print()
        starting_base = int(input("Enter the starting base (default base 10): ") or 10)
        print()
        starting_base_value = str(input("Enter starting base value: ") or "0")
        print()
        starting_character_set = Charsets.detect_charset(starting_base_value)
        print("Select the starting base character set")
        starting_character_set = print_and_get_character_set(starting_character_set)
        print()
        ending_base = int(input("Enter the ending base (default base 10): ") or 10)
        print()
        print("Select the ending base character set")
        ending_character_set = print_and_get_character_set(starting_character_set)
        print()

        lets_convert = Base_Converter.BaseConverter(starting_base, starting_base_value, ending_base,
                                                    starting_character_set, ending_character_set)

    try:
        lets_convert.convert()
    except (BaseConverterException.InvalidBase, BaseConverterException.BaseExceedsSet.BaseExceedsStandard,
            BaseConverterException.BaseExceedsSet.BaseExceedsNormalAscii) as error:

        print(error.message)
        return

    if not command_line_execution:
        print("Converted Value: ", end="")

    print(lets_convert.return_output_for_viewing())

    if not command_line_execution:
        print()


def print_and_get_character_set(expected_character_set):
    print("  1 - standard")
    print("  2 - unicode")
    print("  3 - ascii")

    default = "1"
    if expected_character_set == Charsets.unicode_charset:
        default = "2"
    elif expected_character_set == Charsets.ascii_charset:
        default = "3"

    charset = str(input("  Enter character set # (default " + str(default) + "): ") or default)

    if charset == "" or charset == "1" or charset.lower() == Charsets.standard_charset:
        return Charsets.standard_charset
    if charset == "2" or charset.lower() == Charsets.unicode_charset:
        return Charsets.unicode_charset
    if charset == "3" or charset.lower() == Charsets.ascii_charset:
        return Charsets.ascii_charset

    return charset


def populate_from_console():
    parser = argparse.ArgumentParser(prog="Run_Base_Converter",
                                     description="A base converter tool which supports different character sets. "
                                                 "Currently only positive values, and positive bases are supported. The"
                                                 " different character sets supported currently are: " +
                                                 Charsets.predefined_charsets.__str__()[1:-1] + ".",
                                     epilog="Built for The Information Technology Syndicate")

    parser.add_argument("-sb", "--starting_base", help="The base in which the value to convert from, default is base 10"
                        , type=int, required=False, default=10)
    parser.add_argument("-sc", "--starting_character_set", help="The character set to us for the input, by default a "
                                                                "best attempt will be made at detecting the character "
                                                                "based off of the starting value", required=False)
    parser.add_argument("-ec", "--ending_character_set", help="The character set to us for the output, defaults to the "
                                                              "same character set as the starting character set",
                        required=False,
                        default=Charsets.standard_charset)
    parser.add_argument("starting_value", help="The value to convert from", type=str)
    parser.add_argument("ending_base", help="The base in which the value is to be converted to", type=int)
    args = parser.parse_args()

    if args.starting_character_set is None:
        args.starting_character_set = Charsets.detect_charset(args.starting_value)
    if args.ending_character_set is None:
        args.ending_character_set = args.starting_character_set

    return Base_Converter.BaseConverter(args.starting_base, args.starting_value, args.ending_base,
                                        args.starting_character_set, args.ending_character_set)


if __name__ == '__main__':
    main(sys.argv[1:])
