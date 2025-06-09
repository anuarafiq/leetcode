class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if a == 1: return 1
        i = int(''.join([str(j) for j in b]))

        return (pow(a, i, 1337))