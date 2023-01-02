# [::-1] reverses a string like
#   backward = forward[::-1]
import re


def identify_palindrome(string) -> bool:

    #explanation of below line
    #lst = re.findall('[a-z]+', string.lower())
    #string = ''.join(lst)
    string = ''.join(re.findall('[a-z]+', string.lower()))
    string_re = string[::-1]  # reverse of a string
    return string == string_re


def long_identify_plalindrome(string) -> bool:

    string = string.replace(" ", "")
    stack = []
    for i in string:
        stack.append(i)
    rev_string = string[::-1]

    for i in rev_string:
        if stack[0] == i:
            stack.pop(0)
            print(stack)
        else:
            return False
    return True


if __name__ == '__main__':
    string = str(input())
    #result = long_identify_plalindrome(string)
    result = identify_palindrome(string)
    print(result)
