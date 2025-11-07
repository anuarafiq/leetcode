# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1: return 1
        L, R = 0, n
        firstBad = 0

        while L <= R:
            M = (L+R) // 2

            if isBadVersion(M):
                firstBad = M
                R = M - 1
            else:
                L = M + 1
            
        return firstBad