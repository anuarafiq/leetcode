class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if x == 0: return 0
            if n == 0: return 1
            
            if n % 2 == 0:
                half = power(x, n // 2)
                return half * half
            else:
                half = power(x, (n-1) // 2)
                return half * half * x

        N = n
        if N < 0:
            x, N = 1/x, -N
        return power(x, N)