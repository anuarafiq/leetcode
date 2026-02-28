class Solution:
    def isHappy(self, n: int) -> bool:
        d = dict()

        while n != 1:
            copy = n
            digits = []
            while n:
                digits.append(n % 10)
                n = n // 10
            n = sum([int(n) ** 2 for n in digits])
            if n in d:
                return False
            d[copy] = False
        
        return True