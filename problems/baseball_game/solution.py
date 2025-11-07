class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []

        for o in operations:
            if o == '+':
                ans.append(ans[-1] + ans[-2])
            elif o == 'D':
                ans.append(2 * ans[-1])
            elif o == 'C':
                ans.pop()
            else:
                ans.append(int(o))

        return sum(ans) 