class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1, 1]]
        
        result = [[1], [1, 1]]
        for i in range(3, numRows+1):
            currRows = []
            for j in range(i):
                if j == 0 or j == i-1:
                    currRows.append(1)
                else:
                    currRows.append(result[-1][j] + result[-1][j-1])
            result.append(currRows)

        return result

