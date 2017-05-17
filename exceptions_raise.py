# class ShortInputException(Exception):
#     def __init__(self, length, atleast):
#         Exception.__init__(self)
#         self.length = length
#         self.atleast = atleast
#
#     def is_error(self):
#         if self.length < self.atleast:
#             print('ShortInputException: The input was {} long, expected at least {}'.format(self.length, self.atleast))
#         else:
#             print('No exception was raised.')
#
# something = input('Enter something --> ')
# s = ShortInputException(len(something), 3)
# s.is_error()

# 案例
class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:    # EOFError意味着它发现了一个不期望的文件尾（文件尾是由Ctrl-d引起的）
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print('ShortInputException: The input was {0} long, expected at least {1}'.format(ex.length, ex.atleast))
else:
    print('No exception was raised.')
