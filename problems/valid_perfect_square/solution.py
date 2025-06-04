class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        elif num < 4: return False
        L, R = 0, num//2

        while L <= R:
            M = (L+R) // 2
            if M*M == num:
                return True
            elif M*M > num:
                R = M - 1
            else:
                L = M + 1
        
        return False

