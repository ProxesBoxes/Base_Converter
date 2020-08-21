import Globals


class BaseConverterException(Exception):

    class BaseExceedsSet(Exception):
        class Standard(Exception):
            def __init__(self):
                self.message = "Base exceeds ascii set please use a different character set."

        class NormalAscii(Exception):
            def __init__(self):
                self.message = "Base exceeds " + str(Globals.normal_ascii_max_size) + \
                               " thus \"normal_ascii_set\" can not be used."

    class InvalidBase(Exception):
        def __init__(self, starting_or_ending):
            self.message = "Invalid " + starting_or_ending + " base, only bases of 2 or higher are supported."

    class ExceedsBase(Exception):
        class Characters(Exception):
            def __init__(self, supplied_value, base, character_set):
                self.message = "The supplied value of \"" + str(supplied_value) + \
                               "\" exceeds the available values for base \"" + str(base) + \
                               "\" in the character set \""+character_set+"\""

        class Position(Exception):
            def __init__(self, supplied_value, base, character_set):
                self.message = "The position \""+str(supplied_value)+"\" exceeds the number of available "+\
                               "characters for base \""+str(base)+"\" in the character set \""+character_set+"\""

    class StartingValue(Exception):
        class NotSet(Exception):
            def __init__(self):
                self.message = "No starting value(s) were set"

        class NotListOfStrings(Exception):
            def __init__(self):
                self.message = "StartingValues are not a list of strings"
