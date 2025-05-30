import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        num = 0
        copy = x

        length = math.floor(math.log10(x)) + 1
        if length == 1:
            return True

        for i in range(length):
            digit = copy % 10
            num += digit * (10 ** (length - i - 1))
            copy //= 10

        return x == num
