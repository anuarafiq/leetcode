class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s
        
        n = len(s)
        ans = [["" for i in range(n)] for _ in range(numRows)]
        ret = ""
        row, column = 0, 0
        i = 0
        while i < n:
            ans[row][column] = s[i]
            i += 1
            if row != numRows - 1:
                row += 1
            else:
                while row > 0 and i < n:
                    column += 1
                    row -= 1
                    ans[row][column] = s[i]
                    i += 1
                row += 1
            
        for row in range(numRows):
            for column in range(n):
                ret = ret + ans[row][column]

        return ret
    