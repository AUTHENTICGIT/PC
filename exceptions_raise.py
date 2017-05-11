class ShortInputException(Exception):
    def __init__(self, length, atleast):
        self.__init__(self)
        self.length = length
        self.atleast = atleast

    def is_erro(self):
        if self.length > self.atleast:
            print('ShortInputException: The input was {} long, expected at least {}'.format(self.length, self.atleast))
        else:
            print('No exception was raised.')

something = input()

s = ShortInputException()
