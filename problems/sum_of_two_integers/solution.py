class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == b: return 2*a
        def sign(x):
            return x//abs(x)

        l = [sign(a) * 1 for _ in range(abs(a))] + [sign(b) * 1 for _ in range(abs(b))]

        return sum(l)
