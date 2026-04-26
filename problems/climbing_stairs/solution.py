class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n

        oneBefore = 3
        twoBefore = 2

        for i in range(4, n+1):
            steps = oneBefore + twoBefore
            twoBefore = oneBefore
            oneBefore = steps

        return steps