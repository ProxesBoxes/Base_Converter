import sys
import Base_Converter
import getopt

def main(argv):
    print("base converter")
    lets_convert = Base_Converter.BaseConverter()
    print("select starting base:")
    lets_convert.starting_base = print_and_get_choices()
    lets_convert.starting_base_chars = Base_Converter.get_charset(lets_convert.starting_base)
    print("enter starting base value: ")
    if lets_convert.starting_base < 254:
        lets_convert.starting_base_value = Base_Converter.split(str(input()))
    else:
        lets_convert.starting_base_value = str(input())

    print("select ending base:")
    lets_convert.ending_base = print_and_get_choices()
    if lets_convert.starting_base < 254:
        lets_convert.ending_base_chars = Base_Converter.get_charset(lets_convert.ending_base)
    else:
        lets_convert.ending_base_chars = Base_Converter.generate_unicodes(lets_convert.ending_base)

    lets_convert.convert()

    print("Ending Value: " + "".join(lets_convert.ending_base_value))

def print_and_get_choices():
    print("2 standard_binary")
    print("8 standard_base_8")
    print("10 standard_base_10")
    print("16 standard_hex")
    print("32 standard_base_32")
    print("Or simply enter the base value you want and we'll try our best")
    print("enter # choice:")
    return int(input())

def populate_from_console(possible_args):
    ''' Return false if there was nothing to populate from the console '''
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(possible_args, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print
        'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print
            'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print
    'Input file is "', inputfile
    print
    'Output file is "', outputfile

    return False


if __name__ == '__main__':
    main(sys.argv[1:])
