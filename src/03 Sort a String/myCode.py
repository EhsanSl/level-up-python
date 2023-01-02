import re


def sort_words(string):

    lst = re.split(r'\W+', string)
    lst.sort(key=str.lower)
    str2 = " ".join(lst)
    return str2


if __name__ == '__main__':
    string = input("string :\n")
    result = sort_words(string)
    print(result)