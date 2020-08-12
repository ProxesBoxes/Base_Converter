import Globals


class BaseConverterException(Exception):

    class BaseExceedsSet(Exception):
        class BaseExceedsStandard(Exception):
            def __init__(self):
                self.message = "Base exceeds standard ascii set please use a custom defined set"

        class BaseExceedsNormalAscii(Exception):
            def __init__(self):
                self.message = "Base exceeds " + str(Globals.normal_ascii_max_size) + \
                               " thus \"normal_ascii_set\" can not be used."

    class InvalidBase(Exception):
        def __init__(self, starting_or_ending):
            self.message = "Invalid " + starting_or_ending + " base, only bases of 2 or higher are supported"
