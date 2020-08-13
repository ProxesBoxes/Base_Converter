import Globals


class BaseConverterException(Exception):

    class BaseExceedsSet(Exception):
        class BaseExceedsStandard(Exception):
            def __init__(self):
                self.message = "Base exceeds ascii set please use a different character set."

        class BaseExceedsNormalAscii(Exception):
            def __init__(self):
                self.message = "Base exceeds " + str(Globals.normal_ascii_max_size) + \
                               " thus \"normal_ascii_set\" can not be used."

    class InvalidBase(Exception):
        def __init__(self, starting_or_ending):
            self.message = "Invalid " + starting_or_ending + " base, only bases of 2 or higher are supported."

    class ExceedsBase(Exception):
        def __init__(self, supplied_value, base, character_set):
            self.message = "The supplied value of \"" + str(supplied_value) + \
                           "\" exceeds the available values for base \"" + str(base) + \
                           "\" in the character set \""+character_set+"\""
