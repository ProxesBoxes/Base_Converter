import string
import math

# All bases start with

standard_base_10 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
standard_ascii = list(string.ascii_uppercase) + ["[", "\\", "]", "^", "_", "`"] + list(string.ascii_lowercase) + \
    ["{", "|", "}", "~", "DEL"]

def print_and_get_choices():
    print("2 standard_binary")
    print("8 standard_base_8")
    print("10 standard_base_10")
    print("16 standard_hex")
    print("32 standard_base_32")
    print("Or simply enter the base value you want and we'll try our best")
    print("enter # choice:")
    return int(input())


def split(word):
    return [char for char in word]


def generate_unicodes(base):
    unicode_values = []
    for i in range(base):
        unicode_values += ["U+" + "{:04X}".format(i)]
    return unicode_values


def get_charset(base):
    ''' False denotes custom base was provided '''
    if base <= 10:
        return standard_base_10[:base]
    elif base <= len(standard_base_10 + standard_ascii[:base - 10]):
        return standard_base_10 + standard_ascii[:base - 10]

    return generate_unicodes(base)


class converter:
    starting_base = 0
    starting_base_chars = []
    starting_base_value = []
    ending_base = 0
    ending_base_chars = []
    ending_base_value = []

    def convert(self):
        # start with converting to base 10 value so we can maths
        position = 0
        base_10_value = 0
        if self.starting_base_value[:2] != "U+":
            self.starting_base_value.reverse()

            for char in self.starting_base_value:
                i = self.starting_base_chars.index(char)
                base_10_value += i * (math.pow(self.starting_base, position))
                position += 1
        else:
            base_10_value += self.starting_base_chars.index(self.starting_base_value)
        self.recuse_convert(base_10_value)

    def recuse_convert(self, value):
        cur_pos = math.floor(value / self.ending_base)
        if cur_pos >= self.ending_base:
            self.recuse_convert(cur_pos)
        else:
            self.ending_base_value += self.ending_base_chars[cur_pos]
        mod_val = value % self.ending_base
        self.ending_base_value += self.ending_base_chars[math.floor(mod_val)]


if __name__ == '__main__':
    print("base converter")
    lets_convert = converter()
    print("select starting base:")
    lets_convert.starting_base = print_and_get_choices()
    lets_convert.starting_base_chars = get_charset(lets_convert.starting_base)
    print("enter starting base value: ")
    lets_convert.starting_base_value = split(str(input()))

    print("select ending base:")
    lets_convert.ending_base = print_and_get_choices()
    if lets_convert.starting_base < 65:
        lets_convert.ending_base_chars = get_charset(lets_convert.ending_base)
    else:
        lets_convert.ending_base_chars = generate_unicodes(lets_convert.ending_base)

    lets_convert.convert()

    print("Ending Value: " + "".join(lets_convert.ending_base_value))
