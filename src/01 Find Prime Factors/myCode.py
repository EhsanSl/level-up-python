#if we get input like 630
# function should return [2, 3, 3, 5, 7] => 630 = 2*3*3*5*7
# if input = 13, return 13 (since it has no factors)


# prime numbers are only devidable by themselvs and 1
def find_prime_factors(num):
    lst = []
    divisor = 2
    while divisor <= num:
        if num % divisor == 0:
            lst.append(divisor)
            num = num // divisor
        else:
            divisor += 1
    return lst


if __name__ == '__main__':
    num = int(input())
    lst = find_prime_factors(num=num)
    print(lst)
