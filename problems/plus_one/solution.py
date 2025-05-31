class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
    
        ret = []
        num = 0
        n = len(digits)
        for i in range(n):
            num += digits[-1-i] * (10**i)

        num += 1

        while num > 0:
            ret.append(num % 10)
            num //= 10
        
        return ret[::-1]