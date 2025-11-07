class Solution:
    def arrangeCoins(self, n: int) -> int:
        L, R = 1, n
        
        while L <= R:
            M = (L+R) // 2
            possibleSum = M * (M+1) // 2

            if possibleSum == n:
                return M
            elif possibleSum > n:
                R = M - 1
            else:
                L = M + 1

        return R













        # if n == 1: return 1
        # count = 0
        # i = 1
         
        # while True:
        #     n -= i
        #     if n >= 0:
        #         count += 1
        #     i += 1
        #     if n < 0:
        #         break
        # return count