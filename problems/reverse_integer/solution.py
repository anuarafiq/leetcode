import math
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0
        
        sign = x / abs(x)
        x = str(abs(x))
        reverse = int(x[::-1])

        if reverse < -2**31 or reverse > 2**31 - 1:
            return 0

        return round(sign * reverse)