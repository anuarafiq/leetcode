class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        int1 = 0
        int2 = 0
        n = len(num1)
        m = len(num2)
        hashmap = {str(x): x for x in range(0,10)}

        for i in range(n):
            int1 += hashmap[num1[-1]] * (10**i)
            num1 = num1[:-1]

        for i in range(m):
            int2 += hashmap[num2[-1]] * (10**i)
            num2 = num2[:-1]

        return str(int1 * int2)