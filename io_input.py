# def revert(string):
#     rev_string = string[::-1]
#
#     if string == rev_string:
#         print('Yes, it is a palindrome')
#     else:
#         print('No, it is not a palindrome')
#
# enter = input('Enter text: ')
# revert(enter)

# 案例
def reverse(text):
    return text[::-1]   # 利用步长对序列进行倒序取值

def is_palindrome(text):
    return text == reverse(text)

something = input('Enter text: ')
if is_palindrome(something):
    print('Yes, it is a palindrome')
else:
    print('No, it is not a palindrome')
