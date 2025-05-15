class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1: return x
        L, R = 0, x
        ans = 0

        while L <= R:
            M = (L+R)//2
            if M*M == x:
                return M
            elif M*M < x:
                ans = M
                L = M + 1
            else: 
                R = M - 1
        return ans